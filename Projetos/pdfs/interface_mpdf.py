from tkinter import Tk, Button, Label, Entry, messagebox, StringVar, Frame
from tkinter import filedialog, ttk
# Supondo que a classe esteja em um arquivo chamado PDFProcessor.py
from manipular_pdf import PDFProcessor
from pathlib import Path


class PDFProcessorApp:
    def __init__(self, root):
        self.processor = PDFProcessor()
        self.root = root
        self.configs_app()
        self.display_frames()
        self._select_file_pdf()
        self._select_output_folder()
        self.display_buttons()

    def configs_app(self):
        self.root.title("Manipulador de PDF")
        self.root.minsize(450, 400)
        self.root.configure(background='#D0E4F2')
        self.root.resizable(True, True)

    def display_frames(self):
        self.top_frame = Frame(self.root, bd=4, bg='#A3C9D9',
                               highlightbackground='#A9CDDA',
                               highlightthickness=3)
        self.top_frame.place(relx=0.02, rely=0.02,
                             relwidth=0.96, relheight=0.32)

        self.bottom_frame = Frame(self.root, bd=4, bg='#A3C9D9',
                                  highlightbackground='#A9CDDA',
                                  highlightthickness=3)
        self.bottom_frame.place(relx=0.02, rely=0.35,
                                relwidth=0.96, relheight=0.62)

    def _select_file_pdf(self):
        self.button_select_file = Button(self.top_frame,
                                         text='Selecionar PDF', bd=2,
                                         bg="#FFF",
                                         command=self.select_file)
        self._file_name = Label(
            self.top_frame, text="Nenhum arquivo selecionado")

    def select_file(self):
        self.processor.select_file_pdf()
        self.update_file_name()

    def update_file_name(self):
        if self.processor.file_path:
            file_name = Path(self.processor.file_path).name
            self._file_name.config(text=f"Arquivo selecionado: {file_name}")

    def _select_output_folder(self):
        self.output_folder = Button(self.top_frame,
                                    text='Selecionar pasta de saída',
                                    bd=2,
                                    bg="#FFF",
                                    command=self.select_folder)
        self._output_name = Label(
            self.top_frame, text="Nenhuma pasta selecionada")

    def select_folder(self):
        self.processor.select_output_folder()
        self.update_output_folder_name()

    def update_output_folder_name(self):
        output_name = self.processor.root_folder
        self._output_name.config(
            text=f"Pasta de saída selecionada: {output_name}")

    def display_buttons(self):
        self.button_select_file.place(
            relx=0.02, rely=0.02, relwidth=0.25, relheight=0.20)
        self._file_name.place(
            relx=0.02, rely=0.25, relwidth=0.95, relheight=0.20
        )

        self.output_folder.place(
            relx=0.02, rely=0.52, relwidth=0.35, relheight=0.20
        )
        self._output_name.place(
            relx=0.02, rely=0.75, relwidth=0.95, relheight=0.20
        )


if __name__ == "__main__":
    _root = Tk()
    app = PDFProcessorApp(_root)
    _root.mainloop()
