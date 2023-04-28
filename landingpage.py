from flask import Flask, render_template
import csv
from model import SessionOutput

app = Flask(__name__)

# load songs from CSV file
def load_songs():
    with open('alldata.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        songs = [row for row in reader]
    return songs

@app.route('/')
def index():
    # load current session
    current_session = "My current session"
    # load songs from CSV file
    songs = load_songs()
    # render template with current session and songs
    return render_template('index.html', current_session=current_session, songs=songs)

@app.route('/recommended')
def recommended():
    # return recommended songs as JSON response
    recommended_songs = [
        {"title": "Recommended Song 1", "artist": "Artist 1", "url": "#"},
        {"title": "Recommended Song 2", "artist": "Artist 2", "url": "#"},
        {"title": "Recommended Song 3", "artist": "Artist 3", "url": "#"}
    ]
    return {"recommended_songs": recommended_songs}

if __name__ == '__main__':
    app.run(debug=True)
