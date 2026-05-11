from os import PathLike, listdir
from os.path import exists
import json
import magic
import time
from just_playback import Playback

import tags

mime = magic.Magic(mime=True)
class MusicPlayer:
    def __init__(self, song_dir: str | PathLike = "/home/nova/Music/"):
        self.song_dir = song_dir
        self.player = Playback()
        self.queue = []
        self.player_head = 0
        self.load_songs()
        self.tagReader = tags.ReadTags(self.queue)
        self.load_song()
        self.song_loaded = True
    
    def load_songs(self):
        dbFile = open("songs.json", "a+")
        dbData = dbFile.read()
        print(len(dbData))
        if (len(dbData) == 0 or dbData == '') and False:
            print("database is empty")
            dbFile.write("[\n\n]")
            dbData = dbFile.read()
        dbFile.close()
        with open("songs.json") as f:
            db = json.load(f)
        for file in listdir(self.song_dir):
            if self.song_dir + file not in db:
                print(f"song {file} not in database")
                db.append(self.song_dir + file)
                if "audio" in mime.from_file(self.song_dir + file):
                    self.queue.append(self.song_dir + file)
            else:
                self.queue.append(self.song_dir + file)
        json.dump(db, open("songs.json", "w+"), indent=4)

    
    def load_song(self):
        self.player.load_file(self.queue[self.player_head])
        self.song_loaded = True

    # basic controls
    def play(self, force = False):
        print(f"{self.tagReader.printTags(self.queue[self.player_head])}")
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
    