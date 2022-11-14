import PySide2.QtWidgets as QtWidgets
import subprocess
from PySide2 import QtCore
from mysql.connector import MySQLConnection
import mysql

################################################################################
## Form generated from reading UI file 'reg-teljrxEbYs.ui'
##
## Created by: Qt User Interface Compiler version 5.14.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
                            QRect, QSize, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
                           QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
                           QRadialGradient)
from PySide2.QtWidgets import *

import logo_rc

import userInfo
from functions import Message, Connection
import opener



class Reg_MainWindow(object):

    def setupUi(self, MainWindow):
        if MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        self.window = MainWindow
        self.window.setWindowIcon(QIcon('globe_world_earth_planets_chool_icon_209251.png'))
        MainWindow.resize(932, 520)

        # MainWindow.resize(1118.4, 852)
        MainWindow.setStyleSheet(u"background-color: rgb(210, 210, 210);\n"
                                 "")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.headerF = QFrame(self.centralwidget)
        self.headerF.setObjectName(u"headerF")
        self.headerF.setMaximumSize(QSize(16777215, 200))
        self.headerF.setStyleSheet(u"")
        self.headerF.setFrameShape(QFrame.StyledPanel)
        self.headerF.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.headerF)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.textL = QLabel(self.headerF)
        self.textL.setObjectName(u"textL")
        self.textL.setStyleSheet(u"font: 75 40pt \"Consolas\";\n"
                                 "text-decoration: underline;\n"
                                 "")

        self.horizontalLayout.addWidget(self.textL)

        self.logoL = QLabel(self.headerF)
        self.logoL.setObjectName(u"logoL")
        self.logoL.setMaximumSize(QSize(288, 132))
        self.logoL.setStyleSheet(u"border-image: url(:/logo/logo.png);")

        self.horizontalLayout.addWidget(self.logoL)

        self.verticalLayout.addWidget(self.headerF)

        self.bodyF = QFrame(self.centralwidget)
        self.bodyF.setObjectName(u"bodyF")
        self.bodyF.setStyleSheet(
            u"background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.506, stop:0 rgba(255, 255, 0, 255), stop:1 rgba(210, 210, 210, 210));")
        self.bodyF.setFrameShape(QFrame.StyledPanel)
        self.bodyF.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.bodyF)
        self.gridLayout.setObjectName(u"gridLayout")
        self.nameL = QLabel(self.bodyF)
        self.nameL.setObjectName(u"nameL")
        self.nameL.setMinimumSize(QSize(80, 30))
        self.nameL.setMaximumSize(QSize(50, 16777215))
        self.nameL.setStyleSheet(u"font: 75 26px \"MS Shell Dlg 2\";\n"
                                 "background-color: rgb(210,  210, 210);")

        self.gridLayout.addWidget(self.nameL, 1, 1, 1, 1)

        self.passwLE = QLineEdit(self.bodyF)
        self.passwLE.setObjectName(u"passwLE")
        self.passwLE.setMaximumSize(QSize(16777215, 16777215))
        self.passwLE.setStyleSheet(u"font: 26px \"MS Shell Dlg 2\";\n"
                                   "background-color: rgb(255, 255, 255);")
        self.passwLE.setEchoMode(QLineEdit.Password)

        self.gridLayout.addWidget(self.passwLE, 3, 2, 1, 1)

        self.nameLE = QLineEdit(self.bodyF)
        self.nameLE.setObjectName(u"nameLE")
        self.nameLE.setMaximumSize(QSize(16777215, 16777215))
        self.nameLE.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
                                  "font: 26px \"MS Shell Dlg 2\";")

        self.gridLayout.addWidget(self.nameLE, 1, 2, 1, 1)

        self.backPB = QPushButton(self.bodyF)
        self.backPB.setObjectName(u"backPB")
        self.backPB.setStyleSheet(u"font: 75 26px \"MS Shell Dlg 2\";\n"
                                  "background-color: rgb(255, 255, 0);")

        self.gridLayout.addWidget(self.backPB, 0, 1, 1, 1)

        self.ageSB = QSpinBox(self.bodyF)
        self.ageSB.setObjectName(u"ageSB")
        self.ageSB.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
                                 "font: 26px \"MS Shell Dlg 2\";")

        self.gridLayout.addWidget(self.ageSB, 2, 2, 1, 1)

        self.ageL = QLabel(self.bodyF)
        self.ageL.setObjectName(u"ageL")
        self.ageL.setMinimumSize(QSize(80, 30))
        self.ageL.setMaximumSize(QSize(16777215, 16777215))
        self.ageL.setStyleSheet(u"font: 75 26px \"MS Shell Dlg 2\";\n"
                                "background-color: rgb(210, 210, 210);")

        self.gridLayout.addWidget(self.ageL, 2, 1, 1, 1)

        self.pswaL = QLabel(self.bodyF)
        self.pswaL.setObjectName(u"pswaL")
        self.pswaL.setStyleSheet(u"font: 75 26px \"MS Shell Dlg 2\";\n"
                                 "background-color: rgb(210, 210, 210);")

        self.gridLayout.addWidget(self.pswaL, 4, 1, 1, 1)

        self.pswaLE = QLineEdit(self.bodyF)
        self.pswaLE.setObjectName(u"pswaLE")
        self.pswaLE.setStyleSheet(u"font: 26px \"MS Shell Dlg 2\";\n"
                                  "background-color: rgb(255, 255, 255);")
        self.pswaLE.setEchoMode(QLineEdit.Password)

        self.gridLayout.addWidget(self.pswaLE, 4, 2, 1, 1)

        self.passwL = QLabel(self.bodyF)
        self.passwL.setObjectName(u"passwL")
        self.passwL.setMinimumSize(QSize(80, 30))
        self.passwL.setMaximumSize(QSize(50, 16777215))
        self.passwL.setStyleSheet(u"font: 75 26px \"MS Shell Dlg 2\";\n"
                                  "background-color: rgb(210, 210, 210);")

        self.gridLayout.addWidget(self.passwL, 3, 1, 1, 1)

        self.verticalLayout.addWidget(self.bodyF)

        self.regPB = QPushButton(self.centralwidget)
        self.regPB.setObjectName(u"regPB")
        self.regPB.setMaximumSize(QSize(16777215, 50))
        self.regPB.setStyleSheet(u"font: 75 26px \"MS Shell Dlg 2\";\n"
                                 "background-color: rgb(255, 255, 0);")

        self.verticalLayout.addWidget(self.regPB)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 932, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)

    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"VilágBajnok - Regisztráció", None))
        self.textL.setText(QCoreApplication.translate("MainWindow", u"Vil\u00e1gBajnok", None))
        self.logoL.setText("")
        self.nameL.setText(QCoreApplication.translate("MainWindow", u"N\u00e9v:", None))
        self.ageL.setText(QCoreApplication.translate("MainWindow", u"\u00c9letkor:", None))
        self.pswaL.setText(QCoreApplication.translate("MainWindow", u"Jelsz\u00f3 \u00fajra:", None))
        self.backPB.setText("⇦ Vissza")
        self.passwLE.setPlaceholderText(QCoreApplication.translate("MainWindow", u"legalább 5 karakter", None))
        self.passwL.setText(QCoreApplication.translate("MainWindow", u"Jelsz\u00f3:", None))
        self.regPB.setText(QCoreApplication.translate("MainWindow", u"Regisztr\u00e1ci\u00f3", None))
        # retranslateUi
        self.regPB.clicked.connect(self.RegData)
        self.backPB.clicked.connect(self.BackOpenWindow)
        # self.backPB.clicked.connect(MainWindow.close)

    def BackOpenWindow(self):
        self.window.close()
        self.window = QtWidgets.QMainWindow()
        self.ui = opener.HomePage_MainWindow()
        self.ui.setupUi(self.window)
        self.window.show()

    def RegData(self):

        if len(self.nameLE.text()) == 0 or int(self.ageSB.text()) <= 0 or len(self.passwLE.text()) < 5 or (
                self.passwLE.text() != self.pswaLE.text()):
            Message("HIBAÜZENET","Hiba! A kitöltés nem volt megfelelő, kérlek nézd át mindent megadtál-e megfelelően és próbáld újra!")
            self.regPB.setEnabled(True)
        else:
            con, cur = Connection()
            if con is None:
                Message("HIBAÜZENET", "Adatbázis kapcsolati hiba! Ellenőrizd az internetelérésed!")
                self.regPB.setEnabled(True)
            else:
                try:
                    add = "insert into regisztraciok (nev,kor,jelszo) values (%s,%s,%s)"
                    cur.execute(add, (self.nameLE.text(), self.ageSB.text(), self.passwLE.text()))
                    con.commit()
                    con.close()

                except:
                    Message("HIBAÜZENET", "Hiba! Ez a felhasználónév már foglalt!")
                    self.regPB.setEnabled(True)

                else:
                    self.open_window()


    def open_window(self):
        self.window.close()
        self.window = QtWidgets.QMainWindow()
        name = self.nameLE.text()
        self.ui = userInfo.Quest_MainWindow(name)
        self.ui.setupUi(self.window)
        self.window.show()


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Reg_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
