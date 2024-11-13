import sys
from PyQt6.QtWidgets import QApplication, QMainWindow
from MainWindow import Ui_MainWindow
import math


class MainWindowEx(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # Variable to store the previous result
        self.last_result = ""

        # Connecting buttons to their respective functions
        self.pushButton0.clicked.connect(lambda: self.add_input("0"))
        self.pushButton1.clicked.connect(lambda: self.add_input("1"))
        self.pushButton2.clicked.connect(lambda: self.add_input("2"))
        self.pushButton3.clicked.connect(lambda: self.add_input("3"))
        self.pushButton4.clicked.connect(lambda: self.add_input("4"))
        self.pushButton5.clicked.connect(lambda: self.add_input("5"))
        self.pushButton6.clicked.connect(lambda: self.add_input("6"))
        self.pushButton7.clicked.connect(lambda: self.add_input("7"))
        self.pushButton8.clicked.connect(lambda: self.add_input("8"))
        self.pushButton9.clicked.connect(lambda: self.add_input("9"))
        self.pushButtoncong.clicked.connect(lambda: self.add_input("+"))
        self.pushButtontru.clicked.connect(lambda: self.add_input("-"))
        self.pushButtonnhan.clicked.connect(lambda: self.add_input("*"))
        self.pushButtonchia.clicked.connect(lambda: self.add_input("/"))
        self.pushButtoncham.clicked.connect(lambda: self.add_input("."))
        self.pushButtonNgoacTrair.clicked.connect(lambda: self.add_input("("))
        self.pushButtonNgoacPhai.clicked.connect(lambda: self.add_input(")"))
        self.pushButtonMu.clicked.connect(lambda: self.add_input("**"))

        self.pushButtonSQRT.clicked.connect(self.calculate_sqrt)
        self.pushButtonBang.clicked.connect(self.calculate_result)
        self.pushButtonAC.clicked.connect(self.clear_all)
        self.pushButtonDEL.clicked.connect(self.delete_last)
        self.pushButtoANS.clicked.connect(self.use_last_result)
        self.pushButtoOFF.clicked.connect(self.close)

    def add_input(self, value):
        current_text = self.lineEditKq.text()
        self.lineEditKq.setText(current_text + value)

    def calculate_sqrt(self):
        try:
            expression = self.lineEditKq.text()
            result = math.sqrt(float(expression))
            self.lineEditKq.setText(str(result))
            self.last_result = str(result)
        except Exception as e:
            self.lineEditKq.setText("Error")

    def calculate_result(self):
        try:
            expression = self.lineEditKq.text()
            result = eval(expression)
            self.lineEditKq.setText(str(result))
            self.last_result = str(result)
        except Exception as e:
            self.lineEditKq.setText("Error")

    def clear_all(self):
        self.lineEditKq.clear()

    def delete_last(self):
        current_text = self.lineEditKq.text()
        self.lineEditKq.setText(current_text[:-1])

    def use_last_result(self):
        self.lineEditKq.setText(self.lineEditKq.text() + self.last_result)



