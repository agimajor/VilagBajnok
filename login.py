import PySide2.QtWidgets as QtWidgets
from PySide2 import QtCore
from PySide2.QtCore import (QCoreApplication, QMetaObject, QRect, QSize, QUrl, Qt)
from PySide2.QtGui import QIcon
from PySide2.QtWidgets import *
import conFilter
import logo_rc
import subprocess
from functions import Message, Connection, clearStr
import opener
import userInfo


class Login_MainWindow(object):
    def setupUi(self, MainWindow):
        if MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        self.window = MainWindow
        self.window.setWindowFlag(QtCore.Qt.WindowCloseButtonHint, False)
        self.window.setWindowIcon(QIcon('globe_world_earth_planets_chool_icon_209251.png'))
        MainWindow.resize(932, 520)
        #MainWindow.resize(1118.4, 852)
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
        self.bodyF.setStyleSheet(u"background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.506, stop:0 rgba(255, 255, 0, 255), stop:1 rgba(210, 210, 210, 210));")
        self.bodyF.setFrameShape(QFrame.StyledPanel)
        self.bodyF.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.bodyF)
        self.gridLayout.setObjectName(u"gridLayout")
        self.nameLE = QLineEdit(self.bodyF)
        self.nameLE.setObjectName(u"nameLE")
        self.nameLE.setMinimumSize(QSize(0, 30))
        self.nameLE.setMaximumSize(QSize(16777215, 16777215))
        self.nameLE.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.gridLayout.addWidget(self.nameLE, 1, 2, 1, 1)

        self.passwL = QLabel(self.bodyF)
        self.passwL.setObjectName(u"passwL")
        self.passwL.setMinimumSize(QSize(80, 30))
        self.passwL.setStyleSheet(u"font: 75 26px \"MS Shell Dlg 2\";\n"
"background-color: rgb(210, 210, 210);")

        self.gridLayout.addWidget(self.passwL, 4, 1, 1, 1)

        self.backPB = QPushButton(self.bodyF)
        self.backPB.setObjectName(u"backPB")
        self.backPB.setStyleSheet(u"font: 75 26px \"MS Shell Dlg 2\";\n"
                                  "background-color: rgb(255, 255, 0);")

        self.gridLayout.addWidget(self.backPB, 0, 1, 1, 1)

        self.nameL = QLabel(self.bodyF)
        self.nameL.setObjectName(u"nameL")
        self.nameL.setMinimumSize(QSize(80, 30))
        self.nameL.setStyleSheet(u"font: 75 26px \"MS Shell Dlg 2\";\n"
"background-color: rgb(210,  210, 210);")

        self.gridLayout.addWidget(self.nameL, 1, 1, 1, 1)

        self.passwLE = QLineEdit(self.bodyF)
        self.passwLE.setObjectName(u"passwLE")
        self.passwLE.setMinimumSize(QSize(0, 30))
        self.passwLE.setMaximumSize(QSize(16777215, 16777215))
        self.passwLE.setStyleSheet(u"background-color: rgb(133, 133, 133);\n"
"background-color: rgb(255, 255, 255);")
        self.passwLE.setEchoMode(QLineEdit.Password)

        self.gridLayout.addWidget(self.passwLE, 4, 2, 1, 1)


        self.verticalLayout.addWidget(self.bodyF)

        self.loginPB = QPushButton(self.centralwidget)
        self.loginPB.setObjectName(u"loginPB")
        self.loginPB.setMaximumSize(QSize(16777215, 50))
        self.loginPB.setStyleSheet(u"font: 75 26px \"MS Shell Dlg 2\";\n"
"background-color: rgb(255, 255, 0);")

        self.verticalLayout.addWidget(self.loginPB)

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
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"VilágBajnok - Bejelentkezés", None))
        self.textL.setText(QCoreApplication.translate("MainWindow", u"Vil\u00e1gBajnok", None))
        #self.logoL.setText("")
        self.backPB.setText("⇦ Vissza")
        self.passwL.setText(QCoreApplication.translate("MainWindow", u"Jelsz\u00f3:", None))
        self.nameL.setText(QCoreApplication.translate("MainWindow", u"N\u00e9v:", None))
        self.loginPB.setText(QCoreApplication.translate("MainWindow", u"Bejelentkez\u00e9s", None))
        self.loginPB.clicked.connect(self.LogIn)
        self.backPB.clicked.connect(self.BackOpenWindow)

    def sleepButtons(self): #gombok blokkolása
        self.loginPB.setEnabled(False)
        self.backPB.setEnabled(False)

    def activeButtons(self): #gombok aktiválása
        self.loginPB.setEnabled(True)
        self.backPB.setEnabled(True)

    def BackOpenWindow(self): #nyitó oldal meghívása
        self.sleepButtons()
        self.window.close()
        subprocess.call(["python", "opener.py"])
        
    def LogIn(self): #bejelentkezés ellenőrzése

        self.sleepButtons()
        con, cur = Connection()
        if con is None:
            Message("HIBAÜZENET", "Adatbázis kapcsolati hiba! Ellenőrizd az internetelérésed!")
            self.activeButtons()

        else:
            try:
                query = 'select jelszo from regisztraciok where nev =\''+self.nameLE.text()+"\'"
                cur.execute(query)
                result_passw = cur.fetchone()[0]

            except TypeError:
                Message("HIBAÜZENET", "Hoppá valami probléma adódott! Ellenőrizd a beírt adatokat, majd próbálkozz újra!")
                self.activeButtons()

            else:
                if result_passw == self.passwLE.text():
                    names = 'select nev from adatok where nev =\''+self.nameLE.text()+"\'"
                    cur.execute(names)
                    name_res = cur.fetchall()
                    name_res = clearStr(str(name_res))
                    if name_res == self.nameLE.text():
                        self.open_window()
                    else:
                        self.window.close()
                        self.window = QtWidgets.QMainWindow()
                        name = self.nameLE.text()
                        self.ui = userInfo.Quest_MainWindow(name)
                        self.ui.setupUi(self.window)
                        self.window.show()

                else:
                    Message("HIBAÜZENET", "Hoppá valami probléma adódott! Ellenőrizd a beírt adatokat, majd próbálkozz újra!")
                    self.activeButtons()


    def open_window(self): #szűrő oldal meghívása
        self.window.close()
        name = self.nameLE.text()
        self.window = QtWidgets.QMainWindow()
        self.ui = conFilter.Continents_MainWindow(name)
        self.ui.setupUi(self.window)
        self.window.show()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Login_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())



