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

        self.lineEditThongBao.setText("Vui lòng chọn nhạc")
        self.label.setText("Vui lòng chọn nhạc")

        self.toolButtonPlay.clicked.connect(self.play_music)
        self.toolButtonNext.clicked.connect(self.next_track)
        self.toolButtonPrevious.clicked.connect(self.previous_track)
        self.toolButtonStop.clicked.connect(self.pause_music)
        self.verticalSlider.valueChanged.connect(self.change_volume)

        self.radioButtonBai1.toggled.connect(lambda: self.select_track(0))
        self.radioButtonBai2.toggled.connect(lambda: self.select_track(1))
        self.radioButtonBai3.toggled.connect(lambda: self.select_track(2))

        self.player.errorOccurred.connect(self.handle_error)
        self.player.playbackStateChanged.connect(self.update_status)

        self.verticalSlider.setValue(50)
        self.audio_output.setVolume(0.5)

        self.horizontalSlider.sliderMoved.connect(self.set_position)
        self.player.positionChanged.connect(self.update_position)
        self.player.durationChanged.connect(self.update_duration)