import PySide2.QtWidgets as QtWidgets
# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'udv-teljKdEOrj.ui'
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

import hatter_rc

import subprocess
import login
import reg
import info

#from reg import Ui_MainWindow2



class HomePage_MainWindow(object):
    #def reg(self):
        #self.window2 = QtWidgets.QMainWindow()
        #self.ui = Ui_MainWindow2()
        #self.ui.setupUi(self.window2)
        #self.window2.show()
    def setupUi(self, MainWindow):
        if MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(932, 520)
        MainWindow.setWindowIcon(QIcon('globe_world_earth_planets_chool_icon_209251.png'))
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QSize(932, 520))
        MainWindow.setMaximumSize(QSize(932, 520))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(0, 0, 932, 520))
        self.torzs = QLabel(self.widget)
        self.torzs.setObjectName(u"torzs")
        self.torzs.setGeometry(QRect(0, 0, 932, 520))
        self.torzs.setStyleSheet(u"border-image: url(:/hatter/udv.png);")
        self.filter = QLabel(self.widget)
        self.filter.setObjectName(u"filter")
        self.filter.setGeometry(QRect(0, 0, 932, 520))
        self.filter.setStyleSheet(u"background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0 rgba(0, 0, 0, 0));")
        self.loginPB = QPushButton(self.widget)
        self.loginPB.setObjectName(u"loginPB")
        self.loginPB.setGeometry(QRect(779, 130, 141, 50))
        self.loginPB.setStyleSheet(u"background-color: rgb(255, 255, 0);\n"
"font: 18px \"MS Shell Dlg 2\";")
        self.regPB = QPushButton(self.widget)
        self.regPB.setObjectName(u"regPB")
        self.regPB.setGeometry(QRect(779, 390, 141, 50))
        self.regPB.setStyleSheet(u"background-color: rgb(255, 255, 0);\n"
"font: 18px \"MS Shell Dlg 2\";")
        self.desPB = QPushButton(self.widget)
        self.desPB.setObjectName(u"desPB")
        self.desPB.setGeometry(QRect(779, 260, 141, 50))
        self.desPB.setStyleSheet(u"background-color: rgb(255, 255, 0);\n"
"font: 18px \"MS Shell Dlg 2\";")
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
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"VilágBajnok - Kezdőlap", None))
        self.torzs.setText("")
        self.filter.setText("")
        self.loginPB.setText(QCoreApplication.translate("MainWindow", u"Bejelentkez\u00e9s", None))
        self.regPB.setText(QCoreApplication.translate("MainWindow", u"Regisztr\u00e1ci\u00f3", None))
        self.desPB.setText(QCoreApplication.translate("MainWindow", u"J\u00e1t\u00e9k le\u00edr\u00e1s", None))
        self.regPB.clicked.connect(MainWindow.close)
        self.regPB.clicked.connect(self.openReg)
        self.loginPB.clicked.connect(MainWindow.close)
        self.loginPB.clicked.connect(self.openLogin)
        self.desPB.clicked.connect(MainWindow.close)
        self.desPB.clicked.connect(self.openDescription)


    def sleepButtons(self):
        self.regPB.setEnabled(False)
        self.loginPB.setEnabled(False)
        self.desPB.setEnabled(False)

    def openReg(self):
        self.sleepButtons()
        #subprocess.call(["python", "reg.exe"])
        self.window = QtWidgets.QMainWindow()
        self.ui = reg.Reg_MainWindow()
        self.ui.setupUi(self.window)
        self.window.show()

    def openLogin(self):
        self.sleepButtons()
        #subprocess.call(["python", "login.exe"])
        self.window = QtWidgets.QMainWindow()
        self.ui = login.Login_MainWindow()
        self.ui.setupUi(self.window)
        self.window.show()

    def openDescription(self):
        self.sleepButtons()
        #subprocess.call(["python", "info.exe"])
        self.window = QtWidgets.QMainWindow()
        self.ui = info.Ui_MainWindow()
        self.ui.setupUi(self.window)
        self.window.show()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()

    ui = HomePage_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())




