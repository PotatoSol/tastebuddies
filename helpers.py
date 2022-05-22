from requests.exceptions import ReadTimeout, ConnectionError
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import cred

scope = "user-read-private"
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=cred.client_id, client_secret= cred.client_secret, redirect_uri=cred.redirect_url, scope=scope), requests_timeout=10, retries=10)

#Input a Playlist ID and then get a full playlist as output - necessary because api only allows 100 songs per request
def importFullPlaylist(importPlaylistID):
    outputPlaylist = []
    currentOffset = 0
    while(True):
        try:
            importPlaylist = spotipy.Spotify.playlist_items(self = sp, playlist_id = importPlaylistID).copy()
            break
        except ConnectionError as e:
            print("Failed...trying again...")
            continue
        finally:
            break
        
    totalLen = importPlaylist['total']
    
    outputPlaylist.extend(importPlaylist['items'].copy())
    while( len(outputPlaylist) < totalLen) : 
        currentOffset += 100
        importPlaylist = spotipy.Spotify.playlist_items(self = sp, playlist_id = importPlaylistID, offset = currentOffset)
        outputPlaylist.extend(importPlaylist['items'].copy())
        importPlaylist.clear()
    
    return outputPlaylist