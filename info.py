
import PySide2.QtWidgets as QtWidgets
# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'infoqljEHR.ui'
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
import subprocess
import opener

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        self.window = MainWindow
        self.window.setWindowIcon(QIcon('globe_world_earth_planets_chool_icon_209251.png'))
        MainWindow.resize(932, 520)
        MainWindow.setStyleSheet(u"border-color: rgb(210, 210, 210);\n"
"background-color: rgb(210, 210, 210);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.felulet = QFrame(self.centralwidget)
        self.felulet.setObjectName(u"felulet")
        self.felulet.setFrameShape(QFrame.StyledPanel)
        self.felulet.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.felulet)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.szovegTB = QTextBrowser(self.felulet)
        self.szovegTB.setObjectName(u"szovegTB")
        self.szovegTB.setStyleSheet(u"font: 75 18px \"MS Shell Dlg 2\";\n"
"background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.506, stop:0 rgba(255, 255, 0, 255), stop:1 rgba(210, 210, 210, 210));")

        self.gridLayout_2.addWidget(self.szovegTB, 0, 0, 1, 1)


        self.gridLayout.addWidget(self.felulet, 0, 0, 1, 1)

        self.visszaPB = QPushButton(self.centralwidget)
        self.visszaPB.setObjectName(u"visszaPB")
        self.visszaPB.setMinimumSize(QSize(0, 50))
        self.visszaPB.setStyleSheet(u"font: 75 26px \"MS Shell Dlg 2\";\n"
"background-color: rgb(255, 255, 0);")

        self.gridLayout.addWidget(self.visszaPB, 1, 0, 1, 1)

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
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"VilágBajnok", None))
        self.szovegTB.setHtml(QCoreApplication.translate("MainWindow",
                                                             u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                                             "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                                             "p, li { white-space: pre-wrap; }\n"
                                                             "</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:18px; font-weight:72; font-style:normal;\">\n"
                                                             "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt; font-weight:400;\">Szia! </span></p>\n"
                                                             "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:9pt; font-weight:400;\"><br /></p>\n"
                                                             "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt; font-weight:400;\">\u00dcdv\u00f6z\u00f6llek a </span><span style=\" font-size:9pt; font-weight:600; text-decoration: underline;\">Vil\u00e1gBajnok<"
                                                             "/span><span style=\" font-size:9pt; font-weight:400;\"> j\u00e1t\u00e9kban! El\u0151sz\u00f6r is had mutatkozzak be neked. Major \u00c1gnesnek h\u00edvnak \u00e9s \u00e9n vagyok a j\u00e1t\u00e9k meg\u00e1lmod\u00f3ja \u00e9s megval\u00f3s\u00edt\u00f3ja is. Maga a j\u00e1k\u00e9k a 7-8 oszt\u00e1lyosok sz\u00e1m\u00e1ra sz\u00f3l\u00f3 Oktat\u00e1si Hivatal \u00e1ltal 2021/2022 \u00e9s 2022/2023 tan\u00e9vekre kiadott F\u00f6ldrajz tank\u00f6nyveket dolgozza fel  \u00e9s seg\u00edt a tud\u00e1sod meger\u0151s\u00edt\u00e9s\u00e9ben, illetve elm\u00e9ly\u00edt\u00e9s\u00e9ben. &quot;Innen m\u00e1r csak egy karny\u00fajt\u00e1s a F\u00f6ldrajz 5-\u00f6s.&quot;</span></p>\n"
                                                             "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt; font-weight:400;\">A j\u00e1t\u00e9kot igyekeztem a lehet\u0151 leglogikusabb \u00e9s legegyszer\u0171bben kivitelezni, hogy egy\u00e9rtelm\u0171 legyen az haszn\u00e1lata, viszont n\u00e9h\u00e1"
                                                             "ny ir\u00e1nymutat\u00e1st hozok a j\u00e1t\u00e9k menet\u00e9nek megismer\u00e9s\u00e9hez:</span></p>\n"
                                                             "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:9pt; font-weight:400;\"><br /></p>\n"
                                                             "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:9pt; font-weight:400;\"><br /></p>\n"
                                                             "<ul style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 1;\"><li style=\" font-size:9pt; font-weight:400; background-color:transparent;\" style=\" margin-top:0px; margin-bottom:0px; margin-left:24px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:18px;\">Els\u0151 haszn\u00e1lat el\u0151tt k\u00f6telez\u0151 a regisztr\u00e1ci\u00f3.</span></li>\n"
                                                             "<li style=\" font-size:9pt; font-weight:400; background-color:transparent;\" style=\" margin-top:0"
                                                             "px; margin-bottom:0px; margin-left:24px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:18px;\">Bejelentkez\u00e9st k\u00f6vet\u0151en a k\u00e9rd\u00e9sk\u00f6r sz\u0171r\u00e9s\u00e9hez jutsz el, ezt \u00e9rtelemszer\u0171en az adott kontinens nev\u00e9t\u00a0tartalmaz\u00f3 gomb megnyom\u00e1s\u00e1val alkalmazhatod.</span></li>\n"
                                                             "<li style=\" font-size:9pt; font-weight:400; background-color:transparent;\" style=\" margin-top:0px; margin-bottom:0px; margin-left:24px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:18px;\">A k\u00e9rd\u00e9sekn\u00e9l megjel\u00f6lve az \u00e1ltalad helyesnek \u00edt\u00e9lt v\u00e1laszt k\u00f6vet\u0151en a Tov\u00e1bb gomb seg\u00edts\u00e9g\u00e9vel juthatsz el a k\u00f6vet\u0151 k\u00e9rd\u00e9sig, \u00edgy haladva az utols\u00f3ig, majd egyb\u0151l l\u00e1tod az eredm\u00e9nyt is.</span></li>\n"
                                                             "<li style=\" font-size:9pt; font-weight:400; background-color:transparent;\" style=\" margin-top:0px; mar"
                                                             "gin-bottom:0px; margin-left:24px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:18px;\">Fontosnak tartom megeml\u00edteni, hogy a tesztek k\u00e9rd\u00e9sbankkal dolgoznak, \u00edgy \u00e9rdemes 1-1 p\u00e1ly\u00e1t t\u00f6bbsz\u00f6r is kij\u00e1tszani, hiszen \u00faj k\u00e9rd\u00e9sek jelenhetnek meg.</span></li>\n"
                                                             "<li style=\" font-size:9pt; font-weight:400; background-color:transparent;\" style=\" margin-top:0px; margin-bottom:0px; margin-left:24px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:18px;\">Adott Kontinensen gy\u0171jt\u00f6tt eredm\u00e9nyeidet egy diagramm seg\u00edts\u00e9g\u00e9vel is \u00e1ttekintheted a k\u00f6r\u00f6k v\u00e9g\u00e9n.</span></li>\n"
                                                             "<li style=\" font-size:9pt; font-weight:400; background-color:transparent;\" style=\" margin-top:0px; margin-bottom:0px; margin-left:24px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:18px;\">Ha m\u00e1r van lej\u00e1tszott k\u00f6"
                                                             "r\u00f6d a sz\u0171r\u0151 mez\u0151re visszat\u00e9rve k\u00fcl\u00f6nb\u00f6z\u0151 ikonok jel\u00f6lik az el\u0151rehalad\u00e1sid (👣\u00a0- m\u00e1r pr\u00f3b\u00e1lkozt\u00e1l a tesztel, de az eredm\u00e9ny m\u00e9g nem az igazi, 🚩 \u00a0- sikeresen elfoglaltad a ter\u00fcletet, sz\u00e9p teljes\u00edtm\u00e9ny, viszont a gyakorl\u00e1s ilyenkor sem \u00e1rt).\u00a0</span></li>\n"
                                                             "<li style=\" font-size:9pt; font-weight:400; background-color:transparent;\" style=\" margin-top:0px; margin-bottom:0px; margin-left:24px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:18px;\">V\u00e9g\u00fcl pedig szeretnem megeml\u00edteni, hogy egy weboldal is l\u00e9trej\u00f6tt a j\u00e1t\u00e9khoz, hogy ezzel is \u00f6szt\u00f6n\u00f6zve a min\u00e9l t\u00f6bb \u00e9s jobb eredm\u00e9nyt, amit a </span><span style=\" font-size:18px; font-weight:600;\">https://vilagbajnok.000webhostapp.com/ </span><span style=\" font-size:18px;\">c\u00edmen tudtok el\u00e9rni.</span></li></ul>\n"
                                                             "<p style="
                                                             "\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:24px; margin-right:0px; -qt-block-indent:1; text-indent:0px; font-size:9pt; font-weight:400; background-color:transparent;\"><br /></p>\n"
                                                             "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:24px; margin-right:0px; -qt-block-indent:1; text-indent:0px; font-size:9pt; font-weight:400; background-color:transparent;\"><br /></p>\n"
                                                             "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt; font-weight:400;\">Tov\u00e1bbi k\u00e9rd\u00e9sek\u00e9rt b\u00e1tran fordulj hozz\u00e1m a </span><span style=\" font-size:9pt; font-weight:600; text-decoration: underline;\">magnes026@gmail.com</span><span style=\" font-size:9pt; font-weight:400;\"> e-mail c\u00edmen.</span></p>\n"
                                                             "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9p"
                                                             "t; font-weight:400;\">Kellemes j\u00e1t\u00e9kot \u00e9s egyben tanul\u00e1st k\u00edv\u00e1nok! </span></p>\n"
                                                             "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:24px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:9pt; font-weight:400; background-color:transparent;\"><br /></p>\n"
                                                             "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:24px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:transparent;\"><span style=\" font-size:9pt; font-weight:400; background-color:transparent;\">\u00dcdv, \u00c1gi </span></p>\n"
                                                             "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:9pt; font-weight:400;\"><br /></p>\n"
                                                             "<p dir='rtl' style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'Calibri,Calibri_MSFontService,sans-serif'; font-size:9pt; font"
                                                             "-weight:400; color:#000000;\"><br /></p></body></html>",
                                                             None))
        self.visszaPB.setText(QCoreApplication.translate("MainWindow", u"Vissza", None))
    # retranslateUi
        self.visszaPB.clicked.connect(self.openUdv)


    def openUdv(self):
        self.visszaPB.setEnabled(False)
        self.window.close()
        self.window = QtWidgets.QMainWindow()
        self.ui = opener.HomePage_MainWindow()
        self.ui.setupUi(self.window)
        self.window.show()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    MainWindow.setWindowIcon(QIcon('globe_world_earth_planets_chool_icon_209251.png'))
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
