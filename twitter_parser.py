import tweepy, main

consumer_key =  "vA0le6OmCAajJ5jZek1jEejn8"
consumer_secret = "D2qkzG12E5iwFR3xYWIRlqy7WCeofklX9Ai7gyYBreOYIPGbWx"
access_token = "392433546-9rOVva2ug9Hk7nfHykHmXJig17K29zUAgFN0SMAb"
access_token_secret = "R22ZVkfyxJHILaox1wIkJiznS3rEt9v8Nvtt2fh31U5QK"
bearer_token = "AAAAAAAAAAAAAAAAAAAAAHKudQEAAAAAsayL1paYdg8axWYlKi2aaMD%2B9rY%3DRQ7GlRemLtqVqm0Z2JxsfzbUtp6hYpQOp8SOXWDPSQCr6mRKSv"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth, wait_on_rate_limit=True)
user_handle = main.twitter_handle
user = api.get_user(screen_name = user_handle)
user_ID = user.id_str


user_client = tweepy.Client(   bearer_token = bearer_token, consumer_key = consumer_key, 
                        consumer_secret = consumer_secret, access_token = access_token, 
                        access_token_secret = access_token_secret, wait_on_rate_limit=True)

def get_twitter_follows():
    full_list = []
    following = user_client.get_users_following(id = user_ID, max_results = 1000)
    full_list.extend(following.data)

    for keys in following.meta.keys():
            if keys == "next_token": 
                is_in_dict = True
                next_token = following.meta['next_token']
            else:
                is_in_dict = False

    while is_in_dict:
        following = user_client.get_users_following(id = user_ID, max_results = 1000, pagination_token = next_token)
        full_list.extend(following.data)
        is_in_dict = False
        for keys in following.meta.keys():
            if keys == "next_token": 
                is_in_dict = True
            else:
                is_in_dict = False
                

    return full_list