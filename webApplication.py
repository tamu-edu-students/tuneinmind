import csv
from enum import Enum
from song import Song
from model import SessionOutput
import pandas as pd

sessionOutput = SessionOutput(use_lyrics=True, session_length=3, session_songIDs=[0, 1, 2])

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
        self.currentSessionSongs = []
        self.popularSongs = []
        self.allSongs = []
        self.recommendedSongs = []
        self.currentlyPlaying = None
        self.currentlyPlayedSong = []
        self.sessionThreshold = 5
        self.lyricsToggle = True
        self.loadSongs()

    def reset(self):
        self.session_id = None
        self.session_status = SessionStatus.ACTIVE
        self.currentSessionSongs = []
        self.popularSongs = []
        self.allSongs = []
        self.recommendedSongs = []
        self.currentlyPlaying = None
        self.currentlyPlayedSong = []
        self.sessionThreshold = 5
        self.lyricsToggle = True
        self.loadSongs()
    
    def loadSongs(self):
        '''Reads the alldata.csv songs dataset
            Stores the required song attributes in song object
        '''
        with open('alldata_normalized.csv', newline='', encoding='utf-8') as csvfile:
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

    def selectSongFromPopularSongs(self, song_id):
        '''Select a song to play from the list of Popular Songs
         This deleted the song from popular songs list
         Adds that song to the current session         
         Returns:
            current session, Popular Songs, Recommended Songs'''

        # self.updatePopularSongs(song_id)
        # self.addToCurrentSession(song_id)

    def selectSongFromRecommendedSongs(self, song_id):
        '''Select a song to play from the list of Recommended Songs
        '''
        # self.updatePopularSongs(song_id)
        # self.addToCurrentSession(song_id)

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

    # popular songs calculation- return 51 popular songs [12, 13, 13, 13]
    # sort top songs based on spotify acoustic values(happy, sad, angry, relaxed)
    def generatePopularSongs(self):
        '''Top 50 song recommendations containing a distribution of Happy, Sad, Relaxed and Angry songs'''
        df = pd.read_csv('alldata_normalized.csv')
        filtered_df_happy = df[df['mood'] == 0]
        sorted_df_happy = filtered_df_happy.sort_values(by='spot_happy', ascending=False).head(12)

        filtered_df_angry = df[df['mood'] == 1]
        sorted_df_angry = filtered_df_angry.sort_values(by='spot_angry', ascending=False).head(13)

        filtered_df_sad = df[df['mood'] == 2]
        sorted_df_sad = filtered_df_sad.sort_values(by='spot_sad', ascending=False).head(13)

        filtered_df_relaxed = df[df['mood'] == 3]
        sorted_df_relaxed = filtered_df_relaxed.sort_values(by='spot_relaxed', ascending=False).head(13)

        # Shuffle the concatenated dataframe
        df_concat = pd.concat([sorted_df_happy, sorted_df_angry, sorted_df_sad, sorted_df_relaxed], ignore_index=True)
        df_shuffled = df_concat.sample(frac=1).reset_index(drop=True)

        self.popularSongs = df_shuffled['song_id'].tolist()

        return [song for song in self.allSongs if int(song.song_id) in self.popularSongs]

    def addToCurrentSession(self, song_id):
        '''When user selects a new song to play, it needs to be added to the current session'''
        self.currentSessionSongs.append(song_id)
        self.currentlyPlaying = self.currentSessionSongs[len(self.currentSessionSongs)-1]
        self.currentlyPlayedSong = [song for song in self.allSongs if int(song.song_id) == int(self.currentlyPlaying)][0]
        # print('See Here for current session songs', self.currentSessionSongs)
        # if len(self.currentSessionSongs) > self.sessionThreshold:
        #     self.generateRecommendations()
        

    def deleteFromCurrentSession(self):
        '''To delete a song which is displayed in the current session.
        This is to handle unintended song plays by the user and understand the recommendations better with updates to current session'''
        pass

    def generateRecommendations(self):
        '''Whenever there is an update to the current session, recommendations need to be refreshed
        This function is called in all such cases'''

        # print("calling recommendations function")
        # print("Now the lyrics toggle is ", self.lyricsToggle)
        sessionOutput = SessionOutput(use_lyrics= self.lyricsToggle, session_length=3, session_songIDs= self.currentSessionSongs)
        self.recommendedSongs = sessionOutput.recommend_songs()

        return [song for song in self.allSongs if int(song.song_id) in self.recommendedSongs]
        
    def updatePopularSongs(self, song_id):
        '''Whenever a song is selected from popular songs listed, that song needs to be deleted and refreshed'''
        self.popularSongs.remove(song_id)
    
    def terminateSession(self):
        '''In case where user chooses to terminate the session, the session related information needs to be cleared'''
        pass

    def getCurrentSessionMood(self):
        sessionOutput = SessionOutput(use_lyrics= self.lyricsToggle, session_length=3, session_songIDs= self.currentSessionSongs)
        mood = sessionOutput.session_mood()
        if mood == 0:
            return 'Happy'
        elif mood ==1:
            return 'Angry'
        elif mood == 2:
            return 'Sad'
        elif mood == 3:
            return 'Relaxed'
        else:
            return 'Current Mood'
