#  pylint: disable=missing-docstring
#  pylint: disable=no-name-in-module
#  type: ignore
import sys
import re
import button_function as bf
from PySide6.QtWidgets import (QApplication, QWidget, QMainWindow, QVBoxLayout,
                               QLineEdit, QLabel, QPushButton, QMessageBox)
from PySide6.QtGui import QIcon, QKeyEvent
from PySide6.QtCore import Qt, Signal

# Importa variáveis e estilos de arquivos externos
from variables import (WINDOW_ICON_PATH, BIG_FONT_SIZE, TEXT_MARGIN,
                       MINIMUM_WIDTH, SMALL_FONT_SIZE, MEDIUM_FONT_SIZE)
from styles import setup_theme

NUM_OR_DOT_REGEX = re.compile(r'^[0-9.]$')
# Define uma classe para botões com estilos personalizados


class Button(QPushButton):
    """
    Classe para os botões.

    Métodos:
    - __init__: Inicializa o botão.
    - button_style: Aplica estilos personalizados ao botão.
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.button_style()

    def button_style(self):
        """Aplica estilos personalizados ao botão."""

        font = self.font()  # Obtém a fonte atual do botão

        # Define o tamanho do texto no botão
        font.setPixelSize(MEDIUM_FONT_SIZE)
        self.setFont(font)  # Aplica a fonte modificada ao botão
        self.setMinimumSize(60, 60)  # Define o tamanho mínimo do botão


# Define uma classe para exibição de informações
class Info(QLabel):
    """
    Classe para exibição de informações.

    Métodos:
    - __init__: Inicializa a exibição de informações.
    - config_style_info: Configura o estilo da informação.
    """

    def __init__(self, parent: QWidget | None = None) -> None:
        super().__init__(parent)

        self.config_style_info()

    def config_style_info(self):
        """Configura o estilo da info."""

        # Define o tamanho da info e o alinhamento
        self.setStyleSheet(f'font-size: {SMALL_FONT_SIZE}px;')
        self.setAlignment(Qt.AlignmentFlag.AlignRight)


# Define uma classe para o visor (display)
class Display(QLineEdit):
    """
    Visor (display) da calculadora.

    Sinais:
    - eq_pressed: Emitido quando a tecla = ou Enter é pressionada.
    - del_pressed: Emitido quando a tecla delete ou backspace é pressionada.
    - clear_pressed: Emitido quando a tecla C ou ESC é pressionada.
    - input_pressed: Emitido quando um dígito numérico ou ponto é inserido.
    - operator_pressed: Emitido quando um operador é pressionado.

    Métodos:
    - __init__: Inicializa o visor.
    - config_style_display: Aplica estilos personalizados.
    - keyPressEvent: Manipula eventos de tecla.

    Atributos:
    - eq_pressed: Sinal para tecla = ou Enter.
    - del_pressed: Sinal para tecla delete ou backspace.
    - clear_pressed: Sinal para tecla C ou ESC.
    - input_pressed: Sinal para dígitos numéricos ou ponto.
    - operator_pressed: Sinal para operadores.
    """
    # Define sinais personalizados para eventos específicos
    eq_pressed = Signal()
    del_pressed = Signal()
    clear_pressed = Signal()
    input_pressed = Signal(str)
    operator_pressed = Signal(str)

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

    def keyPressEvent(self, event: QKeyEvent) -> None:
        """
        Manipula eventos de pressionamento de tecla.

        Args:
            event (QKeyEvent): O evento de pressionamento de tecla.
        """
        text = event.text().strip()
        key = event.key()
        keys = Qt.Key

        # Verifica se a tecla específica foi pressionada
        is_enter = key in [keys.Key_Enter, keys.Key_Return]
        is_delet = key in [keys.Key_Backspace, keys.Key_Delete]
        is_esc = key in [keys.Key_Escape, keys.Key_C]
        is_operator = key in [
            keys.Key_Plus, keys.Key_Minus, keys.Key_Slash, keys.Key_Asterisk,
            keys.Key_P,
        ]

        # Emite o sinal correspondente ao evento
        if is_enter or text == '=':
            self.eq_pressed.emit()
            return event.ignore()

        if is_delet:
            self.del_pressed.emit()
            return event.ignore()

        if is_esc:
            self.clear_pressed.emit()
            return event.ignore()

        if is_operator:

            if text.lower() == 'p':
                text = '^'
            # Emite o sinal correspondente ao operador
            self.operator_pressed.emit(text)
            return event.ignore()

        # Não passar daqui se não tiver texto
        if self.is_empty(text):
            return event.ignore()

        # Emite o sinal correspondente à entrada de texto numérico ou ponto
        if self.is_num_or_dot(text):
            self.input_pressed.emit(text)
            return event.ignore()

    def is_empty(self, string: str):
        """Verifica se uma string está vazia."""
        return len(string) == 0

    def is_num_or_dot(self, string: str):
        """Verifica se uma string contém um número ou ponto."""
        return bool(NUM_OR_DOT_REGEX.search(string))


# Define a classe da janela principal da aplicação
class MainWindow(QMainWindow):
    """
    Janela principal da calculadora.

    Métodos:
    - __init__: Inicializa a janela principal.
    - make_msg_box: Cria e retorna uma instância de QMessageBox.

    Atributos:
    - cw: Widget central da janela.
    - v_layout: Layout vertical do widget central.
    """

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

    def make_msg_box(self):
        """Retorna uma instância de QMessageBox."""
        return QMessageBox(self)


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
    button_grid = bf.ButtonsGrid(display, info, window)
    window.v_layout.addLayout(button_grid)

    # Executa a aplicação
    window.show()
    sys.exit(app.exec())
