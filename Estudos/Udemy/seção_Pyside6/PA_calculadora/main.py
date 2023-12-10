#  pylint: disable=missing-docstring
#  pylint: disable=no-name-in-module
#  type: ignore
import sys
from PySide6.QtWidgets import (QApplication, QWidget, QMainWindow, QVBoxLayout,
                               QLineEdit, QLabel, QPushButton)
from PySide6.QtGui import QIcon
from PySide6.QtCore import Qt
from variables import (WINDOW_ICON_PATH, BIG_FONT_SIZE, TEXT_MARGIN,
                       MINIMUM_WIDTH, SMALL_FONT_SIZE, MEDIUM_FONT_SIZE)
from styles import setup_theme


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
        self.setMinimumSize(75, 75)  # Define o tamanho mínimo do botão

        # Define a classe CSS para estilização externa
        self.setProperty("cssClass", "specialButton")


class Info(QLabel):
    def __init__(self, parent: QWidget | None = None, *args, **kwargs) -> None:
        super().__init__(parent, *args, **kwargs)

    def config_style(self):
        # Define o tamanho da info e o alinhamento
        self.setStyleSheet(f'{SMALL_FONT_SIZE}px;')
        self.alignment(Qt.AlignmentFlag.AlignRight)


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


class MainWindow(QMainWindow):
    def __init__(self, parent: QWidget | None = None, *args, **kwargs) -> None:
        super().__init__(parent, *args, **kwargs)

        # Configurando o layout básico
        self.cw = QWidget()
        self.v_layout = QVBoxLayout()
        self.cw.setLayout(self.v_layout)
        self.setCentralWidget(self.cw)
        self.resize(400, 550)

        self.setWindowTitle('Pablo Alves - Calculator')


if __name__ == '__main__':
    # Cria a aplicação

    # Cria uma instância da aplicação com argumentos do sistema
    app = QApplication(sys.argv)

    # Definição do tema da aplicação
    setup_theme()

    # Cria uma instância da classe MainWindow (janela principal da aplicação)
    window = MainWindow()

    # Cria o icone
    icon = QIcon(str(WINDOW_ICON_PATH))
    window.setWindowIcon(icon)
    app.setWindowIcon(icon)

    # Info
    info = Info()
    window.v_layout.addWidget(info)

    # Display
    display = Display()
    window.v_layout.addWidget(display)

    # button
    button = Button('Texto')
    window.v_layout.addWidget(button)

    # Executa
    window.show()
    sys.exit(app.exec())
