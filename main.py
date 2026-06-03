import spotipy
from dotenv import load_dotenv
import os
from spotipy.oauth2 import SpotifyOAuth
from datetime import date

load_dotenv()

client_id = os.getenv("SPOTIFY_API_KEY")
client_secret = os.getenv("SPOTIFY_CLIENT_SECRET")

sp_oauth = SpotifyOAuth(
    client_id=client_id,
    client_secret=client_secret,
    redirect_uri="http://127.0.0.1:5000/callback",
    scope="user-top-read user-read-private user-read-email playlist-modify-public playlist-modify-private",
    show_dialog=True,
    cache_path=None
)

sp = spotipy.Spotify(auth_manager=sp_oauth)

album_images_dict = {}
top_tracks_dict = {}
top_artists_list = []
artist_images_dict = {}
user_name = None
user_id = None
top_tracks_uris = []
name = None
description = None

def fetch_user_data():
    global album_images_dict, top_tracks_dict, top_artists_list, artist_images_dict, user_name, user_id, top_tracks_uris, name, description
    global loyalty_index_value, loyalty_index_statement, music_age_value, music_age_statement
    
    top_tracks = sp.current_user_top_tracks(limit=10, time_range="medium_term")
    top_tracks_dict = {}
    album_images_dict = {}
    for i in top_tracks["items"]:
        top_tracks_dict[i["name"]] = i["artists"][0]["name"]
        album_images_dict[i["name"]] = i["album"]["images"][0]["url"]

    top_artists = sp.current_user_top_artists(limit=10, time_range="medium_term")
    top_artists_list = []
    for i in top_artists["items"]:
        top_artists_list.append(i["name"])

    artist_images_dict = {}
    for artist in top_artists_list:
        results = sp.search(q=artist, type="artist", limit=5)
        if results["artists"]["items"]:
            artist_images_dict[artist] = results["artists"]["items"][0]["images"][0]["url"]

    user_name = sp.current_user()["display_name"].title()
    user_id = sp.current_user()["id"]

    top_tracks_uris = []
    for track in top_tracks["items"]:
        top_tracks_uris.append(track["uri"])

    name = f"{user_name}'s Top Tracks"
    description = "A playlist containing your top tracks created by Wrapify."
    
    loyalty_index_value, loyalty_index_statement = calculate_loyalty_index()
    music_age_value, music_age_statement = calculate_music_age()

def create_top_10_playlist(name, description, public=True):
    playlist = sp.current_user_playlist_create(
        name=name, 
        public=public, 
        description=description
    )
    return playlist["id"]

def add_tracks_to_playlist(playlist_id, track_uris):
    sp.playlist_add_items(playlist_id, track_uris)

def calculate_loyalty_index():
    statement = ""
    top_50_tracks = sp.current_user_top_tracks(limit=50, time_range="medium_term")
    count = 0
    for track in top_50_tracks["items"]:
        if track["artists"][0]["name"] in top_artists_list:
            count += 1
    loyalty_score = (count / 50) * 100

    if loyalty_score > 80:
        statement = "You're a stan!"
    elif loyalty_score > 50:
        statement = "You know your top artist well!"
    else:
        statement = "You like variety in your music!"
    return f"{loyalty_score:.1f}", statement

def calculate_music_age():
    statement = ""
    top_50_tracks = sp.current_user_top_tracks(limit=50, time_range="medium_term")
    avg_age = 0
    for track in top_50_tracks["items"]:
        avg_age += date.today().year - int(track["album"]["release_date"][:4])
    avg_age /= 50

    if avg_age > 50:
        statement = "You're an old soul!"
    elif avg_age > 30:
        statement = "You're a millenial at heart!"
    else:
        statement = "You're a baby!"
    return f"{avg_age:.1f}", statement

loyalty_index_value = None
loyalty_index_statement = None
music_age_value = None
music_age_statement = None