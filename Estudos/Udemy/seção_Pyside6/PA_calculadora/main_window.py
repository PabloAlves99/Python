#  pylint: disable=missing-docstring
#  pylint: disable=no-name-in-module
#  type: ignore
from PySide6.QtWidgets import QWidget, QMainWindow, QVBoxLayout


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
