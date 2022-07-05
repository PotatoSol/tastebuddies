#A class defining a user profile
#Has variables defining their follower lists and liked songs and such




class user_profile():
    def __init__(self, spotify_songs: list, twitter_follows: list, instagram_follows: list):
        self.spotify_songs, self.twitter_follows, self.instagram_follows = [], [], []
        self.spotify_songs.extend(spotify_songs)
        self.twitter_follows.extend(twitter_follows)
        self.instagram_follows.extend(instagram_follows)
        
        self.has_spotify = self.has_account(spotify_songs)
        self.has_twitter = self.has_account(twitter_follows)
        self.has_instagram = self.has_twitterhas_account(instagram_follows)
        
    def has_account(input_account):
        if(input_account.len() == 0):
            return False
        else:
            return True
    
    