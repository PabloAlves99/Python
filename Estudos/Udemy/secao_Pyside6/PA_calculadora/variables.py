
"""
Este módulo define variáveis de configuração para a aplicação.

Módulo: variables.py
Autor: Pablo Alves

Variáveis:
    - ROOT_DIR: Caminho para o diretório raiz do projeto.
    - FILES_DIR: Caminho para o diretório 'files' dentro do diretório raiz.
    - WINDOW_ICON_PATH: Caminho para o arquivo 'big_icon.ico' dentro do
    diretório 'files'.

Constantes:
    - BIG_FONT_SIZE: Tamanho da fonte grande.
    - MEDIUM_FONT_SIZE: Tamanho da fonte média.
    - SMALL_FONT_SIZE: Tamanho da fonte pequena.
    - TEXT_MARGIN: Margem do texto.
    - MINIMUM_WIDTH: Largura mínima da janela.

Paleta de Cores:
    - PRIMARY_COLOR: Cor primária padrão.
    - DARKER_PRIMARY_COLOR: Tom mais escuro da cor primária.
    - DARKEST_PRIMARY_COLOR: Tom mais escuro ainda da cor primária.

Cores Especiais:
    - ESPECIAL_PRIMARY_COLOR: Cor primária especial.
    - ESPECIAL_DARKER_PRIMARY_COLOR: Tom mais escuro da cor primária especial.
    - ESPECIAL_DARKEST_PRIMARY_COLOR: Tom mais escuro ainda da cor primária
    especial.

"""
from pathlib import Path

ROOT_DIR = Path(__file__).parent
FILES_DIR = ROOT_DIR / 'files'
WINDOW_ICON_PATH = FILES_DIR / 'big_icon.ico'

# Sizing
BIG_FONT_SIZE = 30
MEDIUM_FONT_SIZE = 20
SMALL_FONT_SIZE = 18
TEXT_MARGIN = 10
MINIMUM_WIDTH = 400

# Colors
PRIMARY_COLOR = '#ED3237'
DARKER_PRIMARY_COLOR = '#BF2424'
DARKEST_PRIMARY_COLOR = '#8E1715'

# Especial Colors
ESPECIAL_PRIMARY_COLOR = '#222227'
ESPECIAL_DARKER_PRIMARY_COLOR = '#ED3237'
ESPECIAL_DARKEST_PRIMARY_COLOR = '#8E1715'
