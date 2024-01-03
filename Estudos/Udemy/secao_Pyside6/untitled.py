# pylint: disable=all

# -*- coding: utf-8 -*-

###############################################################################
# Form generated from reading UI file 'untitled.ui'
##
# Created by: Qt User Interface Compiler version 6.6.1
##
# WARNING! All changes made in this file will be lost when recompiling UI file!
###############################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
                            QMetaObject, QObject, QPoint, QRect,
                            QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
                           QFont, QFontDatabase, QGradient, QIcon,
                           QImage, QKeySequence, QLinearGradient, QPainter,
                           QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QGridLayout, QHBoxLayout, QLabel,
                               QLineEdit, QMainWindow, QMenuBar, QPushButton,
                               QSizePolicy, QStatusBar, QWidget)


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(660, 440)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_result = QLabel(self.centralwidget)
        self.label_result.setObjectName(u"label_result")
        font = QFont()
        font.setPointSize(23)
        font.setBold(True)
        font.setItalic(True)
        font.setUnderline(False)
        font.setStrikeOut(False)
        font.setKerning(False)
        self.label_result.setFont(font)
        self.label_result.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_result, 0, 0, 1, 1)

        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.label_name = QLabel(self.centralwidget)
        self.label_name.setObjectName(u"label_name")
        font1 = QFont()
        font1.setPointSize(30)
        font1.setBold(True)
        font1.setItalic(True)
        self.label_name.setFont(font1)

        self.gridLayout_2.addWidget(self.label_name, 1, 0, 1, 1)

        self.lineEdit = QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName(u"lineEdit")
        font2 = QFont()
        font2.setPointSize(30)
        font2.setBold(False)
        font2.setItalic(False)
        self.lineEdit.setFont(font2)

        self.gridLayout_2.addWidget(self.lineEdit, 1, 1, 1, 1)

        self.enviar = QPushButton(self.centralwidget)
        self.enviar.setObjectName(u"enviar")
        font3 = QFont()
        font3.setPointSize(20)
        self.enviar.setFont(font3)

        self.gridLayout_2.addWidget(self.enviar, 1, 2, 1, 1)

        self.gridLayout.addLayout(self.gridLayout_2, 1, 0, 1, 1)

        self.horizontalLayout.addLayout(self.gridLayout)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 660, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate(
            "MainWindow", u"MainWindow", None))
        self.label_result.setText(QCoreApplication.translate(
            "MainWindow", u"N\u00e3o tem nada aqui", None))
        self.label_name.setText(QCoreApplication.translate(
            "MainWindow", u"Seu nome:", None))
        self.lineEdit.setPlaceholderText(QCoreApplication.translate(
            "MainWindow", u"Digite seu nome", None))
        self.enviar.setText(QCoreApplication.translate(
            "MainWindow", u"Enviar", None))
    # retranslateUi
