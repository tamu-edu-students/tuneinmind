from enum import Enum

class UserMood(Enum):
    HAPPY = 1
    SAD = 2
    ANGRY = 3
    RELAXED = 4    

class User:
    def _init_(self):
        self.name = None
        self.session_id = None
        self.current_mood = None 

    def selectSongFromPopularSongs():
        '''Select a song to play from the list of Popular Songs'''
        pass

    def selectSongFromRecommendedSongs():
        '''Select a song to play from the list of Recommended Songs'''
        pass

    def deleteSongFromCurrentSession():
        '''Deleting a song from current session, 
        this requires a refresh of recommendations as the session changes'''
        pass

    def enableMoodRecommendations():
        '''The user interface provides the user with a Toggle button
         To enable the Mood based Recommendation system
         This requires a refresh of recommendations'''
        pass

    def disableMoodRecommendations():
        '''The user interface provides the user with a Toggle button
         To disable the Mood based Recommendation system
         This requires a refresh of recommendations'''
        pass

    def startSession():
        '''The user is starting a fresh session
        Verify if the session variables are cleared'''
        pass

    def endSession():
        '''The user decides to end the current session
        Clear all the session variables'''
        pass