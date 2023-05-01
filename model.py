import numpy as np
from numpy.linalg import norm
import pandas as pd

class SessionOutput:

  def __init__(self, df = pd.read_csv('alldata_normalized.csv'), use_lyrics=True, session_length=5, session_songIDs=[0, 1, 2]):
    self.df = df
    self.use_lyrics = use_lyrics
    self.session_length = session_length
    self.session_songIDs = session_songIDs
    
# Function to calculate the cosine similarity between two songs
  def calSimilarity(self, vector, other_song_vector):
    return np.dot(vector, other_song_vector)/(norm(vector)*norm(other_song_vector))

# aggregate vector calculation
  def aggregate_vector(self):
    den = 0
    if self.use_lyrics:
      # print("Yippee !! Lyrics are used to recommend songs")
      agg = np.zeros(10)
      iter_length = min(self.session_length, len(self.session_songIDs))
      for i in range(iter_length):
        currentSessionSongsLength = len(self.session_songIDs)
        songrow = self.df.loc[self.df['song_id'] == self.session_songIDs[currentSessionSongsLength - i - 1]]
        songrow = songrow[['tempo', 'energy', 'danceability','loudness','valence','acousticness','happy','angry','sad','relaxed']]
        # print("Song row")
        # print(songrow)
        agg = agg + songrow.values[0] * (i+1)
        den = den + i+1
    else:
      # print("Oops !! Lyrics are not used.")
      agg = np.zeros(6)
      for i in range(self.session_length):
        songrow = self.df.loc[self.df['song_id'] == self.session_songIDs[i]]
        songrow = songrow[['tempo', 'energy', 'danceability','loudness','valence','acousticness']]
        agg = agg + songrow.values[0] * (i+1)
        den = den + i+1
    return agg/den

# Function to recommend songs based on item-item CF
  def item_itemcf(self,input_aggregate_vector,k):
    # Calculate the similarity scores between the input song and all other songs
        similarity_scores = {}
        for index, row in self.df.iterrows():
            id = row['song_id']
            if self.use_lyrics:
              other_song_vector = [self.df.iloc[id, 7], self.df.iloc[id, 8], self.df.iloc[id, 9], self.df.iloc[id, 10], self.df.iloc[id, 11], self.df.iloc[id, 12], self.df.iloc[id, 20], self.df.iloc[id, 21], self.df.iloc[id, 22], self.df.iloc[id, 23] ]
            else:
               other_song_vector = [self.df.iloc[id, 7], self.df.iloc[id, 8], self.df.iloc[id, 9], self.df.iloc[id, 10], self.df.iloc[id, 11], self.df.iloc[id, 12]]
            similarity_scores[id] = self.calSimilarity(input_aggregate_vector, other_song_vector)
        
        # Sort the similarity scores in descending order and return the top k recommendations
        recommendations_list = []
        sorted_map = sorted(similarity_scores.items(), key=lambda x: x[1], reverse=True)[:k]
        recommendations_list = [pair[0] for pair in sorted_map]
        return recommendations_list

#call from ui
  def recommend_songs(self):
        agg_vector = self.aggregate_vector()
        recommendations = self.item_itemcf(agg_vector,5)
        return recommendations
  
  def session_mood(self):   
   agg = np.zeros(4)
   den = 0
   if self.use_lyrics:           
      for i in range(self.session_length):
        # print("------- Current Song IDs --------")
        # print(self.session_songIDs)
        currentSessionSongsLength = len(self.session_songIDs)
        songrow = self.df.loc[self.df['song_id'] == self.session_songIDs[currentSessionSongsLength - i - 1]]
        # print(songrow)
        songrow_1 = songrow[['spot_happy', 'spot_angry', 'spot_sad','spot_relaxed']]
        # print(songrow_1)
        songrow_2 = songrow[['happy', 'angry', 'sad','relaxed']]
        # print(songrow_2)
        avg = (songrow_1.values[0] + songrow_2.values[0])/2
        agg = agg + avg * (i+1)
        den = den + i+1
   else:
      for i in range(self.session_length):
        songrow = self.df.loc[self.df['song_id'] == self.session_songIDs[i]]
        songrow_1 = songrow[['happy', 'angry', 'sad','relaxed']]
        agg = agg + songrow_1.values[0] * (i+1)
        den = den + i+1
   agg_list = (agg/den).tolist()
   max_index = agg_list.index(max(agg_list))
   return max_index
  
# data = pd.read_csv('alldata.csv')
# test = SessionOutput(data, True, session_length=3, session_songIDs=[1771])
# print("Session mood:", test.session_mood())
# print(test.session_mood())



   
 
   





