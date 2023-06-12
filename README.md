# tuneinmind

Find the live website here: https://tuneinmind-isr.herokuapp.com/

## Introduction
Present recommender systems do not take into account the current session based mood of the user. Recommendations are given based on user’s complete listening history
TuneInMind solves this by taking into consideration the user's Session-based information.
We leverage the lyrics aggregate data as well as the spotify accoustic data to derive the current session mood of a user.
Machine Learning models like Random Forest Classifiers are used to predict the probabilities of each mood.
We recommend songs based on the aggregate mood vector of the session's songs. Moods : Happy, Sad, Relaxed, Angry
This will ensure that user gets appropriate song recommendations pertaining to his/hers current mood.

## Proposed Solution

# Dataset Creation
Songs included in the dataset must be available on both Genius and Spotify. We collected the data using two methods: querying the Spotify API for song features of a given track in the Genius dataset, and searching for song lyrics on the Genius API for Spotify song samples.

# Predict Moods from lyrics
A random forest classification model is used to process song lyrics and predict the probability distribution of four mood attributes: Happy, Sad, Relax, and Angry.

# Predict Moods from Spotify features
Six track features (Danceability, Loudness, Valence, Acousticness, Tempo, and Energy) are obtained using the Spotify API's "Get Track's Audio Features" and pre-processed (normalized and scaled) to be used as inputs to the classification model. The model then predicts the mood distribution for four moods.

# Item-Item Collaborative filtering
During the current session, the "session aggregate mood vector" is created by combining the individual mood distribution vectors of the songs played. This vector is then used to apply Item-Item Collaborative Filtering, which recommends five songs that are most similar to the ones played during the session. The Current Mood label is obtained by aggregating mood attributes derived from both Acoustic and Lyrics data.

## Performance and Evaluation
In recommender systems, evaluation is the process of assessing the performance and quality of the recommendations produced by the system. It involves measuring how well the recommender system predicts user preferences or behavior, and how effective the recommended items are in satisfying the user's needs.

In our case we have evaluated recommendations in two cases for our performance evaluation. First case is toggle on (This is feature developed by our team), In this case lyrics data is also pre-processed and analyzed along with Spotify acoustic data for generating recommendations. Second case is toggle off, In this case lyrics data is not considered, only Spotify acoustic data is considered for generating mood based recommendations.

We can see that performance is significantly improved with introduction of lyrics based moods. With usage of lyrics data , the recommendations are better generated. For happy and relaxed we can see that happy mood songs are recommended. Where as in the older case(without lyrics data) recommendations are slightly off the mark.

