import numpy as np
import pandas as pd

class SessionOutput:

  def __init__(self, use_lyrics=True, session_length=3, session_songIDs=[0, 1, 2]):
    self.use_lyrics = use_lyrics
    self.session_length = session_length
    self.session_songIDs = session_songIDs
  
  def aggregate_vector(self):
    den = 0
    if self.use_lyrics:
      agg = np.zeros(10)
      for i in range(self.session_length):
        songrow = data.loc[data['song_id'] == self.session_songIDs[i]]
        songrow = songrow[['tempo', 'energy', 'danceability','loudness','valence','acousticness','happy','angry','sad','relaxed']]
        agg = agg + songrow.values[0] * (i+1)
        den = den + i+1
    else:
      agg = np.zeros(6)
      for i in range(self.session_length):
        songrow = data.loc[data['song_id'] == self.session_songIDs[i]]
        songrow = songrow[['tempo', 'energy', 'danceability','loudness','valence','acousticness']]
        agg = agg + songrow.values[0] * (i+1)
        den = den + i+1
    # print(agg/den)
    return agg/den

  def item_itemcf(self):
    return


  def recommend_songs(self):
    agg_vector = self.aggregate_vector()
    recommendations = self.item_itemcf(agg_vector)

    return recommendations