from os import PathLike, listdir
import time
from just_playback import Playback



class MusicPlayer:
    def __init__(self, song_dir: str | PathLike = "/home/nova/Music/"):
        self.songDir = song_dir
        self.player = Playback()
        self.queue = []
        self.HEAD = 0
        self.loadSongs()
        self.songLoaded = False
    
    def loadSongs(self):
        for file in listdir(self.songDir):
            self.queue.append(self.songDir + file)
    
    def loadSong(self):
        self.player.load_file(self.queue[self.HEAD])
        self.songLoaded = True

    # basic controls
    def play(self):
        if not self.songLoaded:
            self.loadSong()
        self.player.play()

    def pause(self):
        self.player.pause()

    def stop(self):
        self.player.stop()
    
    def set_pos(self, seconds):
        self.player.seek(seconds)
    
    # other weird ass functions
    
    def is_playing(self):
        return self.player.playing
    
    def get_position(self):
        return self.player.curr_pos
    
    def get_duration(self):
        return self.player.duration
    


if __name__ == "__main__":
    player = MusicPlayer()
    