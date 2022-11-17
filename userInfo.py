from PySide2 import QtCore
import PySide2.QtWidgets as QtWidgets
from PySide2.QtCore import (QCoreApplication, QMetaObject, QRect, QSize)
from PySide2.QtGui import QIcon
from PySide2.QtWidgets import *
import logo_rc
import subprocess
from functions import Message, Connection
import conFilter


class Quest_MainWindow(object):
    def __init__(self, name):
        self.name = name
        self.next = False
    def setupUi(self, MainWindow):
        if MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        self.window = MainWindow
        self.window.setWindowFlag(QtCore.Qt.WindowCloseButtonHint, False)
        self.window.setWindowIcon(QIcon('globe_world_earth_planets_chool_icon_209251.png'))
        MainWindow.resize(932, 520)
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
        self.logoL.setMaximumSize(QSize(216, 99))
        self.logoL.setStyleSheet(u"border-image: url(:/logo/logo.png);")

        self.horizontalLayout.addWidget(self.logoL)

        self.verticalLayout.addWidget(self.headerF)

        self.bodyF = QFrame(self.centralwidget)
        self.bodyF.setObjectName(u"bodyF")
        self.bodyF.setStyleSheet(u"background-color: rgb(210, 210, 210);")
        self.bodyF.setFrameShape(QFrame.StyledPanel)
        self.bodyF.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.bodyF)
        self.gridLayout.setObjectName(u"gridLayout")
        self.q5L = QLabel(self.bodyF)
        self.q5L.setObjectName(u"q5L")
        self.q5L.setMinimumSize(QSize(0, 0))
        self.q5L.setMaximumSize(QSize(16777215, 16777215))
        self.q5L.setStyleSheet(u"font: 75 26px \"MS Shell Dlg 2\";\n"
                               "background-color: rgb(255, 255, 0);")

        self.gridLayout.addWidget(self.q5L, 9, 0, 1, 9)

        self.one2RB = QCheckBox(self.bodyF)
        self.one2RB.setObjectName(u"one2RB")
        self.one2RB.setStyleSheet(u"font: 75 20px \"MS Shell Dlg 2\";\n"
                                  "background-color: rgb(210, 210, 210);")

        self.gridLayout.addWidget(self.one2RB, 10, 0, 1, 1)

        self.one1RB = QCheckBox(self.bodyF)
        self.one1RB.setObjectName(u"egy1RB")
        self.one1RB.setStyleSheet(u"font: 75 20px \"MS Shell Dlg 2\";\n"
                                  "background-color: rgb(210, 210, 210);")

        self.gridLayout.addWidget(self.one1RB, 8, 0, 1, 1)

        self.four2RB = QCheckBox(self.bodyF)
        self.four2RB.setObjectName(u"four2RB")
        self.four2RB.setStyleSheet(u"font: 75 20px \"MS Shell Dlg 2\";\n"
                                   "background-color: rgb(210, 210, 210);")

        self.gridLayout.addWidget(self.four2RB, 10, 3, 1, 1)

        self.five2RB = QCheckBox(self.bodyF)
        self.five2RB.setObjectName(u"five2RB")
        self.five2RB.setStyleSheet(u"font: 75 20px \"MS Shell Dlg 2\";\n"
                                 "background-color: rgb(210, 210, 210);")

        self.gridLayout.addWidget(self.five2RB, 10, 4, 1, 1)

        self.boyRB = QCheckBox(self.bodyF)
        self.boyRB.setObjectName(u"boyRB")
        self.boyRB.setStyleSheet(u"font: 75 20px \"MS Shell Dlg 2\";\n"
                                 "background-color: rgb(210, 210, 210);")

        self.gridLayout.addWidget(self.boyRB, 1, 0, 1, 1)

        self.five1RB = QCheckBox(self.bodyF)
        self.five1RB.setObjectName(u"ot1RB")
        self.five1RB.setStyleSheet(u"font: 75 20px \"MS Shell Dlg 2\";\n"
                                 "background-color: rgb(210, 210, 210);")

        self.gridLayout.addWidget(self.five1RB, 8, 4, 1, 1)

        self.q4L = QLabel(self.bodyF)
        self.q4L.setObjectName(u"k4L")
        self.q4L.setMinimumSize(QSize(0, 0))
        self.q4L.setMaximumSize(QSize(16777215, 16777215))
        self.q4L.setStyleSheet(u"font: 75 26px \"MS Shell Dlg 2\";\n"
                               "background-color: rgb(255, 255, 0);")

        self.gridLayout.addWidget(self.q4L, 7, 0, 1, 9)

        self.three2RB = QCheckBox(self.bodyF)
        self.three2RB.setObjectName(u"three2RB")
        self.three2RB.setStyleSheet(u"font: 75 20px \"MS Shell Dlg 2\";\n"
                                    "background-color: rgb(210, 210, 210);")

        self.gridLayout.addWidget(self.three2RB, 10, 2, 1, 1)

        self.q3L = QLabel(self.bodyF)
        self.q3L.setObjectName(u"q3L")
        self.q3L.setMinimumSize(QSize(0, 0))
        self.q3L.setMaximumSize(QSize(16777215, 16777215))
        self.q3L.setStyleSheet(u"font: 75 26px \"MS Shell Dlg 2\";\n"
                               "background-color: rgb(255, 255, 0);")

        self.gridLayout.addWidget(self.q3L, 4, 0, 1, 9)

        self.no3RB = QCheckBox(self.bodyF)
        self.no3RB.setObjectName(u"no3RB")
        self.no3RB.setStyleSheet(u"font: 75 20px \"MS Shell Dlg 2\";\n"
                                 "background-color: rgb(210, 210, 210);")

        self.gridLayout.addWidget(self.no3RB, 5, 2, 1, 1)

        self.yes2RB = QCheckBox(self.bodyF)
        self.yes2RB.setObjectName(u"yes2RB")
        self.yes2RB.setStyleSheet(u"font: 75 20px \"MS Shell Dlg 2\";\n"
                                 "background-color: rgb(210, 210, 210);")

        self.gridLayout.addWidget(self.yes2RB, 3, 0, 1, 1)

        self.two2RB = QCheckBox(self.bodyF)
        self.two2RB.setObjectName(u"two2RB")
        self.two2RB.setStyleSheet(u"font: 75 20px \"MS Shell Dlg 2\";\n"
                                    "background-color: rgb(210, 210, 210);")

        self.gridLayout.addWidget(self.two2RB, 10, 1, 1, 1)

        self.four1RB = QCheckBox(self.bodyF)
        self.four1RB.setObjectName(u"four1RB")
        self.four1RB.setStyleSheet(u"font: 75 20px \"MS Shell Dlg 2\";\n"
                                   "background-color: rgb(210, 210, 210);")

        self.gridLayout.addWidget(self.four1RB, 8, 3, 1, 1)

        self.girlRB = QCheckBox(self.bodyF)
        self.girlRB.setObjectName(u"girlRB")
        self.girlRB.setStyleSheet(u"font: 75 20px \"MS Shell Dlg 2\";\n"
                                  "background-color: rgb(210, 210, 210);")

        self.gridLayout.addWidget(self.girlRB, 1, 2, 1, 1)

        self.q1L = QLabel(self.bodyF)
        self.q1L.setObjectName(u"q1L")
        self.q1L.setMinimumSize(QSize(0, 0))
        self.q1L.setMaximumSize(QSize(16777215, 16777215))
        self.q1L.setStyleSheet(u"font: 75 26px \"MS Shell Dlg 2\";\n"
                               "background-color: rgb(255, 255, 0);")

        self.gridLayout.addWidget(self.q1L, 0, 0, 1, 9)

        self.q2L = QLabel(self.bodyF)
        self.q2L.setObjectName(u"q2L")
        self.q2L.setMinimumSize(QSize(0, 0))
        self.q2L.setMaximumSize(QSize(16777215, 16777215))
        self.q2L.setStyleSheet(u"font: 75 26px \"MS Shell Dlg 2\";\n"
                               "background-color: rgb(255, 255, 0);")

        self.gridLayout.addWidget(self.q2L, 2, 0, 1, 9)

        self.two1RB = QCheckBox(self.bodyF)
        self.two1RB.setObjectName(u"two1RB")
        self.two1RB.setStyleSheet(u"font: 75 20px \"MS Shell Dlg 2\";\n"
                                    "background-color: rgb(210, 210, 210);")

        self.gridLayout.addWidget(self.two1RB, 8, 1, 1, 1)

        self.yes3RB = QCheckBox(self.bodyF)
        self.yes3RB.setObjectName(u"yes3RB")
        self.yes3RB.setStyleSheet(u"font: 75 20px \"MS Shell Dlg 2\";\n"
                                 "background-color: rgb(210, 210, 210);")

        self.gridLayout.addWidget(self.yes3RB, 5, 0, 1, 1)

        self.no2RB = QCheckBox(self.bodyF)
        self.no2RB.setObjectName(u"no2RB")
        self.no2RB.setStyleSheet(u"font: 75 20px \"MS Shell Dlg 2\";\n"
                                 "background-color: rgb(210, 210, 210);")

        self.gridLayout.addWidget(self.no2RB, 3, 2, 1, 1)

        self.three1RB = QCheckBox(self.bodyF)
        self.three1RB.setObjectName(u"three1RB")
        self.three1RB.setStyleSheet(u"font: 75 20px \"MS Shell Dlg 2\";\n"
                                    "background-color: rgb(210, 210, 210);")

        self.gridLayout.addWidget(self.three1RB, 8, 2, 1, 1)

        self.verticalLayout.addWidget(self.bodyF)

        self.nextPB = QPushButton(self.centralwidget)
        self.nextPB.setObjectName(u"nextPB")
        self.nextPB.setMaximumSize(QSize(16777215, 50))
        self.nextPB.setStyleSheet(u"font: 75 20px \"MS Shell Dlg 2\";\n"
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
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"VilágBajnok - Kérdőív", None))
        self.textL.setText(QCoreApplication.translate("MainWindow", u"Vil\u00e1gBajnok", None))
        self.logoL.setText("")
        self.q5L.setText(QCoreApplication.translate("MainWindow",
                                                    u"Mekkora az \u00e9rdekl\u0151d\u00e9sed a Kontinensek t\u00e9mak\u00f6r ir\u00e1nt?",
                                                    None))
        self.one2RB.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.one1RB.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.four2RB.setText(QCoreApplication.translate("MainWindow", u"4", None))
        self.five2RB.setText(QCoreApplication.translate("MainWindow", u"5", None))
        self.boyRB.setText(QCoreApplication.translate("MainWindow", u"Fi\u00fa", None))
        self.five1RB.setText(QCoreApplication.translate("MainWindow", u"5", None))
        self.q4L.setText(
            QCoreApplication.translate("MainWindow", u"Mennyire szereted a F\u00f6ldrajz tant\u00e1rgyat?", None))
        self.three2RB.setText(QCoreApplication.translate("MainWindow", u"3", None))
        self.q3L.setText(QCoreApplication.translate("MainWindow",
                                                    u"Ett\u0151l elt\u00e9r\u0151 helyen is tanult\u00e1l m\u00e1r a t\u00e9m\u00e1r\u00f3l?",
                                                    None))
        self.no3RB.setText(QCoreApplication.translate("MainWindow", u"Nem", None))
        self.yes2RB.setText(QCoreApplication.translate("MainWindow", u"Igen", None))
        self.two2RB.setText(QCoreApplication.translate("MainWindow", u"2", None))
        self.four1RB.setText(QCoreApplication.translate("MainWindow", u"4", None))
        self.girlRB.setText(QCoreApplication.translate("MainWindow", u"L\u00e1ny", None))
        self.q1L.setText(QCoreApplication.translate("MainWindow", u"Mi a nemed?", None))
        self.q2L.setText(QCoreApplication.translate("MainWindow",
                                                    u"Iskolai keretek k\u00f6z\u00f6tt tanult\u00e1l m\u00e1r a Kontinensek t\u00e9m\u00e1r\u00f3?",
                                                    None))
        self.two1RB.setText(QCoreApplication.translate("MainWindow", u"2", None))
        self.yes3RB.setText(QCoreApplication.translate("MainWindow", u"Igen", None))
        self.no2RB.setText(QCoreApplication.translate("MainWindow", u"Nem", None))
        self.three1RB.setText(QCoreApplication.translate("MainWindow", u"3", None))
        self.nextPB.setText(QCoreApplication.translate("MainWindow", u"Tov\u00e1bb", None))
        # retranslateUi
        self.nextPB.clicked.connect(self.Quest)


    def Quest(self):
        self.nextPB.setEnabled(False)
        con, cur = Connection()

        if con is None:
            Message("HIBAÜZENET", "Adatbázis kapcsolati hiba! Ellenőrizd az internetelérésed!")
            self.window.close()
            subprocess.call(["python", "opener.py"])

        else:
            self.school = 100
            self.other = 100
            self.object = 100
            self.topic = 100
            self.gender = 100
            count = 0

            answers = [self.girlRB, self.boyRB]
            for i in range(len(answers)):
                if answers[i].isChecked() == True:
                    count += 1
                    self.gender = i

            if count != 1:
                self.nextPB.setEnabled(True)
                Message("HIBAÜZENET", "Helytelen kitöltés, próbáld újra!")

            else:
                count = 0
                answers = [self.yes2RB, self.no2RB]

                for i in range(len(answers)):
                    if answers[i].isChecked() == True:
                        self.school = i
                        count += 1

                if count != 1:
                    self.nextPB.setEnabled(True)
                    Message("HIBAÜZENET", "Helytelen kitöltés, próbáld újra!")

                else:
                    count = 0
                    answers = [self.yes3RB, self.no3RB]

                    for i in range(len(answers)):
                        if answers[i].isChecked() == True:
                            self.other = i
                            count += 1

                    if count != 1:
                        self.nextPB.setEnabled(True)
                        Message("HIBAÜZENET", "Helytelen kitöltés, próbáld újra!")

                    else:
                        count = 0
                        answers = [self.one1RB, self.two1RB, self.three1RB, self.four1RB, self.five1RB]

                        for i in range(len(answers)):
                            if answers[i].isChecked() == True:
                                self.object = i+1
                                count += 1

                        if count != 1:
                            self.nextPB.setEnabled(True)
                            Message("HIBAÜZENET", "Helytelen kitöltés, próbáld újra!")

                        else:
                            count = 0
                            answers = [self.one2RB, self.two2RB, self.three2RB, self.four2RB, self.five2RB]

                            for i in range(len(answers)):
                                if answers[i].isChecked() == True:
                                    self.topic = i+1
                                    count += 1

                            if count != 1:
                                self.nextPB.setEnabled(True)
                                Message("HIBAÜZENET", "Helytelen kitöltés, próbáld újra!")

                            else:
                                add = "insert into adatok (nev,nem,iskola,egyeb,targy,tema) values (%s,%s,%s,%s,%s,%s)"
                                cur.execute(add, (self.name,self.gender,self.school,self.other,self.object,self.topic))
                                con.commit()
                                con.close()
                                self.open_window()


    def open_window(self):
        self.window.close()
        name = self.name
        self.window = QtWidgets.QMainWindow()
        self.ui = conFilter.Continents_MainWindow(name)
        self.ui.setupUi(self.window)
        self.window.show()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Quest_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())


