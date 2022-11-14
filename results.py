
import PySide2.QtWidgets as QtWidgets
# -*- coding: utf-8 -*-
from mysql.connector import MySQLConnection
import mysql
import random
import psycopg2
################################################################################
## Form generated from reading UI file 'eredmeny-teljflOadC.ui'
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
#from PyQt5.QtWidgets import QWidget,QPushButton,QApplication,QListWidget,QGridLayout,QLabel
from PySide2.QtWidgets import *
import conFilter
import questions
import logo_rc
import subprocess
from chart import Chart_MainWindow
from functions import Connection, Message, clearStr

class Result_MainWindow(object):
    def __init__(self, name, point, continent, time):
        self.name = name
        self.point = point
        self.continent = continent
        self.time = str(time)

    def setupUi(self, MainWindow):
        if MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(932, 520)
        self.window = MainWindow
        self.window.setWindowIcon(QIcon('globe_world_earth_planets_chool_icon_209251.png'))
        #MainWindow.resize(1118.4, 852)
        MainWindow.setStyleSheet(u"background-color: rgb(210, 210, 210);\n"
                                         "")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.headerF = QFrame(self.centralwidget)
        self.headerF.setObjectName(u"headerF")
        self.headerF.setMinimumSize(QSize(0, 200))
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
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.bodyF.sizePolicy().hasHeightForWidth())
        self.bodyF.setSizePolicy(sizePolicy)
        self.bodyF.setMinimumSize(QSize(0, 0))
        self.bodyF.setStyleSheet(u"background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.506, stop:0 rgba(255, 255, 0, 255), stop:1 rgba(210, 210, 210, 210));")
        self.bodyF.setFrameShape(QFrame.StyledPanel)
        self.bodyF.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.bodyF)
        self.gridLayout.setObjectName(u"gridLayout")
        self.resultL = QLabel(self.bodyF)
        self.resultL.setObjectName(u"resultL")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.resultL.sizePolicy().hasHeightForWidth())
        self.resultL.setSizePolicy(sizePolicy1)
        self.resultL.setStyleSheet(u"font: 26px \"MS Shell Dlg 2\";")

        self.gridLayout.addWidget(self.resultL, 0, 0, 1, 1)

        self.resultpointL = QLabel(self.bodyF)
        self.resultpointL.setObjectName(u"resultpointL")
        sizePolicy1.setHeightForWidth(self.resultpointL.sizePolicy().hasHeightForWidth())
        self.resultpointL.setSizePolicy(sizePolicy1)
        self.resultpointL.setStyleSheet(u"font: 75 28px \"MS Shell Dlg 2\";")

        self.gridLayout.addWidget(self.resultpointL, 0, 1, 1, 1)

        self.pointL = QLabel(self.bodyF)
        self.pointL.setObjectName(u"pointL")
        sizePolicy1.setHeightForWidth(self.pointL.sizePolicy().hasHeightForWidth())
        self.pointL.setSizePolicy(sizePolicy1)
        self.pointL.setStyleSheet(u"font: 26px \"MS Shell Dlg 2\";")

        self.gridLayout.addWidget(self.pointL, 0, 2, 1, 1)

        self.timeL = QLabel(self.bodyF)
        self.timeL.setObjectName(u"timeL")
        sizePolicy1.setHeightForWidth(self.timeL.sizePolicy().hasHeightForWidth())
        self.timeL.setSizePolicy(sizePolicy1)
        self.timeL.setStyleSheet(u"font: 26px \"MS Shell Dlg 2\";")

        self.gridLayout.addWidget(self.timeL, 1, 0, 1, 1)

        self.timesecL = QLabel(self.bodyF)
        self.timesecL.setObjectName(u"timesecL")
        sizePolicy1.setHeightForWidth(self.timesecL.sizePolicy().hasHeightForWidth())
        self.timesecL.setSizePolicy(sizePolicy1)
        self.timesecL.setStyleSheet(u"font: 75 28px \"MS Shell Dlg 2\";")

        self.gridLayout.addWidget(self.timesecL, 1, 1, 1, 1)

        self.secL = QLabel(self.bodyF)
        self.secL.setObjectName(u"secL")
        sizePolicy1.setHeightForWidth(self.secL.sizePolicy().hasHeightForWidth())
        self.secL.setSizePolicy(sizePolicy1)
        self.secL.setStyleSheet(u"font: 26px \"MS Shell Dlg 2\";")

        self.gridLayout.addWidget(self.secL, 1, 2, 1, 1)

        self.verticalLayout.addWidget(self.bodyF)

        self.buttonsF = QFrame(self.centralwidget)
        self.buttonsF.setObjectName(u"buttonsF")
        self.buttonsF.setMinimumSize(QSize(0, 120))
        self.buttonsF.setMaximumSize(QSize(16777215, 60))
        self.buttonsF.setFrameShape(QFrame.StyledPanel)
        self.buttonsF.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.buttonsF)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.resultsPB = QPushButton(self.buttonsF)
        self.resultsPB.setObjectName(u"resultsPB")
        self.resultsPB.setMinimumSize(QSize(0, 50))
        self.resultsPB.setStyleSheet(u"font: 75 26px \"MS Shell Dlg 2\";\n"
                                        "background-color: rgb(255, 255, 0);")

        self.horizontalLayout_2.addWidget(self.resultsPB)

        self.menuPB = QPushButton(self.buttonsF)
        self.menuPB.setObjectName(u"menuPB")
        self.menuPB.setMinimumSize(QSize(0, 50))
        self.menuPB.setMaximumSize(QSize(16777215, 16777215))
        self.menuPB.setStyleSheet(u"font: 75 26px \"MS Shell Dlg 2\";\n"
                                    "background-color: rgb(255, 255, 0);")

        self.horizontalLayout_2.addWidget(self.menuPB)

        self.againPB = QPushButton(self.buttonsF)
        self.againPB.setObjectName(u"againPB")
        self.againPB.setMinimumSize(QSize(0, 50))
        self.againPB.setMaximumSize(QSize(16777215, 16777215))
        self.againPB.setStyleSheet(u"font: 75 26px \"MS Shell Dlg 2\";\n"
                                    "background-color: rgb(255, 255, 0);")

        self.horizontalLayout_2.addWidget(self.againPB)

        self.verticalLayout.addWidget(self.buttonsF)

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
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"VilágBajnok - Eredmény", None))
        self.textL.setText(QCoreApplication.translate("MainWindow", u"Vil\u00e1gBajnok", None))
        self.logoL.setText("")
        self.resultL.setText(QCoreApplication.translate("MainWindow", u"Eredm\u00e9ny: ", None))
        self.resultpointL.setText(QCoreApplication.translate("MainWindow", str(self.point), None))
        self.pointL.setText(QCoreApplication.translate("MainWindow", u"pont", None))
        self.timeL.setText(QCoreApplication.translate("MainWindow", u"Id\u0151: ", None))
        self.timesecL.setText(self.time)
        #self.idompL.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.secL.setText(QCoreApplication.translate("MainWindow", u"m\u00e1sodperc", None))
        self.resultsPB.setText(QCoreApplication.translate("MainWindow", u"Eredm\u00e9nyeim", None))
        self.menuPB.setText(QCoreApplication.translate("MainWindow", u"Men\u00fc", None))
        self.againPB.setText(QCoreApplication.translate("MainWindow", u"\u00dajra", None))


            # retranslateUi

        self.pointInDb()
        self.menuPB.clicked.connect(self.openContinents)
        self.againPB.clicked.connect(self.openKerdes)
        self.resultsPB.clicked.connect(self.openChart)

    def sleepButtons(self):
        self.menuPB.setEnabled(False)
        self.againPB.setEnabled(False)
        self.resultsPB.setEnabled(False)

    def activedButtons(self):
        self.menuPB.setEnabled(True)
        self.againPB.setEnabled(True)
        self.resultsPB.setEnabled(True)

    def openChart(self):
        chart = Chart_MainWindow(self.name, self.continent)
        chart.makeChart()

    def openContinents(self):
        con, cur = Connection()
        if con is not None:
            self.sleepButtons()
            self.window.close()
            self.window = QtWidgets.QMainWindow()
            self.ui = conFilter.Continents_MainWindow(self.name)
            self.ui.setupUi(self.window)
            self.window.show()
        else:
            Message("HIBAÜZENET", "Adatbázis kapcsolati hiba! Ellenőrizd az internetelérésed!")
            self.activedButtons()

    def openKerdes(self):
        con, cur = Connection()
        if con is not None:
            self.sleepButtons()
            self.window.close()
            point = 0
            serial_number = 0
            self.window = QtWidgets.QMainWindow()
            self.ui = questions.Quiz_MainWindow(self.continent, self.name, point, serial_number)
            self.ui.setupUi(self.window)
            self.window.show()

        else:
            Message("HIBAÜZENET", "Adatbázis kapcsolati hiba! Ellenőrizd az internetelérésed!")
            self.activedButtons()


    def pointInDb(self):

        con, cur = Connection()
        if con is None:
            Message("HIBAÜZENET", "Adatbázis kapcsolati hiba! Ellenőrizd az internetelérésed!")
            self.activedButtons()
        else:
            goods = 'select pont, ido, jatek, ossz from eredmeny where nev = %s and kontinens = %s'
            cur.execute(goods, (self.name, self.continent))
            res = cur.fetchall()
            res = clearStr(str(res))
            if len(res) > 0:
                lista = []
                lista.append(res.split(' '))
                print(lista[0])

                if (self.point > int(lista[0][0])) or ((self.point == int(lista[0][0])) and (int(self.time) < int(lista[0][1]))):
                #add = 'update %s set pont = %s, jatek = %s where nev = %s'
                #cur.execute(add, (self.continent, self.point, int(lista[0][1]) + 1, self.name))
                    add = 'update eredmeny set pont = %s, ido = %s, jatek = %s, ossz = %s where nev = %s and kontinens = %s'
                    cur.execute(add, (self.point, int(lista[0][1]), int(lista[0][2]) + 1, int(lista[0][3]) + self.point, self.name, self.continent ))
                    con.commit()
                    con.close()
                    self.addResults()

                else:
                    add = 'update eredmeny set jatek = %s, ossz = %s where nev = %s and kontinens = %s'
                    cur.execute(add, (int(lista[0][2]) + 1, int(lista[0][3]) + self.point, self.name, self.continent))
                #add = 'update %s set jatek = %s where nev = %s'
                #cur.execute(add, (self.continent, int(lista[0][1]) + 1, self.name))
                    con.commit()
                    con.close()
                    self.addResults()
            else:
            #add = "insert into %s (nev,kontinens,pont,jatek) values (%s,%s,%s,%s)"
            #cur.execute(add, (self.continent, self.name, self.continent, self.point, 1))
                add = "insert into eredmeny (nev,kontinens,pont,ido,jatek,ossz) values (%s,%s,%s,%s,%s,%s)"
                cur.execute(add, (self.name, self.continent, self.point, int(self.time), 1, self.point))
                con.commit()
                con.close()
                self.addResults()

    def addResults(self):
        con, cur = Connection()
        id = self.newId()
        print(id)
        if con is None or id is None:
            Message("HIBAÜZENET", "Adatbázis kapcsolati hiba! Ellenőrizd az internetelérésed!")
            self.activedButtons()
        else:
            new = "insert into eredmenyek (id,nev,kontinens,pont,ido) values (%s,%s,%s,%s,%s)"
            cur.execute(new, (id, self.name, self.continent, self.point, self.time))
            con.commit()
            con.close()

    def newId(self):
        con, cur = Connection()
        if con is None:
            return None
        else:
            num = "select count(*) from eredmenyek"
            cur.execute(num)
            id = cur.fetchall()
            add_id = int(clearStr(str(id)))
            con.commit()
            con.close()
            return add_id



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Result_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
