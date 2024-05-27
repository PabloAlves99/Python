from tkinter import Tk, Button, Label, Entry, messagebox, StringVar, Frame
from tkinter import filedialog, ttk
# Supondo que a classe esteja em um arquivo chamado PDFProcessor.py
from manipular_pdf import PDFProcessor
from pathlib import Path


class PDFProcessorApp:
    def __init__(self, root):
        self.processor = PDFProcessor()
        self.root = root
        self.root.title("Manipulador de PDF")

        # Definindo o tamanho mínimo da janela
        self.root.minsize(500, 400)

        # Frames para organizar a disposição dos widgets
        self.top_frame = Frame(root)
        self.top_frame.pack(side="top", fill="both",
                            expand=True, padx=10, pady=10)

        self.bottom_frame = Frame(root)
        self.bottom_frame.pack(side="bottom", fill="x", padx=10, pady=10)

        # Widgets no frame superior
        self.file_label = Label(
            self.top_frame, text="Nenhum arquivo selecionado")
        self.file_label.pack(pady=5)

        self.folder_label = Label(
            self.top_frame, text="Nenhuma pasta selecionada")
        self.folder_label.pack(pady=5)

        self.page_entry_label = Label(
            self.top_frame, text="Páginas específicas (separadas por vírgula)")
        self.page_entry_label.pack(pady=5)

        self.page_entry = Entry(self.top_frame)
        self.page_entry.pack(pady=5)

        self.select_file_button = Button(
            self.top_frame, text="Selecionar Arquivo PDF", command=self.select_file)
        self.select_file_button.pack(pady=5)

        self.select_folder_button = Button(
            self.top_frame, text="Selecionar Pasta de Saída", command=self.select_folder)
        self.select_folder_button.pack(pady=5)

        # Widgets no frame inferior
        self.extract_text_button = Button(
            self.bottom_frame, text="Extrair Texto", command=self.extract_text)
        self.extract_text_button.pack(side="left", padx=5)

        self.extract_images_button = Button(
            self.bottom_frame, text="Extrair Imagens", command=self.extract_images)
        self.extract_images_button.pack(side="left", padx=5)

        self.save_individual_pdfs_button = Button(
            self.bottom_frame, text="Salvar Páginas Individualmente", command=self.save_individual_pdfs)
        self.save_individual_pdfs_button.pack(side="left", padx=5)

        self.save_specific_pages_button = Button(
            self.bottom_frame, text="Salvar Páginas Específicas", command=self.save_specific_pages)
        self.save_specific_pages_button.pack(side="left", padx=5)

        self.merge_pdfs_button = Button(
            self.bottom_frame, text="Mesclar PDFs Selecionados", command=self.merge_pdfs)
        self.merge_pdfs_button.pack(side="left", padx=5)

        self.toggle_theme_button = Button(
            self.bottom_frame, text="Alternar Tema", command=self.toggle_theme)
        self.toggle_theme_button.pack(side="left", padx=5)

        # Estado do tema
        self.dark_mode = False

    def select_file(self):
        self.processor.select_file_pdf()
        if self.processor.file_path:
            file_name = Path(self.processor.file_path).name
            self.file_label.config(text=f"Arquivo selecionado: {file_name}")

    def select_folder(self):
        self.processor.select_output_folder()
        if self.processor.root_folder:
            self.folder_label.config(text=f"Pasta selecionada: {
                                     self.processor.root_folder}")

    def extract_text(self):
        self.processor.execute()
        self.processor.extract_text_files()
        messagebox.showinfo("Sucesso", "Texto extraído e salvo com sucesso.")

    def extract_images(self):
        self.processor.execute()
        self.processor.extract_images()
        messagebox.showinfo(
            "Sucesso", "Imagens extraídas e salvas com sucesso.")

    def save_individual_pdfs(self):
        self.processor.execute()
        self.processor.save_individual_pages_as_pdfs()
        messagebox.showinfo(
            "Sucesso", "Páginas salvas individualmente com sucesso.")

    def save_specific_pages(self):
        pages = self.page_entry.get().split(',')
        pages = [int(page.strip()) for page in pages]
        self.processor.execute()
        self.processor.save_specifics_pdf_pages(*pages)
        messagebox.showinfo(
            "Sucesso", "Páginas específicas salvas com sucesso.")

    def merge_pdfs(self):
        self.processor.merge_selected_pdfs()
        messagebox.showinfo("Sucesso", "PDFs mesclados com sucesso.")

    def toggle_theme(self):
        self.dark_mode = not self.dark_mode
        if self.dark_mode:
            self.apply_dark_theme()
        else:
            self.apply_light_theme()

    def apply_dark_theme(self):
        self.root.config(bg="black")
        for widget in self.root.winfo_children():
            widget.config(bg="black", fg="white")
        for frame in [self.top_frame, self.bottom_frame]:
            for widget in frame.winfo_children():
                widget.config(bg="black", fg="white")

    def apply_light_theme(self):
        self.root.config(bg="white")
        for widget in self.root.winfo_children():
            widget.config(bg="white", fg="black")
        for frame in [self.top_frame, self.bottom_frame]:
            for widget in frame.winfo_children():
                widget.config(bg="white", fg="black")


if __name__ == "__main__":
    root = Tk()
    app = PDFProcessorApp(root)
    root.mainloop()
