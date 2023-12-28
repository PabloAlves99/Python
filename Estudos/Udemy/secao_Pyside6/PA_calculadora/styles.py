#  pylint: disable=no-name-in-module
#  type: ignore

"""
Este módulo configura o tema visual da aplicação utilizando a biblioteca
QDarkTheme.

A paleta de cores e estilos são definidos no arquivo e aplicados através da
função `setup_theme()`.

Módulo: styles.py
Autor: Pablo Alves

Classes e Funções:
    - setup_theme(): Configura o tema visual da aplicação.

Constantes de Cores:
    - PRIMARY_COLOR: Cor primária padrão.
    - DARKER_PRIMARY_COLOR: Tom mais escuro da cor primária.
    - DARKEST_PRIMARY_COLOR: Tom mais escuro ainda da cor primária.
    - ESPECIAL_PRIMARY_COLOR: Cor primária especial.
    - ESPECIAL_DARKER_PRIMARY_COLOR: Tom mais escuro da cor primária especial.
    - ESPECIAL_DARKEST_PRIMARY_COLOR: Tom mais escuro ainda da cor primária
    especial.

Estrutura QSS (Qt Style Sheets):
    - Define os estilos para botões especiais e seus efeitos (hover, pressed).

Dependências:
    - qdarktheme: Biblioteca para aplicar temas escuros em aplicações
    PyQt/PySide.


"""
import qdarktheme
from variables import (
    PRIMARY_COLOR, DARKER_PRIMARY_COLOR, DARKEST_PRIMARY_COLOR,
    ESPECIAL_PRIMARY_COLOR, ESPECIAL_DARKER_PRIMARY_COLOR,
    ESPECIAL_DARKEST_PRIMARY_COLOR)

qss = f"""
    QPushButton[cssClass="specialButtonSpace"] {{
        color: #fff;
        background: {PRIMARY_COLOR};
    }}
    QPushButton[cssClass="specialButtonSpace"]:hover {{
        color: #fff;
        background: {DARKER_PRIMARY_COLOR};
    }}
    QPushButton[cssClass="specialButtonSpace"]:pressed {{
        color: #fff;
        background: {DARKEST_PRIMARY_COLOR};
    }}

    QPushButton[cssClass="specialButton"] {{
        color: #ED3237;
        background: {ESPECIAL_PRIMARY_COLOR};
    }}
    QPushButton[cssClass="specialButton"]:hover {{
        color: #fff;
        background: {ESPECIAL_DARKER_PRIMARY_COLOR};
    }}
    QPushButton[cssClass="specialButton"]:pressed {{
        color: #fff;
        background: {ESPECIAL_DARKEST_PRIMARY_COLOR};
    }}
"""


def setup_theme():
    """
    Configura o tema visual da aplicação utilizando a biblioteca QDarkTheme.

    Esta função aplica estilos específicos aos botões e define as cores
    principais do tema.

    Parâmetros:
        Nenhum.

    Retorno:
        Nenhum.

    Exemplo:
        ```python
        from styles import setup_theme

        # ... código da aplicação ...

        setup_theme()
        ```
    """
    qdarktheme.setup_theme(
        theme='dark',
        corner_shape='rounded',
        custom_colors={
            "[dark]": {
                "primary": f"{PRIMARY_COLOR}"
            },
            "[light]": {
                "primary": f"{PRIMARY_COLOR}"
            },
        },
        additional_qss=qss
    )
