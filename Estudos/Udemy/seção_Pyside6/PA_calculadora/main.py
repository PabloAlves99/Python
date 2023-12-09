#  pylint: disable=missing-docstring
#  pylint: disable=no-name-in-module
#  type: ignore
import sys
from PySide6.QtWidgets import QWidget, QApplication


class Calculator(QWidget):
    def __init__(self):
        super().__init__()


if __name__ == '__main__':
    app = QApplication()
    widget = Calculator()
    widget.resize(400, 200)
    widget.show()

    sys.exit(app.exec())
