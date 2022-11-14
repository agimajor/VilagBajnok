import time

import PyQt5
import PySide2.QtWidgets as QtWidgets
# -*- coding: utf-8 -*-
from mysql.connector import MySQLConnection
import mysql
import numpy as np
import random
from PyQt5.QtCore import QTimer
################################################################################
## Form generated from reading UI file 'kerdes-teljVCRFeD.ui'
##
## Created by: Qt User Interface Compiler version 5.14.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################
from functools import partial
from PySide2.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt, QTime)

from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient)
from PySide2.QtWidgets import *
from results import Result_MainWindow

import conFilter
import logo_rc
import subprocess
from functools import partial
from functions import Message, Connection, clearStr


from PySide2.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
                            QRect, QSize, QUrl, Qt, QEvent, QTime)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
                           QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
                           QRadialGradient)
from PySide2.QtWidgets import *

from random import randint


class Quiz_MainWindow(object):
    def __init__(self, continent, name, point, serial_number):

        super().__init__()
        self.continent = continent
        self.name = name
        self.point = point
        self.serial_number = serial_number
        self.goods_list = self.QuestionsList(self.continent)

        self.activegame = True
        #self.count = 1800
        self.timer = QTimer()
        self.timer.timeout.connect(self.ShowTime)
        self.timer.start(1000)
        self.start = False
        self.count = 0

    def setupUi(self, MainWindow):
        if MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        self.window = MainWindow
        self.window.setWindowIcon(QIcon('globe_world_earth_planets_chool_icon_209251.png'))
        #MainWindow.resize(1118.4, 852)
        MainWindow.resize(932, 520)
        MainWindow.setStyleSheet(u"background-color: rgb(210, 210, 210);\n"
"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.timeL = QLabel(self.centralwidget)
        self.timeL.setObjectName(u"timeL")
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.timeL.sizePolicy().hasHeightForWidth())
        self.timeL.setSizePolicy(sizePolicy)
        self.timeL.setMinimumSize(QSize(30, 30))
        self.timeL.setMaximumSize(QSize(200, 50))
        self.timeL.setStyleSheet(u"font: 18px \"MS Shell Dlg 2\";")

        self.verticalLayout.addWidget(self.timeL)

        self.headerF = QFrame(self.centralwidget)
        self.headerF.setObjectName(u"headerF")
        self.headerF.setMinimumSize(QSize(0, 100))
        self.headerF.setMaximumSize(QSize(16777215, 80))
        self.headerF.setStyleSheet(u"font: 26px \"MS Shell Dlg 2\";\n"
"background-color: rgb(210, 210, 210);\n"
"")
        self.headerF.setFrameShape(QFrame.StyledPanel)
        self.headerF.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.headerF)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.questL = QLabel(self.headerF)
        self.questL.setObjectName(u"questL")
        self.questL.setStyleSheet(u"font: 26px \"MS Shell Dlg 2\";\n"
"background-color: rgb(255, 255, 0);\n"
"")

        self.horizontalLayout.addWidget(self.questL)


        self.verticalLayout.addWidget(self.headerF)

        self.bodyF = QFrame(self.centralwidget)
        self.bodyF.setObjectName(u"bodyF")
        self.bodyF.setStyleSheet(u"font: 26px \"MS Shell Dlg 2\";\n"
"background-color: rgb(210, 210, 210);\n"
"")
        self.bodyF.setFrameShape(QFrame.StyledPanel)
        self.bodyF.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.bodyF)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.answer1 = QRadioButton(self.bodyF)
        self.answer1.setObjectName(u"answer1")
        sizePolicy.setHeightForWidth(self.answer1.sizePolicy().hasHeightForWidth())
        self.answer1.setSizePolicy(sizePolicy)
        self.answer1.setMaximumSize(QSize(16777215, 16777215))
        self.answer1.setStyleSheet(u"font: 26px \"MS Shell Dlg 2\";\n"
"background-color: rgb(210, 210, 210);\n"
"")

        self.verticalLayout_2.addWidget(self.answer1)

        self.answer2 = QRadioButton(self.bodyF)
        self.answer2.setObjectName(u"answerz2")
        sizePolicy.setHeightForWidth(self.answer2.sizePolicy().hasHeightForWidth())
        self.answer2.setSizePolicy(sizePolicy)
        self.answer2.setMaximumSize(QSize(16777215, 16777215))
        self.answer2.setStyleSheet(u"font: 26px \"MS Shell Dlg 2\";\n"
"background-color: rgb(210, 210, 210);")

        self.verticalLayout_2.addWidget(self.answer2)

        self.answer3 = QRadioButton(self.bodyF)
        self.answer3.setObjectName(u"answer3")
        sizePolicy.setHeightForWidth(self.answer3.sizePolicy().hasHeightForWidth())
        self.answer3.setSizePolicy(sizePolicy)
        self.answer3.setMaximumSize(QSize(16777215, 16777215))
        self.answer3.setStyleSheet(u"font: 26px \"MS Shell Dlg 2\";\n"
"background-color: rgb(210, 210, 210);")

        self.verticalLayout_2.addWidget(self.answer3)

        self.answer4 = QRadioButton(self.bodyF)
        self.answer4.setObjectName(u"answer4")
        sizePolicy.setHeightForWidth(self.answer4.sizePolicy().hasHeightForWidth())
        self.answer4.setSizePolicy(sizePolicy)
        self.answer4.setMinimumSize(QSize(0, 0))
        self.answer4.setMaximumSize(QSize(16777215, 16777215))
        self.answer4.setStyleSheet(u"font: 26px \"MS Shell Dlg 2\";\n"
"background-color: rgb(210, 210, 210);\n"
"")

        self.verticalLayout_2.addWidget(self.answer4)


        self.verticalLayout.addWidget(self.bodyF)

        self.nextPB = QPushButton(self.centralwidget)
        self.nextPB.setObjectName(u"nextPB")
        self.nextPB.setMinimumSize(QSize(0, 50))
        self.nextPB.setMaximumSize(QSize(16777215, 30))
        self.nextPB.setStyleSheet(u"font: 75 26px \"MS Shell Dlg 2\";\n"
"background-color: rgb(255, 255, 0);")

        self.verticalLayout.addWidget(self.nextPB)

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
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"VilágBajnok - Quiz", None))
        #self.idoL.setText(QCoreApplication.translate("MainWindow", ido, None))
        #self.idoL.setText("0")
        #self.idoL.setText("⏳: " + str(self.count))
        self.nextPB.setText(QCoreApplication.translate("MainWindow", u"Tov\u00e1bb", None))
        self.group = QtWidgets.QButtonGroup()
        self.group.addButton(self.answer1)
        self.group.addButton(self.answer2)
        self.group.addButton(self.answer3)
        self.group.addButton(self.answer4)

        self.start = True
        self.startQuestion()

        if self.activegame == False:
            MainWindow.close()

    # retranslateUi
    def ShowTime(self):
        #self.count += 1
        if self.start:
            self.count += 1
            min = (self.count//60)
            sec = (self.count%60)
            idostr ='⏳: {:02d}:{:02d}'.format(min, sec)
            #idostr = (self.count)
            self.timeL.setText(idostr)

    def QuestionsList(self, continent):
        con, cur = Connection()
        if con is not None:
            good_num = 'select kerdes_id from kerdesek where kategoria =\'' + continent + "\'"
            cur.execute(good_num)
            quiz_num_res = cur.fetchall()
            rand_quiz = set()
            while len(rand_quiz) < 10:
                idx = random.randint(0, 29)
                rand_quiz.add(int(clearStr(str(quiz_num_res[idx]))))
            return list(rand_quiz)
        else:
            return None


    def startQuestion(self):
        self.nextPB.setEnabled(True)
        self.group.setExclusive(False)
        self.answer1.setChecked(False)
        self.answer2.setChecked(False)
        self.answer3.setChecked(False)
        self.answer4.setChecked(False)
        self.group.setExclusive(True)
        print(self.serial_number)
        self.goodQuestions()


    def goodQuestions(self):
        con, cur = Connection()
        if con is not None and self.goods_list is not None:
            e = str(self.goods_list[self.serial_number])
            e = clearStr(e)
            question = 'select kerdes, valasz1, valasz2, valasz3, valasz4, helyes from kerdesek where kerdes_id =\'' + e + "\'"
            cur.execute(question)
            res1 = cur.fetchall()
            res1 = str(list(res1))
            print(res1)
            self.kerdes, self.v1, self.v2, self.v3, self.v4, self.jo = res1.split(",")

            self.questL.setText(str(self.serial_number + 1) + ". " + clearStr(self.kerdes))
            self.answer1.setText(clearStr(self.v1))
            self.answer2.setText(clearStr(self.v2))
            self.answer3.setText(clearStr(self.v3))
            self.answer4.setText(clearStr(self.v4))

            self.nextPB.clicked.connect(self.addCheck)
        else:
            self.start = False
            self.open_continents()
            #MainWindow.close()



    def addCheck(self):
        self.nextPB.setEnabled(False)
        if self.answer1.isChecked():
            self.addPoint(1)
        elif self.answer2.isChecked():
            self.addPoint(2)
        elif self.answer3.isChecked():
            self.addPoint(3)
        elif self.answer4.isChecked():
            self.addPoint(4)
        else:
            self.nextPB.setEnabled(True)
            #msg = QMessageBox()
            #msg.setWindowTitle("HIBA")
            #msg.setIcon(QMessageBox.Warning)
            #msg.setText("Válaszd ki az általad helyesnek ítélt megoldást mielőtt tovább lépsz!")
            #msg.exec()


    def addPoint(self, answer):
        print(self.serial_number)
        if answer == int(clearStr(self.jo)):

            self.point += 1

            if self.serial_number == 9 and self.activegame:
                self.activegame = False
                self.start = False
                #QtWidgets.QMainWindow.close(self)
                #MainWindow.close()
                self.open_result()


            elif self.activegame:
                self.serial_number += 1
                self.nextQuestion()

        else:
            self.point = self.point
            if self.serial_number == 9 and self.activegame:
                self.start = False
                self.activegame = False
                #QtWidgets.QMainWindow.close(self)
                #MainWindow.close()
                self.open_result()


            elif self.activegame:
                self.serial_number += 1
                self.nextQuestion()


    def open_result(self):
        #MainWindow.close()
        self.window.close()
        self.window = QtWidgets.QMainWindow()
        self.ui = Result_MainWindow(self.name, self.point, self.continent, self.count)
        self.ui.setupUi(self.window)
        self.window.show()
        #MainWindow1.close()

    def open_continents(self):

        self.window.close()
        self.window = QtWidgets.QMainWindow()
        self.ui = conFilter.Continents_MainWindow(self.name)
        self.ui.setupUi(self.window)
        self.window.show()

    def nextQuestion(self):
        self.startQuestion()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Quiz_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())


