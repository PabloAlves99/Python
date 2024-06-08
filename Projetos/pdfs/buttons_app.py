from tkinter import Toplevel, Label
from tkinter import Tk, Button, Label, messagebox, Toplevel
from pathlib import Path
from factory_app import IButtons
from pdf_processor import PDFProcessor


class DefaultButtons(IButtons):
    def __init__(self, root: Tk, top_frame, bottom_frame) -> None:
        self.processor = PDFProcessor()
        self.tooltip_manager = None
        self.top_frame = top_frame
        self.bottom_frame = bottom_frame
        self.root = root
        self.create_buttons()
        self.show_buttons()

    def create_buttons(self):
        self.button_select_file = Button(self.top_frame,
                                         text='Selecionar PDF',
                                         bg="#DBDBDB",
                                         command=self.select_file)
        self._file_name = Label(
            self.top_frame, text="Nenhum arquivo selecionado", bg="#DBDBDB",)

        self.output_folder = Button(self.top_frame,
                                    text='Selecionar pasta de saída',
                                    bg="#DBDBDB",
                                    command=self.select_folder)
        self._output_name = Label(
            self.top_frame, text="Nenhuma pasta selecionada", bg="#DBDBDB")

        self.button_extract_text = Button(
            self.bottom_frame, text="Extrair Texto", command=self.extract_text)

        self.button_extract_images = Button(
            self.bottom_frame, text="Extrair Imagens",
            command=self.extract_images)

        self.button_separate_pdf = Button(
            self.bottom_frame, text="Separar PDF",
            command=self.save_separate_pdfs)

    def show_buttons(self):
        self.button_select_file.place(
            relx=0.02, rely=0.02, relwidth=0.36, relheight=0.20)
        self._file_name.place(
            relx=0.40, rely=0.02, relwidth=0.55, relheight=0.20
        )

        self.output_folder.place(
            relx=0.02, rely=0.24, relwidth=0.36, relheight=0.20
        )
        self._output_name.place(
            relx=0.40, rely=0.24, relwidth=0.55, relheight=0.20
        )

        self.button_extract_text.place(
            relx=0.02, rely=0.02, relwidth=0.25, relheight=0.15
        )

        self.button_extract_images.place(
            relx=0.38, rely=0.02, relwidth=0.25, relheight=0.15
        )

        self.button_separate_pdf.place(
            relx=0.73, rely=0.02, relwidth=0.25, relheight=0.15
        )

    def select_file(self):
        self.processor.select_file_pdf()
        self.update_file_name()

    def update_file_name(self):
        if self.processor.file_path:
            file_name = Path(self.processor.file_path).name
            self._file_name.config(text=f"PDF: {file_name}")

            self.tooltip_manager = TooltipManager(
                self._file_name, str(self.processor.file_path))

    def select_folder(self):
        self.processor.select_output_folder()
        self.update_output_folder_name()

    def update_output_folder_name(self):
        if self.processor.root_folder:
            output_name = Path(self.processor.root_folder).name
            self._output_name.config(
                text=f"Pasta de destino: {output_name}")

            self.tooltip_manager = TooltipManager(
                self._output_name, str(self.processor.root_folder))

    def extract_text(self):
        self.processor.read_file_path()
        self.processor.create_output_folder()
        if self.processor.reader:
            self.processor.extract_text_files()
            messagebox.showinfo("Sucesso", "Texto extraído com sucesso!")
        else:
            messagebox.showerror("Erro", "Nenhum arquivo PDF foi carregado.")

    def extract_images(self):
        self.processor.read_file_path()
        self.processor.create_output_folder()
        if self.processor.file_path:
            self.processor.extract_images()
            messagebox.showinfo(
                "Sucesso", "Imagens extraídas e salvas com sucesso.")
        else:
            messagebox.showwarning(
                "Aviso", "Por favor, selecione um arquivo PDF primeiro.")

    def save_separate_pdfs(self):
        self.processor.read_file_path()
        self.processor.create_output_folder()
        if self.processor.file_path:
            self.processor.save_individual_pages_as_pdfs()
            messagebox.showinfo(
                "Sucesso", "Páginas salvas individualmente com sucesso.")
        else:
            messagebox.showwarning(
                "Aviso", "Por favor, selecione um arquivo PDF primeiro.")

    def save_specific_pages(self):
        if self.processor.file_path:
            pages = self.page_entry.get().split(',')
            pages = [int(page.strip()) for page in pages]
            self.processor.save_specifics_pdf_pages(*pages)
            messagebox.showinfo(
                "Sucesso", "Páginas específicas salvas com sucesso.")
        else:
            messagebox.showwarning(
                "Aviso", "Por favor, selecione um arquivo PDF primeiro.")

    def merge_pdfs(self):
        self.processor.merge_selected_pdfs()


class TooltipManager:
    def __init__(self, widget, text):
        self.widget = widget
        self.text = text
        self.tooltip = None
        self.bind_events()

    def bind_events(self):
        self.widget.bind("<Enter>", self.show_tooltip)
        self.widget.bind("<Leave>", self.hide_tooltip)

    def show_tooltip(self, event):
        x = event.widget.winfo_rootx() + 20
        y = event.widget.winfo_rooty() + 20
        self.tooltip = Toplevel(event.widget)
        self.tooltip.wm_overrideredirect(1)
        self.tooltip.wm_geometry(f"+{x}+{y}")
        label = Label(self.tooltip, text=self.text,
                      background="#ffffe0", relief="solid", borderwidth=1)
        label.pack()

    def hide_tooltip(self, event):
        if self.tooltip:
            self.tooltip.destroy()
            self.tooltip = None
