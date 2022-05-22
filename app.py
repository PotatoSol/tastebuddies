from numpy import full
from requests.exceptions import ReadTimeout, ConnectionError
from spotipy.oauth2 import SpotifyOAuth
import helpers
import spotipy
import pprint
import cred

scope = "user-read-private"
pp = pprint.PrettyPrinter(indent=0)
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=cred.client_id, client_secret= cred.client_secret, redirect_uri=cred.redirect_url, scope=scope), requests_timeout=10, retries=100)

#Grab all of the user's playlists from their profile
user_playlists = spotipy.Spotify.current_user_playlists(sp).copy()

#Temporary Variables for the loop below, no underscores
tempPlaylist, tempCleanedPlaylist, tempArtists, tempArtistIDs, fullUserPlaylist, tempCleanedSong, tempCleanedPlaylistTuple = [], [], [], [], [], (), ()
tempSongName, tempSongID, tempSongVar, tempPlaylistItems = None, None, None, None 

#These will be returned after the loop below, have underscores
parsed_user_playlists, cleaned_user_playlists = [], []

while(True):
    try:
        #Go through all of the playlists of the user and then...
        for playlistSelection in range(len(user_playlists['items'])):
            print('Working on this playlist: ' + str(playlistSelection) + " out of " + str(len(user_playlists['items'])))
            #Go through the selected playlist and get the full version of it 
            fullUserPlaylist = helpers.importFullPlaylist(user_playlists['items'][playlistSelection]['id'])
            #Go through every song in the full selected playlist
            for songSelection in range(len(fullUserPlaylist)):
                tempPlaylistItems = fullUserPlaylist[songSelection]
                tempPlaylist.extend(fullUserPlaylist[songSelection]) #Adds the full song item to tempPlaylist
                #TODO Maybe change these to dicts? tuple?
                #Get the artist information for the selected song
                
                for artistSelection in (range(len(tempPlaylistItems['track']['artists']))):
                    tempArtists.append(tempPlaylistItems['track']['artists'][artistSelection]['name']) #Get the name for each artist and add it to a temp var
                    tempArtistIDs.append(tempPlaylistItems['track']['artists'][artistSelection]['id']) #Get the ID for each artist and add it to a temp var
                #Temp var ( Song name, Artist names, Song IDs, Artist IDs - really only going to check Song ID later, probably)
                tempCleanedSong = ( 
                    tempPlaylistItems['track']['name'],
                    tempArtists.copy(),
                    tempPlaylistItems['track']['id'],
                    tempArtistIDs.copy()
                )
                tempCleanedPlaylist.extend(tempCleanedSong) #Add the new cleared song item to the temp playlist
                tempArtists.clear() #clear variable to be used again
                tempArtistIDs.clear() #clear variable to be used again
            parsed_user_playlists.extend((user_playlists['items'][playlistSelection], tempPlaylist.copy())) #Adds to the end of the parsed playlist (Playlist item, list of full song item)
            tempCleanedPlaylistTuple = ((user_playlists['items'][playlistSelection]['name']), (tempCleanedPlaylist.copy()))
            cleaned_user_playlists.append(tempCleanedPlaylistTuple) #Adds to the end of the cleaned playlist (Playlist name, Cleaned song item)
            tempCleanedPlaylist.clear() #clear variable to be used again
            tempPlaylist.clear() #clear variable to be used again
        
    except ConnectionError as e:
        print('Connection failed, continuing hopefully') #Does not retry, figure out how to do that
    finally:
        break #idk


print(len(cleaned_user_playlists))