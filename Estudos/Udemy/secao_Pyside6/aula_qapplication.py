# QApplication e QPushButton de PySide6.QtWidgets
# QApplication -> O Widget principal da aplicação
# QPushButton -> Um botão
# PySide6.QtWidgets -> Onde estão os widgets do PySide6
# QMainWindow e centralWidget
# -> QApplication (app)
#   -> QMainWindow (window->setCentralWidget)
#       -> CentralWidget (central_widget)
#           -> Layout (layout)
#               -> Widget 1 (botao1)
#               -> Widget 2 (botao2)
#               -> Widget 3 (botao3)
#   -> show
# -> exec
import sys

from PySide6.QtWidgets import (QApplication, QPushButton, QWidget, QVBoxLayout,
                               QMainWindow)

app = QApplication(sys.argv)
window = QMainWindow()
central_widget = QWidget()
window.setCentralWidget(central_widget)

botao = QPushButton('Texto do botão')
botao.setStyleSheet('font-size: 40px; color:red;')

botao2 = QPushButton('Texto do botão')
botao2.setStyleSheet('font-size: 80px; color:blue;')


layout = QVBoxLayout()
central_widget.setLayout(layout)
layout.addWidget(botao)
layout.addWidget(botao2)


def mudar_background(_status_bar):  # pylint: disable=missing-docstring
    _status_bar.showMessage('O meu slot foi executado')
    botao.setStyleSheet('font-size: 40px; background-color:red;')
    botao2.setStyleSheet('font-size: 80px; background-color:blue;')


def voltar_background(_status_bar):  # pylint: disable=missing-docstring
    _status_bar.showMessage('O meu slot foi executado')
    botao.setStyleSheet('font-size: 40px; color:red;')
    botao2.setStyleSheet('font-size: 80px; color:blue;')


# StatusBar
status_bar = window.statusBar()
status_bar.showMessage('Mensagem na barra')

menu = window.menuBar()
primeiro_menu = menu.addMenu('Menu')
primeira_acao = primeiro_menu.addAction('Mudar Background')
segunda_acao = primeiro_menu.addAction('Voltar Background')
primeira_acao.triggered.connect(  # type:ignore
    lambda: mudar_background(status_bar)
)
segunda_acao.triggered.connect(  # type:ignore
    lambda: voltar_background(status_bar)
)

window.show()
app.exec()
