from PyQt6 import QtCore, QtWidgets, QtGui
import pygame
import os
from MainWindow import Ui_MainWindow

class MainWindowEx(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # Khởi tạo pygame
        pygame.mixer.init()

        self.label.setScaledContents(True)

        self.playlist = [
            {"name": "Chúc Bé Ngủ Ngon - Piano", "path": "./music/ChucBeNguNgon-Piano-4128737.mp3",
             "gif": "./images/PhatNhac1.gif"},
            {"name": "Nop - Chen Yue Long", "path": "./music/Nop-ChenYueLong-8917890.mp3",
             "gif": "./images/PhatNhac2.gif"},
            {"name": "Star Sky - TwoStepsFromHell", "path": "./music/StarSky-TwoStepsFromHell-3897684.mp3",
             "gif": "./images/PhatNhac3.gif"}
        ]

        self.current_index = None

        self.lineEditThongBao.setText("Vui lòng chọn nhạc")
        self.label.setText("Vui lòng chọn nhạc")

        # Kết nối các nút điều khiển
        self.toolButtonPlay.clicked.connect(self.play_music)
        self.toolButtonNext.clicked.connect(self.next_track)
        self.toolButtonPrevious.clicked.connect(self.previous_track)
        self.toolButtonStop.clicked.connect(self.pause_music)
        self.verticalSlider.valueChanged.connect(self.change_volume)

        self.radioButtonBai1.toggled.connect(lambda: self.select_track(0))
        self.radioButtonBai2.toggled.connect(lambda: self.select_track(1))
        self.radioButtonBai3.toggled.connect(lambda: self.select_track(2))

        self.verticalSlider.setValue(50)
        pygame.mixer.music.set_volume(0.5)

    def load_music(self, index):
        """Load and prepare the music track from the playlist."""
        track = self.playlist[index]
        file_path = track["path"]

        if os.path.exists(file_path):
            pygame.mixer.music.load(file_path)
            print(f"Playing file: {file_path}")

            self.lineEditThongBao.setText(f"Nhạc đang phát: {track['name']}")
            self.load_gif(track["gif"])
        else:
            print(f"File not found: {file_path}")
            self.lineEditThongBao.setText("File không tồn tại")

    def load_gif(self, gif_path):
        """Load and start the GIF animation on the label."""
        if os.path.exists(gif_path):
            gif = QtGui.QMovie(gif_path)
            if gif.isValid():
                self.label.setMovie(gif)
                gif.start()
            else:
                print("Error: Cannot display GIF")
                self.label.clear()
        else:
            print("GIF file not found:", gif_path)
            self.label.clear()

    def play_music(self):
        """Play or resume the selected music track."""
        if self.current_index is not None:
            if pygame.mixer.music.get_busy():
                pygame.mixer.music.unpause()
            else:
                self.load_music(self.current_index)
                pygame.mixer.music.play()
        else:
            self.lineEditThongBao.setText("Vui lòng chọn nhạc")

    def pause_music(self):
        """Pause the music without stopping it completely."""
        if pygame.mixer.music.get_busy():
            pygame.mixer.music.pause()
            self.lineEditThongBao.setText("Tạm dừng")

    def next_track(self):
        """Switch to the next track in the playlist and update the radio button selection."""
        if self.current_index is not None:
            self.current_index = (self.current_index + 1) % len(self.playlist)
            self.load_music(self.current_index)
            pygame.mixer.music.play()
            self.update_radio_buttons()

    def previous_track(self):
        """Switch to the previous track in the playlist and update the radio button selection."""
        if self.current_index is not None:
            self.current_index = (self.current_index - 1) % len(self.playlist)
            self.load_music(self.current_index)
            pygame.mixer.music.play()
            self.update_radio_buttons()

    def change_volume(self):
        """Adjust the volume based on the slider value."""
        volume = self.verticalSlider.value() / 100
        pygame.mixer.music.set_volume(volume)
        self.lineEditVolume.setText(f"{self.verticalSlider.value()}%")

    def select_track(self, index):
        if self.sender().isChecked():
            self.current_index = index
            self.load_music(self.current_index)

    def update_radio_buttons(self):
        if self.current_index == 0:
            self.radioButtonBai1.setChecked(True)
        elif self.current_index == 1:
            self.radioButtonBai2.setChecked(True)
        elif self.current_index == 2:
            self.radioButtonBai3.setChecked(True)
