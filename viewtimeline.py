import tweepy
from twitterClient import get_twitter_auth


#downloads your home timeline tweets and prints each one of their texts to the console


auth = get_twitter_auth()
api = tweepy.API(auth)

public_tweets = api.home_timeline()
for tweet in public_tweets:
    print(tweet.text)