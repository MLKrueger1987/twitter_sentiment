"""
Fetchs Tweets using tweepy
"""
import tweepy
from auth_tokens import oauth_dict as tokens

class TweetFetcher(object):
    """docstring for TweetFetcher"""
    def __init__(self):
        """
        Intatiates a tweet fetcher
        """
        consumer_key = tokens['consumer_key']
        consumer_secret = tokens['consumer_secret']
        access_token = tokens['access_token']
        access_token_secret = tokens['access_token_secret']

        auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_token, access_token_secret)

        self.api = tweepy.API(auth)

    def fetch_hashtag(self, tag, max_to_fetch=200, language='en', no_RT= True):
        """
        Fetches the tweets that match a hashtag search
        """
        query = tag + " -filter:retweets" if no_RT else tag

        lang = language

        rpp = 100 # The number of tweets returned per page, 100 is max

        hash_search = tweepy.Cursor(self.api.search, q=query, 
                                    rpp=rpp, lang=lang,).items(max_to_fetch)
        for page in hash_search:
            with open('tweets_with_hashtag_#Apple.txt', 'a') as the_file:
                the_file.write(str(page.text.encode('utf-8')) + '\n')

        print('Extracted {} tweets with hashtag {}'.format(max_to_fetch, 
                                                           query))
