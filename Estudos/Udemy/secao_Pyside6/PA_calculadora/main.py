#  pylint: disable=missing-docstring
#  pylint: disable=no-name-in-module
#  type: ignore
import sys
import button_function as bf
from PySide6.QtWidgets import (QApplication, QWidget, QMainWindow, QVBoxLayout,
                               QLineEdit, QLabel, QPushButton, QGridLayout)
from PySide6.QtGui import QIcon
from PySide6.QtCore import Qt, Slot

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


# Define uma classe para exibição de informações
class Info(QLabel):
    def __init__(self, parent: QWidget | None = None, *args, **kwargs) -> None:
        super().__init__(parent, *args, **kwargs)

        self.config_style_info()

    def config_style_info(self):
        # Define o tamanho da info e o alinhamento
        self.setStyleSheet(f'{SMALL_FONT_SIZE}px;')
        self.setAlignment(Qt.AlignmentFlag.AlignRight)


# Define uma classe para o visor (display)
class Display(QLineEdit):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.config_style_display()

    def config_style_display(self):
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


class ButtonsGrid(QGridLayout):
    def __init__(
            self, _display: Display, _info: Info, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

        self._grid_mask = [
            ['%', 'CE', 'C', '←'],
            ['½', '^', '√', '/'],
            ['7', '8', '9', '*'],
            ['4', '5', '6', '-'],
            ['1', '2', '3', '+'],
            ['±', '0', '.', '='],
        ]
        self.display = _display
        self.info = _info
        self._left = None
        self._right = None
        self._op = None
        self.setSpacing(3)
        self._equation = ''
        self.create_buttons()

    @property
    def equation(self):
        return self.equation

    @equation.setter
    def equation(self, value):
        self._equation = value
        self.info.setText(value)

    def create_buttons(self):
        for i, row in enumerate(self._grid_mask):
            for column, text_grid in enumerate(row):
                _button = Button(text_grid)

                if _button.text() == '=':
                    _button.setProperty("cssClass", "specialButton")

                if not bf.is_num_or_dot(text_grid):
                    self._config_special_button(_button)

                self.addWidget(_button, i, column)
                slot = self._make_slot(self.insert_text_display, _button)
                self._connect_button_clicked(_button, slot)

    def clear_display_and_info(self):
        self.display.clear()
        self.info.clear()
        self._op = None
        self._left = None
        self._right = None

    def _connect_button_clicked(self, button, slot):
        button.clicked.connect(slot)

    def _config_special_button(self, _button):
        text = _button.text()

        if text == 'C':
            _button.clicked.connect(self.clear_display_and_info)
        elif text == 'CE':
            _button.clicked.connect(self.display.clear)

        if text in '+-*/%½^√':
            self._connect_button_clicked(
                _button, self._make_slot(self._operator_clicked, _button))

    def _make_slot(self, func, *args, **kwargs):
        @Slot()
        def real_slot():
            func(*args, **kwargs)
        return real_slot

    def insert_text_display(self, _button):
        text = _button.text()
        new_display_text = self.display.text() + text

        if not bf.is_valid_number(new_display_text):
            return

        self.display.insert(text)

    def _define_info(self):
        self._left = float(self.display.text())
        self.info.setText(str(self._left))

    def _define_operator(self, text):
        self._op = text
        print(f'Oeração = {text}')

    def calculate(self):
        if self._left is not None:
            if self._op == '+':
                self._left = float(self._left) + float(self.display.text())
            if self._op == '-':
                self._left = float(self._left) - float(self.display.text())
            if self._op == '*':
                self._left = float(self._left) * float(self.display.text())
            if self._op == '/':
                self._left = float(self._left) / float(self.display.text())
            self.info.setText(str(self._left))

    def _operator_clicked(self, _button):
        text = _button.text()
        current_display_text = self.display.text().strip()

        if self._left is None and current_display_text:
            self._define_info()
        elif current_display_text:
            self.calculate()

        self._define_operator(text)
        self.display.clear()


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
        self.setFixedSize(418, 500)

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
    info = Info('Sua conta')
    window.v_layout.addWidget(info)  # Adiciona a info na aplicação

    # Display
    display = Display()
    window.v_layout.addWidget(display)  # Adiciona o display na aplicação

    # Button Grid
    button_grid = ButtonsGrid(display, info)
    window.v_layout.addLayout(button_grid)

    # Executa a aplicação
    window.show()
    sys.exit(app.exec())
