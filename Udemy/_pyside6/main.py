# pylint: disable=all
import sys

from PySide6.QtWidgets import QApplication, QMainWindow
from _untitled import Ui_MainWindow


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)

        self.enviar.clicked.connect(self.changeLabelResult)  # type: ignore

    def changeLabelResult(self):
        text = self.lineEdit.text()
        self.label_result.setText(text)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    app.exec()
