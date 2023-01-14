from flask import Flask, render_template
from flask_cors import CORS, cross_origin
from markupsafe import escape
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

app = Flask(__name__)
sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id="84af1505be054f3b9fd53159862927c3", client_secret="56649eacd32e4547bef169c2b4413932"))

@app.route('/')
def index():
    return render_template('index.html')

# ==================== Spotipy ====================
# Album
@app.get('/album/<string:id>')
def get_album(id):
    return sp.album(escape(id))

# Album with tracks
@app.get('/album/<string:id>/tracks')
def get_album_tracks(id):
    return sp.album_tracks(escape(id))

# Artist
@app.get('/artist/<string:id>')
def get_artist(id):
    return sp.artist(escape(id))

# Artist with albums
@app.get('/artist/<string:id>/albums')
def get_artist_albums(id):
    return sp.artist_albums(escape(id))

# Artist top tracks
@app.get('/artist/<string:id>/top-tracks')
def get_artist_top_tracks(id):
    return sp.artist_top_tracks(escape(id))

# Track
@app.get('/track/<string:id>')
def get_track(id):
    return sp.track(escape(id))

# Search album
@app.get('/search/album/<string:name>', defaults={'limit': 10})
@app.get('/search/album/<string:name>/<int:limit>')
def search_album(name, limit):
    return sp.search(q='album:' + escape(name), type='album', limit=escape(limit))

# Search artist
@app.get('/search/artist/<string:name>', defaults={'limit': 5})
@app.get('/search/artist/<string:name>/<int:limit>')
def search_artist(name, limit):
    return sp.search(q='artist:' + escape(name), type='artist', limit=escape(limit))

# Search track
@app.get('/search/track/<string:name>', defaults={'limit': 10})
@app.get('/search/track/<string:name>/<int:limit>')
def search_track(name, limit):
    return sp.search(q='track:' + escape(name), type='track', limit=escape(limit))