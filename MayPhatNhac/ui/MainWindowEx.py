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

    def load_music(self, index):
        """Load and prepare the music track from the playlist."""
        track = self.playlist[index]
        self.player.setSource(QtCore.QUrl.fromLocalFile(track["path"]))

        self.lineEditThongBao.setText(f"Nhạc đang phát: {track['name']}")

        self.load_gif(track["gif"])

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
            if self.player.playbackState() == QtMultimedia.QMediaPlayer.PlaybackState.PausedState:

                self.player.play()
            else:

                self.load_music(self.current_index)
                self.player.play()
        else:
            self.lineEditThongBao.setText("Vui lòng chọn nhạc")

    def pause_music(self):
        """Pause the music without stopping it completely."""
        if self.player.playbackState() == QtMultimedia.QMediaPlayer.PlaybackState.PlayingState:
            self.player.pause()
            self.lineEditThongBao.setText("Tạm dừng")

    def next_track(self):
        """Switch to the next track in the playlist and update the radio button selection."""
        if self.current_index is not None:
            self.current_index = (self.current_index + 1) % len(self.playlist)
            self.load_music(self.current_index)
            self.player.play()
            self.update_radio_buttons()

    def previous_track(self):
        """Switch to the previous track in the playlist and update the radio button selection."""
        if self.current_index is not None:
            self.current_index = (self.current_index - 1) % len(self.playlist)
            self.load_music(self.current_index)
            self.player.play()
            self.update_radio_buttons()

    def change_volume(self):
        """Adjust the volume based on the slider value."""
        volume = self.verticalSlider.value() / 100
        self.audio_output.setVolume(volume)
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

    def handle_error(self, error):
        print("Error playing music:", self.player.errorString())
        self.lineEditThongBao.setText("Error playing music")

    def update_status(self, state):
        if state == QtMultimedia.QMediaPlayer.PlaybackState.PlayingState:
            self.lineEditThongBao.setText(f"Nhạc đang phát: {self.playlist[self.current_index]['name']}")
        elif state == QtMultimedia.QMediaPlayer.PlaybackState.PausedState:
            self.lineEditThongBao.setText("Tạm dừng")
        else:
            self.label.setText("Nhạc đã dừng")

    def update_duration(self, duration):
        self.horizontalSlider.setMaximum(duration)

    def update_position(self, position):
        self.horizontalSlider.setValue(position)
        # Optional: Update a label with the current time
        current_time = QtCore.QTime(0, 0).addMSecs(position)
        self.lineEditTime.setText(current_time.toString("mm:ss"))

    def set_position(self, position):
        self.player.setPosition(position)