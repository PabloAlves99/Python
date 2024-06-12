from tkinter import Tk, Button, Label, messagebox, Toplevel, Listbox, Entry
from pathlib import Path
from typing import List
from factory_app import IButtons
from pdf_processor import PDFProcessor
from PyPDF2 import PdfMerger


class DefaultButtons(IButtons):
    def __init__(self, root: Tk, top_frame, bottom_frame, color) -> None:
        self.processor = PDFProcessor()
        self.selected_pdfs: List[str] = []
        self.tooltip_manager = None
        self.top_frame = top_frame
        self.bottom_frame = bottom_frame
        self.root = root
        self.color = color
        self.create_buttons()
        self.show_buttons()
        self.preliminary_setup()

    def create_buttons(self):
        # Top frame buttons
        self.button_select_file = Button(self.top_frame,
                                         text='Selecionar PDF',
                                         bg=self.color.bg_button,
                                         command=self.select_file)
        self._file_name = Label(
            self.top_frame, text="Nenhum arquivo selecionado",
            bg=self.color.bg_label)

        self.output_folder = Button(self.top_frame,
                                    text='Salvar em:',
                                    bg=self.color.bg_button,
                                    command=self.select_folder)
        self._output_name = Label(
            self.top_frame, text="Nenhuma pasta selecionada",
            bg=self.color.bg_label)

        self.button_extract_text = Button(self.top_frame,
                                          text="Extrair Texto",
                                          bg=self.color.bg_button,
                                          command=self.extract_text)

        self.button_extract_images = Button(self.top_frame,
                                            text="Extrair Imagens",
                                            bg=self.color.bg_button,
                                            command=self.extract_images)

        self.button_separate_pdf = Button(self.top_frame,
                                          text="Separar PDF",
                                          bg=self.color.bg_button,
                                          command=self.save_separate_pdfs)

        self.salve_specific_page = Button(self.top_frame,
                                          text="Selecionar página(s) para "
                                          "salvar: ",
                                          bg=self.color.bg_button,
                                          command=self.save_specific_pages)

        self.label_specific_page = PlaceholderEntry(self.top_frame,
                                                    placeholder=' Ex: 2, 5, '
                                                    '7...')

        self.extract_text_specific = Button(self.top_frame,
                                            text="Extrair texto da Pagina: ",
                                            bg=self.color.bg_button,
                                            command=self.save_text_specific)

        self.label_text_specific = PlaceholderEntry(self.top_frame,
                                                    placeholder=' Ex: 2, 5, '
                                                    '7...')

        self.action_listbox = Listbox(self.top_frame)

        # bottom frame buttons
        self.button_listbox = Button(self.bottom_frame,
                                     text='Adicionar pdf na lista',
                                     bg=self.color.bg_button,
                                     command=self.add_pdf_to_pdf_list)

        self.select_pdf_from_listbox = Button(self.bottom_frame,
                                              text="Apagar PDF selecionado",
                                              bg=self.color.bg_button,
                                              command=self.get_selected_pdf)

        self.remove_list_items = Button(self.bottom_frame,
                                        text="Apagar itens da lista",
                                        bg=self.color.bg_button,
                                        command=self.remove_all_list)

        self.button_merge_pdfs = Button(self.bottom_frame,
                                        text="Juntar PDFs da lista",
                                        bg=self.color.bg_button,
                                        command=self.join_pdf_list)

        self.pdf_listbox = Listbox(self.bottom_frame,
                                   selectmode='multiple')

    def show_buttons(self):
        self._file_name.place(
            relx=0.02, rely=0.02, relwidth=0.47, relheight=0.11)
        self._output_name.place(
            relx=0.51, rely=0.02, relwidth=0.47, relheight=0.11)

        self.button_select_file.place(
            relx=0.15, rely=0.15, relwidth=0.20, relheight=0.11)
        self.output_folder.place(
            relx=0.65, rely=0.15, relwidth=0.20, relheight=0.11)

        self.button_extract_text.place(
            relx=0.02, rely=0.32, relwidth=0.26, relheight=0.11)
        self.button_extract_images.place(
            relx=0.02, rely=0.45, relwidth=0.26, relheight=0.11)
        self.button_separate_pdf.place(
            relx=0.02, rely=0.58, relwidth=0.26, relheight=0.11)

        self.salve_specific_page.place(
            relx=0.02, rely=0.71, relwidth=0.33, relheight=0.11)
        self.label_specific_page.place(
            relx=0.37, rely=0.71, relwidth=0.12, relheight=0.11)

        self.extract_text_specific.place(
            relx=0.02, rely=0.84, relwidth=0.33, relheight=0.11)
        self.label_text_specific.place(
            relx=0.37, rely=0.84, relwidth=0.12, relheight=0.11)

        self.action_listbox.place(
            relx=0.51, rely=0.32, relwidth=0.47, relheight=0.64)

        self.pdf_listbox.place(
            relx=0.40, rely=0.02, relwidth=0.55, relheight=0.90)
        self.button_listbox.place(
            relx=0.02, rely=0.06, relwidth=0.36, relheight=0.18)
        self.button_merge_pdfs.place(
            relx=0.02, rely=0.27, relwidth=0.36, relheight=0.18)
        self.select_pdf_from_listbox.place(
            relx=0.02, rely=0.49, relwidth=0.36, relheight=0.18)
        self.remove_list_items.place(
            relx=0.02, rely=0.71, relwidth=0.36, relheight=0.18)

    def preliminary_setup(self):
        self.buttons = [
            self.button_select_file, self.output_folder,
            self.button_extract_text, self.button_extract_images,
            self.button_separate_pdf, self.button_listbox,
            self.select_pdf_from_listbox, self.remove_list_items,
            self.button_merge_pdfs, self.salve_specific_page
        ]
        self.hover_effect_manager = HoverEffectManager(
            self.buttons, self.color.hover_button, self.color.bg_button
        )
        self.update_action_list(f'{' ' * 27}Ações realizadas')

    def select_file(self):
        self.processor.select_file_pdf()
        self.update_file_name()
        self.update_action_list('Arquivo PDF selecionado')

    def update_file_name(self):
        if self.processor.file_path:
            file_name = Path(self.processor.file_path).name
            self._file_name.config(text=f"PDF selecionado: {file_name}")

            self.tooltip_manager = TooltipManager(
                self._file_name, str(self.processor.file_path))
            self.processor.read_file_path()

    def select_folder(self):
        self.processor.select_output_folder()
        self.update_output_folder_name()
        self.update_action_list('Pasta para salvar o arquivo selecionada')

    def update_output_folder_name(self):
        if self.processor.root_folder:
            output_name = Path(self.processor.root_folder).name
            self._output_name.config(
                text=f"Pasta de destino: {output_name}")

            self.tooltip_manager = TooltipManager(
                self._output_name, str(self.processor.root_folder))
            self.processor.create_output_folder()

    def extract_text(self):
        if self.processor.reader:
            self.processor.extract_text_files()
            self.update_action_list("Texto extraído com sucesso!")
        else:
            messagebox.showerror("Erro", "Nenhum arquivo PDF foi carregado.")

    def extract_images(self):
        if self.processor.file_path:
            self.processor.extract_images()
            self.update_action_list("Imagens extraídas e salvas com sucesso.")
        else:
            messagebox.showwarning(
                "Aviso", "Por favor, selecione um arquivo PDF primeiro.")

    def save_separate_pdfs(self):
        if self.processor.file_path:
            self.processor.save_individual_pages_as_pdfs()
            self.update_action_list(
                "Páginas salvas individualmente com sucesso.")
        else:
            messagebox.showwarning(
                "Aviso", "Por favor, selecione um arquivo PDF primeiro.")

    def add_pdf_to_pdf_list(self):
        for pdf in self.processor.select_pdf_to_list():
            self.selected_pdfs.append(pdf)
            file_name = Path(pdf).name
            self.pdf_listbox.insert('end', file_name)
            self.update_action_list(f"PDF: {file_name} adicionado a lista")

    def remove_pdf_to_pdf_list(self, pdf_name):
        for index, _ in enumerate(self.selected_pdfs):
            if pdf_name in self.selected_pdfs[index]:
                self.selected_pdfs.pop(index)
                self.update_listbox()
                self.update_action_list(f"PDF: {Path(pdf_name).name} "
                                        "removido da lista")
                break

    def update_listbox(self):
        self.pdf_listbox.delete(0, "end")
        for pdf in self.selected_pdfs:
            file_name = Path(pdf).name
            self.pdf_listbox.insert('end', f'  {file_name}')

    def get_selected_pdf(self):
        # Obter o índice do item selecionado
        for index in self.pdf_listbox.curselection():
            if index:
                # Obter o nome do arquivo selecionado
                selected_pdf = self.pdf_listbox.get(index)
                self.remove_pdf_to_pdf_list(selected_pdf)
            else:
                print("Nenhum arquivo selecionado.")

    def remove_all_list(self):
        self.pdf_listbox.delete(0, "end")
        self.selected_pdfs.clear()
        self.update_action_list("PDFs removidos da lista")

    def join_pdf_list(self):
        if self.processor.root_folder:
            if self.selected_pdfs:
                self.processor.pdf_list = PdfMerger()
                for pdf in self.selected_pdfs:
                    self.processor.pdf_list.append(pdf)
                self.processor.merge_pdfs()
                self.remove_all_list()
                self.update_action_list("PDFs da lista juntados")
        else:
            messagebox.showerror("Erro",
                                 "Nenhuma pagina de destino foi selecionada.")

    def save_specific_pages(self):
        if self.processor.file_path:
            pages = self.label_specific_page.get().split(',')
            pages = [int(page.strip()) for page in pages]
            self.processor.save_specifics_pdf_pages(*pages)
            self.update_action_list(f"Páginas {pages} salvas com sucesso.")
        else:
            messagebox.showwarning(
                "Aviso", "Por favor, selecione um arquivo PDF primeiro.")

    def save_text_specific(self):
        if self.processor.file_path:
            pages = self.label_text_specific.get().split(',')
            pages = [int(page.strip()) for page in pages]
            for page in pages:
                text = self.processor.extract_text_from_page(page)
                self.processor.save_text(text, page)
                self.update_action_list(f"Texto da pagina \"{page}\" salvo "
                                        "com sucesso.")
        else:
            messagebox.showwarning(
                "Aviso", "Por favor, selecione um arquivo PDF primeiro.")

    def update_action_list(self, action):
        self.action_listbox.insert('end', f'  {action}')


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
        self.tooltip.wm_overrideredirect(1)  # type: ignore
        self.tooltip.wm_geometry(f"+{x}+{y}")
        label = Label(self.tooltip, text=self.text,
                      background="#ffffe0", relief="solid", borderwidth=1)
        label.pack()

    def hide_tooltip(self, event):
        events = []
        events.append(event)
        if self.tooltip:
            self.tooltip.destroy()
            self.tooltip = None


