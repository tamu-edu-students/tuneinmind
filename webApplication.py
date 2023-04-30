import csv
from enum import Enum
from song import Song

class moodCategory(Enum):
    HAPPY = 1
    SAD = 2
    ANGRY = 3
    RELAXED = 4

mood_dict = {'0':'happy', '1':'angry', '2':'sad', '3':'relaxed'}

class SessionStatus(Enum):
    INACTIVE = 1
    ACTIVE = 2
    TERMINATED = 3

class webApplication:
    def __init__(self):
        self.session_id = None
        self.session_status = SessionStatus.ACTIVE
        self.currentSession = []
        self.popularSongs = []
        self.allSongs = []
    
    def loadSongs(self):
        '''Reads the alldata.csv songs dataset
            Stores the required song attributes in song object
        '''
        with open('alldata.csv', newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            songs = [row for row in reader]
        
        #create song objects
        for song in songs:
            songid = song['song_id']
            title = song['title']
            artist = song['a_name'] 
            mood = mood_dict[song['mood']]
            songObject = Song(songid,title, artist, mood)
            self.allSongs.append(songObject)

        return self.allSongs

    def selectSongFromPopularSongs(self):
        '''Select a song to play from the list of Popular Songs
         This deleted the song from popular songs list
         Adds that song to the current session
         
         Returns:
            current session, Popular Songs, Recommended Songs'''
        pass

    def selectSongFromRecommendedSongs(self):
        '''Select a song to play from the list of Recommended Songs
        '''
        pass

    def deleteSongFromCurrentSession(self):
        '''Deleting a song from current session, 
        this requires a refresh of recommendations as the session changes'''
        pass

    def enableMoodRecommendations(self):
        '''The user interface provides the user with a Toggle button
         To enable the Mood based Recommendation system
         This requires a refresh of recommendations'''
        pass

    def disableMoodRecommendations():
        '''The user interface provides the user with a Toggle button
         To disable the Mood based Recommendation system
         This requires a refresh of recommendations
         
         Returns:
            '''
        pass

    def startSession():
        '''The user is starting a fresh session
        Verify if the session variables are cleared

        Returns: 
            Current Session(empty), Popular Songs, Recommended Songs'''
        pass

    def endSession():
        '''The user decides to end the current session
        Clear all the session variables'''
        pass

    def generatePopularSongs(self):
        '''Top 50 song recommendations containing a distribution of Happy, Sad, Relaxed and Angry songs'''
        pass

    def addToCurrentSession(self):
        '''When user selects a new song to play, it needs to be added to the current session'''
        pass

    def deleteFromCurrentSession(self):
        '''To delete a song which is displayed in the current session.
        This is to handle unintended song plays by the user and understand the recommendations better with updates to current session'''
        pass

    def generateRecommendations(self):
        '''Whenever there is an update to the current session, recommendations need to be refreshed
        This function is called in all such cases'''
        pass

    def updatePopularSongs(self):
        '''Whenever a song is selected from popular songs listed, that song needs to be deleted and refreshed'''
        pass
    
    def terminateSession(self):
        '''In case where user chooses to terminate the session, the session related information needs to be cleared'''
        pass
