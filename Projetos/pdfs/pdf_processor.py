# pylint: disable=missing-docstring,empty-docstring
import sys
from pathlib import Path
from tkinter import Tk
from tkinter.filedialog import askopenfilename, askopenfilenames
from tkinter.filedialog import askdirectory
from typing import List, Optional, Union
from PyPDF2 import PdfMerger, PdfReader, PdfWriter
from PyPDF2.errors import PdfReadError


class PDFProcessor:

    def __init__(self, execute: bool = False) -> None:

        self.file_path: Optional[str] = None
        self.root_folder: Optional[Path] = None
        self.new_folder: Optional[Path] = None
        self.reader: Optional[PdfReader] = None

        if execute:
            self.execute()

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
                print("Caminho do arquivo selecionado:", self.file_path)
            else:
                print("Nenhum arquivo selecionado.")
                self.reader = None
                sys.exit()
        except FileNotFoundError as e:
            print(f"Erro: Arquivo não encontrado - {e}")
        except PdfReadError as e:
            print(f"Erro: Falha ao ler o arquivo PDF - {e}")
        except Exception as e:
            print(f"Erro ao ler o arquivo PDF: {e}")
            self.reader = None
            sys.exit()

    def create_output_folder(self):
        if self.root_folder and self.root_folder != Path('.'):
            self.new_folder = self.root_folder / "novos_pdf"
            self.new_folder.mkdir(exist_ok=True)
            print(f"Nova pasta criada: {self.new_folder}")
        else:
            print("Nenhuma pasta selecionada.")

    def execute(self):
        self.select_file_pdf()
        self.select_output_folder()
        self.read_file_path()
        self.create_output_folder()

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

    def __extract_text(self) -> List[str]:
        return [page.extract_text() for page in
                self.reader.pages] if self.reader is not None else [
                    'PDF sem texto']

    def __extract_text_from_page(self, page):
        return (self.reader.pages[page - 1].extract_text() if self.reader
                is not None else ['page precisa ser int'])

    def __save_texts(
            self, text_list: Union[
                str, List[str]], page: Optional[int] = None):
        if self.new_folder:
            if page is None:
                for page_number, text in enumerate(text_list):
                    with open(self.new_folder / f'page_{page_number}.txt', 'w',
                              encoding='utf-8') as texto_arquivo:
                        texto_arquivo.write(text)
            else:
                with open(self.new_folder / f'page_{page}.txt', 'w',
                          encoding='utf-8') as texto_arquivo:
                    texto_arquivo.write(text_list)

    def extract_text_files(self, page: Optional[int] = None):

        if page is None:
            texts = self.__extract_text()
            self.__save_texts(texts)

        elif isinstance(page, int):
            num_pages = self.get_num_pages()
            is_page_valid = 1 <= page <= num_pages

            if num_pages is not None and is_page_valid:
                text = self.__extract_text_from_page(page)
                self.__save_texts(text, page)

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
                with open(self.new_folder / f'page_{page_number+1}'
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

        print("Todas as páginas individuais foram salvas em PDF.")

    def save_specifics_pdf_pages(self, *args):
        if self.reader is None:
            print("Nenhum arquivo PDF carregado.")
            return

        try:
            pages_number = args
            writer = PdfWriter()
            for page_number in pages_number:
                writer.add_page(self.reader.pages[page_number - 1])
                specific_pdf_path = self.new_folder / f'page_{page_number}.pdf'
                with open(specific_pdf_path, 'wb') as sf:
                    writer.write(sf)
                print(f"A página {page_number} foi salva em {
                      specific_pdf_path}.")

        except IndexError:
            print(f"Erro: O PDF possui {len(pages_number)}")
        except Exception as e:
            print(f"Erro ao salvar as páginas: {e}")

    def merge_selected_pdfs(self):
        # Abrindo uma nova janela para selecionar os PDFs a serem mesclados
        root = Tk()
        root.withdraw()
        pdf_files = askopenfilenames(
            title="Selecione os PDFs que deseja juntar",
            filetypes=[("PDF files", "*.pdf")]
        )
        root.destroy()  # Fechando a janela após a seleção

        # Verificando se algum arquivo foi selecionado
        if not pdf_files:
            print("Nenhum arquivo selecionado.")
            return

        # Criando um objeto PdfMerger para mesclar os PDFs selecionados
        merger = PdfMerger()
        for pdf_file in pdf_files:
            merger.append(pdf_file)

        # Salvando o PDF mesclado
        self.select_output_folder()
        self.create_output_folder()
        merged_pdf_path = self.new_folder / 'merged_selected_pdfs.pdf'
        with open(merged_pdf_path, 'wb') as merged_file:
            merger.write(merged_file)

        print(f"Os PDFs selecionados foram mesclados em {merged_pdf_path}.")


if __name__ == "__main__":
    x = PDFProcessor(execute=True)
    x.save_specifics_pdf_pages(1, 2)
