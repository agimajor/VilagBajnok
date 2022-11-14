
import PySide2.QtWidgets as QtWidgets
import psycopg2
# -*- coding: utf-8 -*-
from mysql.connector import MySQLConnection
import mysql
import random
import sys
################################################################################
## Form generated from reading UI file 'kontinensekhbkAZr.ui'
##
## Created by: Qt User Interface Compiler version 5.14.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################
from PySide2 import QtCore
from PySide2.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient)
from PySide2.QtWidgets import *
from questions import Quiz_MainWindow
from opener import HomePage_MainWindow

import kontinens_rc
import subprocess
from functions import Message, Connection, clearStr

class Continents_MainWindow(object):
    def __init__(self, name):
        self.name = name


    def setupUi(self, MainWindow):
        #MainWindow.setWindowFlags(QtCore.Qt.WindowCloseButtonHint | QtCore.Qt.WindowMinimizeButtonHint)
        MainWindow.setWindowFlag(QtCore.Qt.WindowCloseButtonHint, False)
        if MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        self.window = MainWindow
        self.window.setWindowIcon(QIcon('globe_world_earth_planets_chool_icon_209251.png'))
        MainWindow.resize(932, 520)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QSize(932, 520))
        MainWindow.setMaximumSize(QSize(932, 520))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(0, 0, 932, 520))
        sizePolicy.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy)
        self.hatterL = QLabel(self.widget)
        self.hatterL.setObjectName(u"hatterL")
        self.hatterL.setGeometry(QRect(0, 0, 932, 500))
        self.hatterL.setStyleSheet(u"border-image: url(:/kontinens/kontinens_szurke.png);")
        self.filterL = QLabel(self.widget)
        self.filterL.setObjectName(u"filterL")
        self.filterL.setGeometry(QRect(0, 0, 932, 520))
        self.filterL.setStyleSheet(
            u"background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0 rgba(0, 0, 0, 0));")
        self.eaPB = QPushButton(self.widget)
        self.eaPB.setObjectName(u"eaPB")
        self.eaPB.setGeometry(QRect(135, 90, 131, 41))
        self.eaPB.setStyleSheet(u"font: 18px \"MS Shell Dlg 2\";")
        self.daPB = QPushButton(self.widget)
        self.daPB.setObjectName(u"daPB")
        self.daPB.setGeometry(QRect(240, 280, 131, 51))
        self.daPB.setStyleSheet(u"font: 18px \"MS Shell Dlg 2\";")
        self.euPB = QPushButton(self.widget)
        self.euPB.setObjectName(u"euPB")
        self.euPB.setGeometry(QRect(470, 70, 81, 41))
        self.euPB.setStyleSheet(u"font: 18px \"MS Shell Dlg 2\";")
        self.afPB = QPushButton(self.widget)
        self.afPB.setObjectName(u"afPB")
        self.afPB.setGeometry(QRect(480, 220, 71, 41))
        self.afPB.setStyleSheet(u"font: 18px \"MS Shell Dlg 2\";")
        self.azsPB = QPushButton(self.widget)
        self.azsPB.setObjectName(u"azsPB")
        self.azsPB.setGeometry(QRect(645, 80, 81, 41))
        self.azsPB.setStyleSheet(u"font: 18px \"MS Shell Dlg 2\";")
        self.auPB = QPushButton(self.widget)
        self.auPB.setObjectName(u"auPB")
        self.auPB.setGeometry(QRect(750, 310, 91, 41))
        self.auPB.setStyleSheet(u"font: 18px \"MS Shell Dlg 2\";")
        self.ankPB = QPushButton(self.widget)
        self.ankPB.setObjectName(u"ankPB")
        self.ankPB.setGeometry(QRect(480, 430, 111, 51))
        self.ankPB.setStyleSheet(u"font: 18px \"MS Shell Dlg 2\";")
        self.eaL = QLabel(self.widget)
        self.eaL.setObjectName(u"eaL")
        self.eaL.setGeometry(QRect(140, 30, 61, 51))
        self.eaL.setStyleSheet(u"font: 75 26px \"Consolas\";")
        self.daL = QLabel(self.widget)
        self.daL.setObjectName(u"daL")
        self.daL.setGeometry(QRect(260, 220, 61, 51))
        self.daL.setStyleSheet(u"font: 75 26px \"Consolas\";")
        self.afL = QLabel(self.widget)
        self.afL.setObjectName(u"afL")
        self.afL.setGeometry(QRect(470, 160, 61, 51))
        self.afL.setStyleSheet(u"font: 75 26px \"Consolas\";")
        self.euL = QLabel(self.widget)
        self.euL.setObjectName(u"euL")
        self.euL.setGeometry(QRect(490, 20, 61, 51))
        self.euL.setStyleSheet(u"font: 75 26px \"Consolas\";")
        self.azsL = QLabel(self.widget)
        self.azsL.setObjectName(u"azsL")
        self.azsL.setGeometry(QRect(660, 30, 61, 51))
        self.azsL.setStyleSheet(u"font: 75 26px \"Consolas\";")
        self.auL = QLabel(self.widget)
        self.auL.setObjectName(u"auL")
        self.auL.setGeometry(QRect(760, 260, 61, 51))
        self.auL.setStyleSheet(u"font: 75 26px \"Consolas\";")
        self.ankL = QLabel(self.widget)
        self.ankL.setObjectName(u"ankL")
        self.ankL.setGeometry(QRect(680, 420, 61, 51))
        self.ankL.setStyleSheet(u"font: 75 26px \"Consolas\";")
        self.logoutPB = QPushButton(self.widget)
        self.logoutPB.setObjectName(u"logoutPB")
        self.logoutPB.setGeometry(QRect(840, 0, 91, 31))
        self.logoutPB.setStyleSheet(u"font: 14px \"MS Shell Dlg 2\";")
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
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"VilágBajnok - Válassz Kontinenst!", None))
        #self.bgL.setText("")
        self.filterL.setText("")
        self.eaPB.setText(QCoreApplication.translate("MainWindow", u"\u00c9szak-Amerika", None))
        self.daPB.setText(QCoreApplication.translate("MainWindow", u"D\u00e9l-Amerika ", None))
        self.euPB.setText(QCoreApplication.translate("MainWindow", u"Eur\u00f3pa", None))
        self.afPB.setText(QCoreApplication.translate("MainWindow", u"Afrika", None))
        self.azsPB.setText(QCoreApplication.translate("MainWindow", u"\u00c1zsia", None))
        self.auPB.setText(QCoreApplication.translate("MainWindow", u"Ausztr\u00e1lia", None))
        self.ankPB.setText(QCoreApplication.translate("MainWindow", u"Anktartisz", None))
        self.logoutPB.setText(QCoreApplication.translate("MainWindow", u"Kijelentkez\u00e9s", None))

        self.Start()
        self.eaPB.clicked.connect(self.eaContinent)
        #self.eaPB.clicked.connect(MainWindow.close)
        self.daPB.clicked.connect(self.daContinent)
        #self.daPB.clicked.connect(MainWindow.close)
        self.ankPB.clicked.connect(self.ankContinent)
        #self.ankPB.clicked.connect(MainWindow.close)
        self.euPB.clicked.connect(self.euContinent)
        #self.euPB.clicked.connect(MainWindow.close)
        self.afPB.clicked.connect(self.afContinent)
        #self.afPB.clicked.connect(MainWindow.close)
        self.azsPB.clicked.connect(self.azsContinent)
        #self.azsPB.clicked.connect(MainWindow.close)
        self.auPB.clicked.connect(self.auContinent)
        #self.auPB.clicked.connect(MainWindow.close)
        self.logoutPB.clicked.connect(self.Logout)
        #self.logoutPB.clicked.connect(MainWindow.close)

    def Start(self):
        con, cur = Connection()
        if con is None:
            Message("HIBAÜZENET", "Adatbázis kapcsolati hiba! Ellenőrizd az internetelérésed!")
        else:
            continents = 'select kontinens from eredmeny where nev =\'' + self.name + "\'"
            cur.execute(continents)
            con_res = cur.fetchall()
            con_res = clearStr(str(con_res))
            if len(con_res) > 0:
                con_list = []
                con_list.append(con_res.split(' '))
                con_diff = list(set(con_list[0]))

                for i in range(len(con_diff)):
                    cont = con_diff[i]
                    #points = f'select pont from eredmeny where kontinens ={cont} and nev = {self.name}'
                    points = "select pont from eredmeny where nev = %s and kontinens = %s"
                    cur.execute(points, (self.name, cont))
                    point_res = cur.fetchall()
                    point_res = clearStr(str(point_res))
                    point_list = []
                    point_list.append(point_res.split(' '))
                    point_diff = list(set(point_list[0]))
                    best = 0

                    if len(point_diff) > 0:
                        for idx in range(len(point_diff)):
                            p = point_diff[idx]
                            if int(p) > best:
                                best = int(p)

                        if cont == "afrika":
                            if best >= 8:
                                self.afL.setText("🚩")
                            else:
                                self.afL.setText("👣")

                        elif cont == "europa":
                            if best >= 8:
                                self.euL.setText("🚩")
                            else:
                                self.euL.setText("👣")

                        elif cont == "ausztralia":
                            if best >= 8:
                                self.auL.setText("🚩")
                            else:
                                self.auL.setText("👣")

                        elif cont == "azsia":
                            if best >= 8:
                                self.azsL.setText("🚩")
                            else:
                                self.azsL.setText("👣")

                        elif cont == "antarktisz":
                            if best >= 8:
                                self.ankL.setText("🚩")
                            else:
                                self.ankL.setText("👣")

                        elif cont == "eszak-amerika":
                            if best >= 8:
                                self.eaL.setText("🚩")
                            else:
                                self.eaL.setText("👣")

                        elif cont == "del-amerika":
                            if best >= 8:
                                self.daL.setText("🚩")
                            else:
                                self.daL.setText("👣")


    # retranslateUi
    def Logout(self):
        self.window.close()
        self.sleepButtons()
        self.window = QtWidgets.QMainWindow()
        self.ui = HomePage_MainWindow()
        self.ui.setupUi(self.window)
        self.window.show()

    def sleepButtons(self):
        self.eaPB.setEnabled(False)
        self.daPB.setEnabled(False)
        self.ankPB.setEnabled(False)
        self.euPB.setEnabled(False)
        self.afPB.setEnabled(False)
        self.azsPB.setEnabled(False)
        self.auPB.setEnabled(False)

    def activeButtons(self):
        self.eaPB.setEnabled(True)
        self.daPB.setEnabled(True)
        self.ankPB.setEnabled(True)
        self.euPB.setEnabled(True)
        self.afPB.setEnabled(True)
        self.azsPB.setEnabled(True)
        self.auPB.setEnabled(True)

    def eaContinent(self):
        self.sleepButtons()
        self.chooseContinent("eszak-amerika")
        #MainWindow.close()


    def daContinent(self):
        self.sleepButtons()
        self.chooseContinent("del-amerika")
        #MainWindow.close()


    def ankContinent(self):
        self.sleepButtons()
        self.chooseContinent("antarktisz")
        #MainWindow.close()


    def euContinent(self):
        self.sleepButtons()
        self.chooseContinent("europa")
        #MainWindow.close()


    def afContinent(self):
        self.sleepButtons()
        self.chooseContinent("afrika")
        #MainWindow.close()


    def azsContinent(self):
        self.sleepButtons()
        self.chooseContinent("azsia")
        #MainWindow.close()


    def auContinent(self):
        self.sleepButtons()
        self.chooseContinent("ausztralia")
        #MainWindow.close()


    def chooseContinent(self, continent):

        con, cur = Connection()
        if con is None:
            Message("HIBAÜZENET", "Adatbázis kapcsolati hiba! Ellenőrizd az internetelérésed!")
            self.activeButtons()
        else:
            self.window.close()
            name = self.name
            point = 0
            serial_number = 0
            self.window = QtWidgets.QMainWindow()
            self.ui = Quiz_MainWindow(continent, name, point, serial_number)
            self.ui.setupUi(self.window)
            self.window.show()



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Continents_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
