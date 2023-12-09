# QApplication e QPushButton de PySide6.QtWidgets
# QApplication -> O Widget principal da aplicação
# QPushButton -> Um botão
# PySide6.QtWidgets -> Onde estão os widgets do PySide6

import sys

from PySide6.QtWidgets import QApplication, QPushButton

app = QApplication(sys.argv)

botao = QPushButton('Testo do botão')
botao.setStyleSheet('font-size: 40px;')
botao.show()

botao = QPushButton('Testo do botão')

app.exec()
