#  pylint: disable=missing-docstring
#  pylint: disable=no-name-in-module
#  type: ignore
import sys
from PySide6.QtWidgets import (QApplication, QWidget, QMainWindow, QVBoxLayout,
                               QLineEdit, QLabel, QPushButton, QGridLayout)
from PySide6.QtGui import QIcon
from PySide6.QtCore import Qt

# Importa variáveis e estilos de arquivos externos
from variables import (WINDOW_ICON_PATH, BIG_FONT_SIZE, TEXT_MARGIN,
                       MINIMUM_WIDTH, SMALL_FONT_SIZE, MEDIUM_FONT_SIZE)
from styles import setup_theme


# Define uma classe para botões com estilos personalizados
class Button(QPushButton):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.button_style()

    def button_style(self):
        """
        Aplica estilos personalizados ao botão.
        """
        font = self.font()  # Obtém a fonte atual do botão

        # Define o tamanho do texto no botão
        font.setPixelSize(MEDIUM_FONT_SIZE)
        self.setFont(font)  # Aplica a fonte modificada ao botão
        self.setMinimumSize(60, 60)  # Define o tamanho mínimo do botão


class ButtonsGrid(QGridLayout):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

        self._grid_mask = [
            ['%', 'CE', 'C', '←'],
            ['7', '8', '9', 'x'],
            ['4', '5', '6', '-'],
            ['1', '2', '3', '+'],
            ['±', '0', ',', '='],
        ]
        self.create_buttons()

    def create_buttons(self):
        for i, row in enumerate(self._grid_mask):
            for j, text_grid in enumerate(row):
                _button = Button(text_grid)

                if text_grid == '=':
                    # Define a classe CSS para estilização externa
                    _button.setProperty("cssClass", "specialButton")

                self.addWidget(_button, i, j)


# Define uma classe para exibição de informações


class Info(QLabel):
    def __init__(self, parent: QWidget | None = None, *args, **kwargs) -> None:
        super().__init__(parent, *args, **kwargs)

    def config_style(self):
        # Define o tamanho da info e o alinhamento
        self.setStyleSheet(f'{SMALL_FONT_SIZE}px;')
        self.alignment(Qt.AlignmentFlag.AlignRight)


# Define uma classe para o visor (display)
class Display(QLineEdit):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.config_style()

    def config_style(self):
        """
        Aplica estilos personalizados ao "visor".
        """
        #  Define o tamanho da fonte do "visor"
        self.setStyleSheet(f'font-size: {BIG_FONT_SIZE}px;')

        # Define a altura mínima do "visor" com base no tamanho da fonte
        self.setMinimumHeight(BIG_FONT_SIZE * 2)

        # Define a largura mínima do "visor"
        self.setMinimumWidth(MINIMUM_WIDTH)

        # Alinha o texto no "visor" à direita
        self.setAlignment(Qt.AlignmentFlag.AlignRight)

        # Define as margens internas do "visor"
        self.setTextMargins(*[TEXT_MARGIN for _ in range(4)])


# Define a classe da janela principal da aplicação
class MainWindow(QMainWindow):
    def __init__(self, parent: QWidget | None = None, *args, **kwargs) -> None:
        super().__init__(parent, *args, **kwargs)

        # Configurando o layout básico
        self.cw = QWidget()  # Cria um widget para ser o central widget
        self.v_layout = QVBoxLayout()  # Cria um layout vertical

        # Define o layout principal do widget central
        self.cw.setLayout(self.v_layout)

        # Define o widget central da janela principal
        self.setCentralWidget(self.cw)

        # Defina o tamanho máximo da janela
        self.setMaximumSize(450, 500)

        # Define o titulo para a janela principal
        self.setWindowTitle('Pablo Alves - Calculator')


if __name__ == '__main__':
    # Cria a aplicação
    app = QApplication(sys.argv)

    # Definição do tema da aplicação
    setup_theme()

    # Cria uma instância da classe MainWindow (janela principal da aplicação)
    window = MainWindow()

    # Cria o icone
    icon = QIcon(str(WINDOW_ICON_PATH))  # Caminho do icone
    window.setWindowIcon(icon)  # Define o icone para a janela
    app.setWindowIcon(icon)  # Define o icone para a aplicação

    # Info
    info = Info()
    window.v_layout.addWidget(info)  # Adiciona a info na aplicação

    # Display
    display = Display()
    window.v_layout.addWidget(display)  # Adiciona o display na aplicação

    # Button Grid
    button_grid = ButtonsGrid()
    window.v_layout.addLayout(button_grid)
    # Executa a aplicação
    window.show()
    sys.exit(app.exec())
