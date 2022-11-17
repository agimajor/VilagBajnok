from PySide2.QtWidgets import QMessageBox
from mysql.connector import MySQLConnection
import mysql
from PySide2.QtGui import QIcon

def Message(title, text): #hibaüzenet a felhasználónak
        msg = QMessageBox()
        msg.setWindowTitle(title)
        msg.setIcon(QMessageBox.Warning)
        msg.setWindowIcon(QIcon('globe_world_earth_planets_chool_icon_209251.png'))
        msg.setText(text)
        msg.exec()

def Connection(): #adatbázis kapcsolat
        try:
            con = mysql.connector.connect(host="mysql.nethely.hu", user="vilagbajnokdb", password="id15112202", database="vilagbajnokdb")
            #con = mysql.connector.connect(host="localhost", user="root", password="", database="vilagbajnok")
            cur = con.cursor()

        except:
            con = None
            cur = None

        finally:
                return con, cur


def clearStr(res): #nem hivánt karakterek kiszűrése
    for char in ["(", ")", "'", ",", "[", "]"]:
        res = res.replace(char, "")
    return res




