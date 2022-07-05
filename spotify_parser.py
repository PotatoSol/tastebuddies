from spotipy.oauth2 import SpotifyOAuth
import spotipy
import cred

scope = "user-library-read"
user = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=cred.client_id, client_secret= cred.client_secret, redirect_uri=cred.redirect_url, scope=scope), requests_timeout=10, retries=100)

def get_spotify_liked_songs():
    user_total = user.current_user_saved_tracks()['total']
    user_liked_tracks, user_liked_songs = [], []
    offset_amount = 0
    while(len(user_liked_tracks) < user_total):
        user_liked_tracks.extend(user.current_user_saved_tracks(offset = offset_amount)['items'])
        offset_amount += 20

    for x in range(len(user_liked_tracks)):
        user_liked_songs.extend(user_liked_tracks[x]['track']['name'])
    return user_liked_songs