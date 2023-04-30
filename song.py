from enum import Enum

class playStatus(Enum):
    NOT_PLAYED = 1
    PLAYING = 2
    PLAYED = 3

class Song:
    def __init__(self, song_id, title, artist, mood):
        self.song_id = song_id
        self.title = title
        self.artist = artist 
        self.mood = mood
        self.playstatus = None