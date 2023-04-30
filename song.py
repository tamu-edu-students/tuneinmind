from enum import Enum

class playStatus(Enum):
    NOT_PLAYED = 1
    PLAYING = 2
    PLAYED = 3

class Song:
    def __init__(self, songid, title, artist, mood):
        self.songid = songid
        self.title = title
        self.artist = artist 
        self.mood = mood
        self.playstatus = None