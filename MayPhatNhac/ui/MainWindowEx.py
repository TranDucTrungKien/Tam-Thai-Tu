from PyQt6 import QtCore, QtWidgets, QtMultimedia, QtGui
import os
from MainWindow import Ui_MainWindow

class MainWindowEx(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.audio_output = QtMultimedia.QAudioOutput()
        self.player = QtMultimedia.QMediaPlayer()
        self.player.setAudioOutput(self.audio_output)

        self.label.setScaledContents(True)

        self.playlist = [
            {"name": "Chúc Bé Ngủ Ngon - Piano", "path": r"C:\Users\kien0\Music\ChucBeNguNgon-Piano-4128737.mp3",
             "gif": r"C:\Users\kien0\OneDrive - zxcvb\Pictures\Templates\PhatNhac1.gif"},
            {"name": "Nop - Chen Yue Long", "path": r"C:\Users\kien0\Music\Nop-ChenYueLong-8917890.mp3",
             "gif": r"C:\Users\kien0\OneDrive - zxcvb\Pictures\Templates\PhatNhac2.gif"},
            {"name": "Star Sky - TwoStepsFromHell",
             "path": r"C:\Users\kien0\Music\StarSky-TwoStepsFromHell-3897684.mp3",
             "gif": r"C:\Users\kien0\OneDrive - zxcvb\Pictures\Templates\PhatNhac3.gif"}
        ]
        self.current_index = None