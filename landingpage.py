from flask import Flask, render_template
import csv
# from model import SessionOutput

app = Flask(__name__)



# load songs from CSV file
def load_songs(song_ids):
    with open('alldata.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        songs = [row for row in reader]

    if song_ids:
        result_songs = []
        for song in songs: 
            if song['song_id'] in song_ids: 
                result_songs.append(song)
        return result_songs 
    else:
        return songs


def get_song_recommendations(session_song_ids):
    # Call Session function
    # Take the session_song_ids as the input and return the recommended songs
    recommended_song_ids = ['1','2','3','4','5', '6','7','8','9','10', '11','12','13','14','15']
    return load_songs(recommended_song_ids)


@app.route('/')
def index():
    # load current session
    current_session = "My current session"
    # load songs from CSV file
    songs = load_songs([])

    session_song_ids = ['6','7','8','9','10']
    recommended_songs = get_song_recommendations(session_song_ids)
    # render template with current session and songs
    return render_template('index.html', current_session=current_session, songs=songs, recommended_songs = recommended_songs)

# @app.route('/recommended')
# def recommended():
#     # return recommended songs as JSON response
#     recommended_songs = [
#         {"title": "Recommended Song 1", "artist": "Artist 1", "url": "#"},
#         {"title": "Recommended Song 2", "artist": "Artist 2", "url": "#"},
#         {"title": "Recommended Song 3", "artist": "Artist 3", "url": "#"}
#     ]
#     return {"recommended_songs": recommended_songs}

if __name__ == '__main__':
    app.run(debug=True)
