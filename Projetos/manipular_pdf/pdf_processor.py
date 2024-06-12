# pylint: disable=missing-docstring,empty-docstring
# type: ignore
from pathlib import Path
from tkinter import Tk
from tkinter.filedialog import askopenfilename, askopenfilenames, askdirectory
from typing import List, Optional, Union
from PyPDF2 import PdfMerger, PdfReader, PdfWriter
from PyPDF2.errors import PdfReadError


class PDFProcessor:

    def __init__(self, execute: bool = False) -> None:

        self.file_path: Optional[str] = None
        self.root_folder: Optional[Path] = None
        self.new_folder: Optional[Path] = None
        self.reader: Optional[PdfReader] = None
        self.pdf_list = PdfMerger()

        if execute:
            self.execute()

    def execute(self):
        self.select_file_pdf()
        self.select_output_folder()
        self.read_file_path()
        self.create_output_folder()

    def select_file_pdf(self):
        root = Tk()
        root.withdraw()
        self.file_path = askopenfilename(title="Selecione o arquivo PDF",
                                         filetypes=[("PDF files", "*.pdf")])
        root.destroy()

    def select_output_folder(self):
        self.root_folder = Path(askdirectory(
            title="Selecione onde deseja salvar"))

    def read_file_path(self):
        try:
            if self.file_path:
                self.reader = PdfReader(self.file_path)
            else:
                self.reader = None
        except FileNotFoundError as e:
            print(f"Erro: Arquivo não encontrado - {e}")
            self.reader = None
        except PdfReadError as e:
            print(f"Erro: Falha ao ler o arquivo PDF - {e}")
            self.reader = None

    def create_output_folder(self):
        if self.root_folder and self.root_folder != Path('.'):
            self.new_folder = self.root_folder / "novos_pdf"
            self.new_folder.mkdir(exist_ok=True)
        else:
            print("Nenhuma pasta selecionada.")

    def get_num_pages(self) -> Optional[int]:
        return len(self.reader.pages) if self.reader is not None else None

    def has_text_content(self) -> bool:
        return any(
            page.extract_text() for page in
            self.reader.pages) if self.reader is not None else False

    def has_image_content(self) -> bool:
        return any(
            page.images for page in
            self.reader.pages) if self.reader is not None else False

    def page_extraction(self) -> List[str]:
        return [page.extract_text() for page in
                self.reader.pages] if self.reader is not None else [
                    'PDF sem texto']

    def extract_text_from_page(self, page) -> str:
        return (self.reader.pages[page - 1].extract_text() if self.reader
                is not None else ['page precisa ser int'])

    def save_text(self, text_list: Union[List[str], str],
                  page: Optional[int] = None):

        if self.new_folder:

            if page is None:

                for page_number, text in enumerate(text_list):
                    with open(self.new_folder / f'page_{page_number}.txt', 'w',
                              encoding='utf-8') as texto_arquivo:
                        texto_arquivo.write(text)

            else:
                with open(self.new_folder / f'page_{page}.txt', 'w',
                          encoding='utf-8') as texto_arquivo:
                    texto_arquivo.write(text_list)  # type: ignore

    def extract_text_files(self, page: Optional[int] = None):

        if page is None:
            texts = self.page_extraction()
            self.save_text(texts)

        elif isinstance(page, int):
            num_pages = self.get_num_pages()
            is_page_valid = 1 <= page <= num_pages  # type: ignore

            if is_page_valid:
                text = self.extract_text_from_page(page)
                self.save_text(text, page)

            elif is_page_valid is False:
                print(
                    f"Página {page} está fora do intervalo válido "
                    f"(1 - {num_pages}).")

    def extract_images(self):
        if self.reader is None:
            print("Nenhum arquivo PDF carregado.")
            return

        for page_number, page in enumerate(self.reader.pages):
            # Extraindo e salvando todas as imagens de cada página
            for image_index, image in enumerate(page.images):
                with open(self.new_folder / f'page_{page_number + 1}'
                          f'_image_{image_index}.png', 'wb') as img_file:
                    img_file.write(image.data)

    def save_individual_pages_as_pdfs(self):
        if self.reader is None:
            print("Nenhum arquivo PDF carregado.")
            return

        # Criando um objeto PdfWriter para escrever as páginas individuais
        for page_number, page in enumerate(self.reader.pages):
            writer = PdfWriter()
            with open(self.new_folder / f'page_{page_number}.pdf',
                      'wb') as arquivo:
                writer.add_page(page)
                writer.write(arquivo)

    def save_specifics_pdf_pages(self, *args):
        if self.reader is None:
            print("Nenhum arquivo PDF carregado.")
            return

        try:
            pages_number = args

            for page_number in pages_number:
                writer = PdfWriter()
                writer.add_page(self.reader.pages[page_number - 1])
                specific_pdf_path = self.new_folder / f'page_{page_number}.pdf'
                with open(specific_pdf_path, 'wb') as sf:
                    writer.write(sf)
                print(f"A página {page_number} foi salva em "
                      f"{specific_pdf_path}.")

        except IndexError:
            print(f"Erro: O PDF possui {len(pages_number)} paginas")

    def select_pdf_to_list(self) -> List[str]:
        files = askopenfilenames(
            title="Selecione os PDFs que deseja juntar",
            filetypes=[("PDF files", "*.pdf")]
        )
        return files

    def merge_pdfs(self):

        if not self.pdf_list.pages:
            for pdf_file in self.select_pdf_to_list():
                self.pdf_list.append(pdf_file)

            if not self.pdf_list:
                print("Nenhum PDF selecionado.")
                return

        if self.new_folder is not None:
            merged_pdf_path = self.new_folder / 'merged_pdfs.pdf'

            with open(merged_pdf_path, 'wb') as merged_file:
                self.pdf_list.write(merged_file)


# if __name__ == "__main__":
#     x = PDFProcessor(execute=True)
#     x.merge_pdfs()
