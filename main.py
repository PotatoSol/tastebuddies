import user_profile, spotify_parser, twitter_parser

twitter_handle = ""
user = user_profile(spotify_parser.get_spotify_liked_songs(), twitter_parser.get_twitter_follows(), [])