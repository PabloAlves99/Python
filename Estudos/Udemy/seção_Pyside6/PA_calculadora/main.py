#  pylint: disable=missing-docstring
#  pylint: disable=no-name-in-module
#  type: ignore
import sys

from main_window import MainWindow
from display import Display
from PySide6.QtWidgets import QApplication
from PySide6.QtGui import QIcon
from variables import WINDOW_ICON_PATH

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
