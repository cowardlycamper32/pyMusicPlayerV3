from PyQt6.QtCore import QSize, QTimer, Qt
from PyQt6.QtWidgets import (
    QApplication, QWidget, QMainWindow, QPushButton, QSlider, QHBoxLayout, QVBoxLayout
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

        # buttons
        self.playButton = QPushButton()
        self.playButton.setFixedSize(QSize(64, 64))
        self.prevButton = QPushButton()
        self.prevButton.setFixedSize(QSize(48, 48))
        self.nextButton = QPushButton()
        self.nextButton.setFixedSize(QSize(48, 48))

        # interface
        self.timeline = QSlider(Qt.Orientation.Horizontal)

        # signals
        self.playButton.clicked.connect(self.toggle_playback)
        self.nextButton.clicked.connect(self.next_clicked)
        self.prevButton.clicked.connect(self.prev_clicked)
        self.timeline.sliderMoved.connect(self.seek_track)
        self.timeline.valueChanged.connect(self.autoplay_next)

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
        mainLayout.addWidget(self.timeline)

        container = QWidget()
        container.setLayout(mainLayout)
        self.setCentralWidget(container)

        self.slider_timer = QTimer()
        self.slider_timer.timeout.connect(self.update_ui)
        self.slider_timer.start(100)

        self.music.load_song()
    
    def toggle_playback(self):
        if self.music.playing:
            self.music.pause()
            self.playButton.setIcon(QIcon("icons/play.svg"))
        else:
            self.music.play()
            self.playButton.setIcon(QIcon("icons/pause.svg"))
    
    def autoplay_next(self):
        if int(self.music.position) == int(self.music.duration):
            self.music.next()

    def update_ui(self):
        if not self.timeline.isSliderDown():
            curr_pos = self.music.position
            duration = self.music.duration
            
            self.timeline.setRange(0, int(duration))
            self.timeline.setValue(int(curr_pos))
        
        
    
    def seek_track(self, value):
        self.music.set_pos(value)
    
    def next_clicked(self):
        self.music.next()
    
    def prev_clicked(self):
        self.music.prev()

        

window = MainWindow()
window.show()

app.exec()