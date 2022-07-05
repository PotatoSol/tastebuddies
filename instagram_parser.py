import instagrapi



user = instagrapi.Client()
user.login("PotatoSol", "ughyPotato224!")
user_id = user.user_id_from_username("potatosol")
following = user.user_following_gql()
print(following)