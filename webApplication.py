from enum import Enum

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
