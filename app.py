import spotipy
from spotipy.oauth2 import SpotifyOAuth
import cred
import pprint
from requests.exceptions import ReadTimeout, ConnectionError

scope = "user-read-private"

pp = pprint.PrettyPrinter(indent=0)
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=cred.client_id, client_secret= cred.client_secret, redirect_uri=cred.redirect_url, scope=scope), requests_timeout=10, retries=10)

user_playlists = spotipy.Spotify.current_user_playlists(sp)
parsed_user_playlists = []
cleaned_user_playlists = []

tempPlaylist = []
tempCleanedPlaylist = []
tempPlaylistItems = None #Full Song Item
tempCleanedSong = () #Tuple(Song Name, Artist, Song ID, Artist ID)
tempSongName = None #Song Name
tempArtists = [] #Artists
tempSongID = None #SongID
tempArtistIDs = [] #ArtistIDs
playlistOffset = 0
tempSongVar = None

#TODO: add support for playlists over 100 tracks
#maybe something like make a playlist before the loop and loop thru if its under the total 
#can use tempPlaylistItems length to get current number of songs
#and use user_playlists['items'][x]['tracks']['total'] to get the number of tracks per specific playlist

#Input a Playlist ID and then get a full playlist as output
def importFullPlaylist(importPlaylistID):
    outputPlaylist = []
    currentOffset = 0
    importPlaylist = spotipy.Spotify.playlist_items(self = sp, playlist_id = importPlaylistID)
    totalLen = importPlaylist['total']
    
    outputPlaylist.extend(importPlaylist['items'].copy())
    while( len(outputPlaylist) < totalLen) : 
        currentOffset += 100
        importPlaylist = spotipy.Spotify.playlist_items(self = sp, playlist_id = importPlaylistID, offset = currentOffset)
        outputPlaylist.extend(importPlaylist['items'].copy())
        importPlaylist.clear()
    
    return outputPlaylist

# #Go through each playlist and....
# for i in range(1):#range(len(user_playlists['items'])):
#     for j in range(user_playlists['items'][i]['tracks']['total']):
#         tempPlaylistItems = spotipy.Spotify.playlist_items(playlist_id = user_playlists['items'][i]['id'], self = sp) #asigns the full song item to this var
#         tempPlaylist.append(tempPlaylistItems) #adds the full song item to the temp playlist list
        
#         for artist in range(len(tempPlaylistItems['items'][j]['track']['artists'])):
#             print(len(tempPlaylistItems['items']))
#             tempArtists.append(tempPlaylistItems['items'][j]['track']['artists'][artist]['name'])
#             tempArtistIDs.append(tempPlaylistItems['items'][j]['track']['artists'][artist]['id'])
        
#         tempCleanedSong = ( #song, artists, id, artist ids
#             tempPlaylistItems['items'][j]['track']['name'], 
#             tempArtists.copy(),
#             tempPlaylistItems['items'][j]['track']['id'],
#             tempArtistIDs.copy()
#             )
#         tempCleanedPlaylist.append(tempCleanedSong)
#         tempArtists.clear()
#         tempArtistIDs.clear()
#     parsed_user_playlists.append((user_playlists['items'][i], tempPlaylist.copy()))
#     cleaned_user_playlists.append((user_playlists['items'][i]['name'], tempCleanedPlaylist.copy()))
#     printOnce = tempCleanedPlaylist.copy()
#     tempCleanedPlaylist.clear()
#     tempPlaylist.clear()


