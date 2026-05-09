from PyQt6.QtCore import QSize
from PyQt6.QtWidgets import (
    QApplication, QWidget, QMainWindow, QPushButton, QProgressBar, QHBoxLayout, QVBoxLayout
)
from PyQt6.QtGui import QIcon
from player import MusicPlayer

app = QApplication([])

class MainWindow(QMainWindow):
    def __init__(self):
        # basic window config
        super().__init__()
        self.setMinimumSize(QSize(500, 500))
        self.resize(750, 750)
        self.setWindowTitle("pyMusicPlayerV3")
        # self.setWindowIcon("placeholder")

        self.music = MusicPlayer()
        

        # stylesheet
        with open("stylesheet.qss", "r") as stylesheet:
            self.setStyleSheet(stylesheet.read())

        # states
        self.playState = False

        # buttons
        self.playButton = QPushButton()
        self.playButton.setFixedSize(QSize(64, 64))
        self.prevButton = QPushButton()
        self.prevButton.setFixedSize(QSize(48, 48))
        self.nextButton = QPushButton()
        self.nextButton.setFixedSize(QSize(48, 48))

        # interface
        self.progressBar = QProgressBar()

        # set button displays
        self.playButton.setIcon(QIcon("icons/play.svg"))
        self.playButton.setIconSize(QSize(64, 64))

        self.prevButton.setIcon(QIcon("icons/previous.svg"))
        self.prevButton.setIconSize(QSize(48, 48))

        self.nextButton.setIcon(QIcon("icons/next.svg"))
        self.nextButton.setIconSize(QSize(48, 48))

        # layout
        btnLayout = QHBoxLayout()
        btnLayout.addWidget(self.prevButton)
        btnLayout.addWidget(self.playButton)
        btnLayout.addWidget(self.nextButton)
        btnLayout.setSpacing(8)
        btnLayout.setContentsMargins(16, 8, 16, 8)

        mainLayout = QVBoxLayout()
        mainLayout.addLayout(btnLayout)
        mainLayout.addWidget(self.progressBar)

        container = QWidget()
        container.setLayout(mainLayout)
        self.setCentralWidget(container)
    
    def toggle_playback(self):
        if self.music.is_playing:
            self.music.pause()
            self.playButton.setIcon(QIcon("icons/pause.svg"))
        else:
            self.music.play()
            self.playButton.setIcon(QIcon("icons/play.svg"))
    
    def update_ui(self):
        curr_pos = self.music.get_position
        duration = self.music.get_duration
        
        self.progressBar.setRange(0, int(duration))
        self.progressBar.setValue(int(curr_pos))

        

window = MainWindow()
window.show()

app.exec()