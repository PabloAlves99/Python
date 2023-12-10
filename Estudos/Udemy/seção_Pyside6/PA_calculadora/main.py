#  pylint: disable=missing-docstring
#  pylint: disable=no-name-in-module
#  type: ignore
import sys

from PySide6.QtWidgets import (QApplication, QWidget, QMainWindow, QVBoxLayout,
                               QLineEdit,)
from PySide6.QtGui import QIcon
from PySide6.QtCore import Qt
from variables import (WINDOW_ICON_PATH, BIG_FONT_SIZE, TEXT_MARGIN,
                       MINIMUM_WIDTH)


class Display(QLineEdit):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.config_style()

    def config_style(self):
        self.setStyleSheet(f'font-size: {BIG_FONT_SIZE}px;')
        self.setMinimumHeight(BIG_FONT_SIZE * 2)
        self.setMinimumWidth(MINIMUM_WIDTH)
        self.setAlignment(Qt.AlignmentFlag.AlignRight)
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
        self.setStyleSheet('background-color: #262626; color: #A6A6A6;')

        self.setWindowTitle('Pablo Alves - Calculator')


if __name__ == '__main__':
    # Cria a aplicação
    app = QApplication(sys.argv)
    window = MainWindow()

    # Cria o icone
    icon = QIcon(str(WINDOW_ICON_PATH))
    window.setWindowIcon(icon)
    app.setWindowIcon(icon)

    # Display
    display = Display()
    window.v_layout.addWidget(display)

    # Executa
    window.show()
    sys.exit(app.exec())
