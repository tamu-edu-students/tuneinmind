from flask import Flask, render_template, jsonify, request
import csv
from webApplication import webApplication
# from model import SessionOutput

app = Flask(__name__)
webApp = webApplication()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/session')
def session_index():
    songs = webApp.generatePopularSongs()
    # render template with current session and songs
    return render_template('session.html', songs=songs, recommended_songs = [])

@app.route('/add_song_to_session', methods=['POST'])
def add_song_to_session():
    data = request.get_json()
    song_id = data["song_id"]
    webApp.addToCurrentSession(song_id)
    return jsonify({'success': True})

@app.route('/get_recommended_songs')
def get_recommended_songs():
    # Get the current session songs
    print(webApp.currentSessionSongs)
    current_session_songs = [int(x) for x in webApp.currentSessionSongs]
    print("------Current Session Songs------")
    print(current_session_songs)
    webApp.currentSessionSongs = current_session_songs
    # Generate the recommended songs based on the current session songs
    recommended_songs = webApp.generateRecommendations()
    print("------Recommended Songs------")
    print(recommended_songs)
    # Convert the recommended songs to a JSON response
    response = [{'title': song.title, 'artist': song.artist, 'song_id': song.song_id} for song in recommended_songs]
    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)
