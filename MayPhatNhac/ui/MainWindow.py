# Form implementation generated from reading ui file 'D:\TamThaiTu\MayPhatNhac\ui\MainWindow.ui'
#
# Created by: PyQt6 UI code generator 6.7.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(704, 517)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        self.label.setGeometry(QtCore.QRect(220, 80, 311, 221))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(255, 255, 255);")
        self.label.setObjectName("label")
        self.lineEditThongBao = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.lineEditThongBao.setGeometry(QtCore.QRect(190, 380, 341, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.lineEditThongBao.setFont(font)
        self.lineEditThongBao.setObjectName("lineEditThongBao")
        self.verticalSlider = QtWidgets.QSlider(parent=self.centralwidget)
        self.verticalSlider.setGeometry(QtCore.QRect(640, 120, 22, 181))
        self.verticalSlider.setOrientation(QtCore.Qt.Orientation.Vertical)
        self.verticalSlider.setObjectName("verticalSlider")
        self.groupBox = QtWidgets.QGroupBox(parent=self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(10, 80, 161, 211))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.groupBox.setFont(font)
        self.groupBox.setStyleSheet("color: rgb(255, 255, 255);")
        self.groupBox.setObjectName("groupBox")
        self.radioButtonBai1 = QtWidgets.QRadioButton(parent=self.groupBox)
        self.radioButtonBai1.setGeometry(QtCore.QRect(10, 50, 141, 20))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.radioButtonBai1.setFont(font)
        self.radioButtonBai1.setStyleSheet("color: rgb(255, 255, 255);")
        self.radioButtonBai1.setObjectName("radioButtonBai1")
        self.radioButtonBai2 = QtWidgets.QRadioButton(parent=self.groupBox)
        self.radioButtonBai2.setGeometry(QtCore.QRect(10, 100, 95, 20))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.radioButtonBai2.setFont(font)
        self.radioButtonBai2.setStyleSheet("color: rgb(255, 255, 255);")
        self.radioButtonBai2.setObjectName("radioButtonBai2")
        self.radioButtonBai3 = QtWidgets.QRadioButton(parent=self.groupBox)
        self.radioButtonBai3.setGeometry(QtCore.QRect(10, 160, 95, 20))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.radioButtonBai3.setFont(font)
        self.radioButtonBai3.setStyleSheet("color: rgb(255, 255, 255);")
        self.radioButtonBai3.setObjectName("radioButtonBai3")
        self.label_2 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(170, 10, 371, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 0, 0, 255), stop:0.166 rgba(255, 255, 0, 255), stop:0.333 rgba(0, 255, 0, 255), stop:0.5 rgba(0, 255, 255, 255), stop:0.666 rgba(0, 0, 255, 255), stop:0.833 rgba(255, 0, 255, 255), stop:1 rgba(255, 0, 0, 255));\n"
"color: rgb(255, 255, 255);")
        self.label_2.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.lineEditVolume = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.lineEditVolume.setGeometry(QtCore.QRect(610, 100, 81, 21))
        self.lineEditVolume.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"color: rgb(255, 255, 255);")
        self.lineEditVolume.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.lineEditVolume.setObjectName("lineEditVolume")
        self.horizontalSlider = QtWidgets.QSlider(parent=self.centralwidget)
        self.horizontalSlider.setGeometry(QtCore.QRect(160, 330, 461, 22))
        self.horizontalSlider.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.horizontalSlider.setObjectName("horizontalSlider")
        self.lineEditTime = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.lineEditTime.setGeometry(QtCore.QRect(62, 330, 91, 22))
        self.lineEditTime.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.lineEditTime.setObjectName("lineEditTime")
        self.toolButtonPlay = QtWidgets.QToolButton(parent=self.centralwidget)
        self.toolButtonPlay.setGeometry(QtCore.QRect(40, 430, 121, 31))
        self.toolButtonPlay.setStyleSheet("background-color: rgb(213, 213, 213);")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("./images/PlayMusic.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.toolButtonPlay.setIcon(icon)
        self.toolButtonPlay.setObjectName("toolButtonPlay")
        self.toolButtonStop = QtWidgets.QToolButton(parent=self.centralwidget)
        self.toolButtonStop.setGeometry(QtCore.QRect(210, 430, 121, 31))
        self.toolButtonStop.setStyleSheet("background-color: rgb(213, 213, 213);")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("./images/StopMusic.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.toolButtonStop.setIcon(icon1)
        self.toolButtonStop.setObjectName("toolButtonStop")
        self.toolButtonPrevious = QtWidgets.QToolButton(parent=self.centralwidget)
        self.toolButtonPrevious.setGeometry(QtCore.QRect(390, 430, 121, 31))
        self.toolButtonPrevious.setStyleSheet("background-color: rgb(213, 213, 213);")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("./images/Previous.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.toolButtonPrevious.setIcon(icon2)
        self.toolButtonPrevious.setObjectName("toolButtonPrevious")
        self.toolButtonNext = QtWidgets.QToolButton(parent=self.centralwidget)
        self.toolButtonNext.setGeometry(QtCore.QRect(550, 430, 121, 31))
        self.toolButtonNext.setStyleSheet("background-color: rgb(213, 213, 213);")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("./images/Next.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.toolButtonNext.setIcon(icon3)
        self.toolButtonNext.setObjectName("toolButtonNext")
        self.label_3 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(4, -5, 701, 471))
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap("./images/NenNhac.jpg"))
        self.label_3.setScaledContents(True)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(30, 10, 71, 61))
        self.label_4.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.label_4.setText("")
        self.label_4.setPixmap(QtGui.QPixmap("./images/TamThaiTu.jpg"))
        self.label_4.setScaledContents(True)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(290, 50, 121, 16))
        self.label_5.setStyleSheet("color: rgb(85, 255, 255);")
        self.label_5.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.label_3.raise_()
        self.label.raise_()
        self.lineEditThongBao.raise_()
        self.verticalSlider.raise_()
        self.groupBox.raise_()
        self.label_2.raise_()
        self.lineEditVolume.raise_()
        self.horizontalSlider.raise_()
        self.lineEditTime.raise_()
        self.toolButtonPlay.raise_()
        self.toolButtonStop.raise_()
        self.toolButtonPrevious.raise_()
        self.toolButtonNext.raise_()
        self.label_4.raise_()
        self.label_5.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 704, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Máy Phát Nhạc"))
        self.label.setText(_translate("MainWindow", "ảnh"))
        self.lineEditThongBao.setText(_translate("MainWindow", "Nhạc đang phát:"))
        self.groupBox.setTitle(_translate("MainWindow", "List Music:"))
        self.radioButtonBai1.setText(_translate("MainWindow", "Chúc bé ngủ ngon"))
        self.radioButtonBai2.setText(_translate("MainWindow", "Nop"))
        self.radioButtonBai3.setText(_translate("MainWindow", "Star Sky"))
        self.label_2.setText(_translate("MainWindow", "Máy Phát Nhạc"))
        self.lineEditTime.setText(_translate("MainWindow", "00:00"))
        self.toolButtonPlay.setText(_translate("MainWindow", "..."))
        self.toolButtonStop.setText(_translate("MainWindow", "..."))
        self.toolButtonPrevious.setText(_translate("MainWindow", "..."))
        self.toolButtonNext.setText(_translate("MainWindow", "..."))
        self.label_5.setText(_translate("MainWindow", "_Tam Thái Tử"))