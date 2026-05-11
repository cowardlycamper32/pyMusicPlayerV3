import mutagen.mp3
from mutagen.mp3 import EasyMP3
from mutagen.id3 import ID3, TIT2, TPE1
from mutagen.easyid3 import EasyID3

class ReadTags:
    def __init__(self, songList: list[str]):
        self.songList = songList
        for i in songList:
            try:
                tags = EasyMP3(i)
                songID3 = ID3(i)

                print(f"{i.split("/")[-1]} tags: {tags}")
                if tags is None or tags == {}:
                    print(f"{i.split("/")[-1]} tags: None")
                    song_filename = i.split("/")[-1]
                    if " by " in song_filename:
                        temp = song_filename.split(" by ")
                    elif " | " in song_filename:
                        temp = song_filename.split(" | ")

                    else:
                        if "\"" in song_filename:
                            temp = song_filename.split("\"")
                            if len(temp) == 3:
                                temp = temp[1]
                        else:
                            temp = song_filename

                    if type(temp) == list:
                        temp2 = temp[-1].split("[")
                        temp3 = temp2[0].split("]")
                        splits = [temp[0], "".join((temp3[0], temp2[1]))]
                        print(f"attempting list to tags on {splits}")
                        songID3.add(TIT2(encoding=3, text=u''+splits[0]+''))
                        songID3.add(TPE1(encoding=3, text=u''+splits[1]+''))
                    else:
                        temp2 = temp.split("[")
                        temp3 = temp2[0].split("]")
                        splits = "".join((temp2[0], temp3[-1]))
                        print(f"attempting str to tag on {splits}")
                        songID3.add(TIT2(encoding=3, text=u''+splits+''))
                    songID3.save(i)
            except mutagen.mp3.HeaderNotFoundError:
                print(f"file {i.split('/')[-1]} has no tags or is corrupted")
    def printTags(self, path):
        tags = EasyMP3(path)
        return f"{path.split('/')[-1]} tags: {tags}"





if __name__ == "__main__":
    tagReader = ReadTags(["/home/nova/Music/DEEP SLEEP - POPPY PLAYTIME 3 SONG [vKVttC2S7vE].mp3","/home/nova/Music/DOORS FLOOR 2 ANIMATED SONG \uff5c Rockit Music [ODPm7hjFwP4].mp3","/home/nova/Music/The Living Tombstone - \uff02Rust\uff02 Visualizer [frKg1m5L-CY].mp3","/home/nova/Music/Mick Gordon - 08. Flesh & Metal [VYVFXYEm_Mw].mp3","/home/nova/Music/Gravity [Wynimbmwg3k].mp3","/home/nova/Music/As It Is, Set It Off & JordyPurp - IN THREES [uPEEZuFbT3o].mp3","/home/nova/Music/Imagine Dragons - Natural [0I647GU3Jsc].mp3"])
