#  pylint: disable= all

# # PyPDF2 para manipular arquivos PDF (Instalação)
# PyPDF2 para manipular arquivos PDF (PdfReader)
# PyPDF2 é uma biblioteca de manipulação de arquivos PDF feita em Python puro,
# gratuita e de código aberto. Ela é capaz de ler, manipular, escrever e unir
# dados de arquivos PDF, assim como adicionar anotações, transformar páginas,
# Link: https://pypdf2.readthedocs.io/en/3.0.0/

from pathlib import Path
from PyPDF2 import PdfMerger, PdfReader, PdfWriter

# Definindo caminhos para as pastas e o arquivo PDF de origem
PASTA_RAIZ = Path(__file__).parent
PASTA_ORIGINAL = PASTA_RAIZ / 'pdf_original'
PASTA_NOVA = PASTA_RAIZ / 'arquivos_novos'
RELATORIO_BACEN = PASTA_ORIGINAL / 'relatorio_do_mercado.pdf'

# Criando a pasta 'arquivos_novos' se ela não existir
PASTA_NOVA.mkdir(exist_ok=True)

# Criando um objeto PdfReader para ler o arquivo PDF de origem
reader = PdfReader(RELATORIO_BACEN)

# Obtendo a primeira página do PDF
page_0 = reader.pages[0]
# Obtendo a primeira imagem da primeira página do PDF
imagem_0 = page_0.images[0]


# PDFWriter

# Criando um novo arquivo no diretório 'arquivos_novos' com o nome da imagem
with open(PASTA_NOVA / imagem_0.name, 'wb') as fp:
    # Escrevendo os dados da imagem no arquivo recém-criado
    fp.write(imagem_0.data)

# Iterando sobre as páginas do reader e criando arquivos PDF separados para
# cada página
for page_number, page in enumerate(reader.pages):
    # Criando um objeto PdfWriter para escrever as páginas individuais
    writer = PdfWriter()
    with open(PASTA_NOVA / f'page_{page_number}.pdf', 'wb') as arquivo:
        # Adicionando a página ao objeto PdfWriter
        writer.add_page(page)
        # Escrevendo a página no arquivo PDF
        writer.write(arquivo)

# PDFMerger

# Criando uma lista de arquivos PDF individuais
files = [
    PASTA_NOVA / 'page_1.pdf',
    PASTA_NOVA / 'page_0.pdf',
]

merger = PdfMerger()
for file in files:
    # Adicionando cada arquivo à mesclagem
    merger.append(file)

# Escrevendo o arquivo mesclado (MERGED.pdf)
merger.write(PASTA_NOVA / 'MERGED.pdf')
# Fechando o objeto PdfMerger
merger.close()
