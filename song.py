from enum import Enum

class moodCategory(Enum):
    HAPPY = 1
    SAD = 2
    ANGRY = 3
    RELAXED = 4

class playStatus(Enum):
    NOT_PLAYED = 1
    PLAYING = 2
    PLAYED = 3

class Song:
    def __init__(self):
        self.title = None
        self.artist = None 
        self.mood = None 
        self.playstatus = None