import tweepy

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_toke(access_token, access_token_secret)

api = tweepy.API(auth)
