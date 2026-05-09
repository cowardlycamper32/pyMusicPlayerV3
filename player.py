from os import PathLike, listdir
import magic
import time
from just_playback import Playback


mime = magic.Magic(mime=True)
class MusicPlayer:
    def __init__(self, song_dir: str | PathLike = "/home/nova/Music/"):
        self.song_dir = song_dir
        self.player = Playback()
        self.queue = []
        self.player_head = 0
        self.load_songs()
        self.load_song()
        self.song_loaded = True
    
    def load_songs(self):
        for file in listdir(self.song_dir):
            if "audio" in mime.from_file(self.song_dir + file):
                self.queue.append(self.song_dir + file)
    
    def load_song(self):
        self.player.load_file(self.queue[self.player_head])
        self.song_loaded = True

    # basic controls
    def play(self, force = False):
        if force:
            self.load_song()
            self.player.play()
            return
        if not self.song_loaded:
            self.load_song()
            self.player.play()
        elif self.player.active:
            self.player.resume()
        else:
            self.player_head += 1
            self.player.play()

    def pause(self):
        self.player.pause()

    def stop(self):
        self.player.stop()
    
    def set_pos(self, seconds):
        self.player.seek(seconds)
    
    def next(self):
        self.player_head += 1
        self.play(True)
    
    def prev(self):
        if self.position >= 5:
            self.play(True)
        else:
            self.player_head -= 1
            self.play(True)
    
    # other weird ass functions
    @property
    def playing(self):
        return self.player.playing
    
    @property
    def position(self):
        return self.player.curr_pos
    
    @property
    def duration(self):
        return self.player.duration
    


if __name__ == "__main__":
    player = MusicPlayer()
    