class HoverEffectManager:
    def __init__(self, buttons, hover_color, original_color):
        self.buttons = buttons
        self.hover_color = hover_color
        self.original_color = original_color
        self.add_hover_effects()

    def add_hover_effects(self):
        for button in self.buttons:
            button.bind("<Enter>", lambda event,
                        btn=button: self.on_enter(btn))
            button.bind("<Leave>", lambda event,
                        btn=button: self.on_leave(btn))

    def on_enter(self, button):
        button['background'] = self.hover_color

    def on_leave(self, button):
        button['background'] = self.original_color


class PlaceholderEntry(Entry):
    def __init__(self, frame=None, placeholder="", text_color='grey',
                 *args, **kwargs):
        super().__init__(frame, *args, **kwargs)

        self.placeholder = placeholder
        self.placeholder_color = text_color
        self.default_fg_color = self["fg"]

        self.bind("<FocusIn>", self.on_entry_focus_in)
        self.bind("<FocusOut>", self.on_entry_focus_out)

        self.set_placeholder()

    def set_placeholder(self):
        self.insert(0, self.placeholder)
        self.config(fg=self.placeholder_color)

    def on_entry_focus_in(self, event):
        if self.get() == self.placeholder:
            self.delete(0, 'end')
            self.config(fg=self.default_fg_color)

    def on_entry_focus_out(self, event):
        if not self.get():
            self.set_placeholder()
