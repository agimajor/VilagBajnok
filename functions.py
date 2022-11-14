from PySide2.QtWidgets import QMessageBox
import PySide2.QtWidgets as QtWidgets
from mysql.connector import MySQLConnection
import mysql


def Message(title, text):
        msg = QMessageBox()
        msg.setWindowTitle(title)
        msg.setIcon(QMessageBox.Warning)
        msg.setText(text)
        msg.exec()

def Connection():
        try:
            
            #con = mysql.connector.connect(host="localhost", user="root", password="", database="vilagbajnok")
            con = mysql.connector.connect(host="sql7.freemysqlhosting.net", user="sql7550831", password="DRpXDuHP1i", database="sql7550831")
            cur = con.cursor()
        except:

            con = None
            cur = None

        finally:
                return con, cur


def clearStr(res):
    for char in ["(", ")", "'", ",", "[", "]"]:
        res = res.replace(char, "")
    return res


