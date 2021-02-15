import boto3
import json
from datetime import datetime
import calendar
import random
import time
import sys
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import os

#Variables that contains the user credentials to access Twitter API
consumer_key = os.environ['TWITTER_CONSUMER_KEY']
consumer_secret = os.environ['TWITTER_CONSUMER_SECRET']
access_token = os.environ['TWITTER_ACCESS_KEY']
access_secret= os.environ['TWITTER_ACCESS_SECRET']



class TweetStreamListener(StreamListener):        
    # on success
    def on_data(self, data):
        tweet = json.loads(data)
        try:
            if 'text' in tweet.keys():
                message = json.dumps(tweet)

                message = message + "\n"
                
                results = kinesis_client.put_record(
                    DeliveryStreamName=stream_name,
                    Record={
                    'Data': message
                    }
                )
                print(results)
        except (AttributeError, Exception) as e:
                print (e)
        return True
        
    # failure
    def on_error(self, status):
        print(status)


stream_name = 'twitter-firehose'  #name of kinesis data stream

if __name__ == '__main__':
    # connect to kinesis client
    kinesis_client = boto3.client('firehose',
                                  region_name='us-east-1',
                                  aws_access_key_id=os.environ['AWS_IAM_ACCESS_KEY_ID'],  
                                  aws_secret_access_key=os.environ['AWS_IAM_SECRET_ACCESS_KEY']) 
    # create instance of the tweepy tweet stream listener
    listener = TweetStreamListener()
    # set twitter keys/tokens
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_secret)
    # create instance of the tweepy stream
    stream = Stream(auth, listener)
    # search twitter for tags or keywords from cli parameters
    
    #query = sys.argv[1:] # list of CLI arguments 
    #query_fname = ' '.join(query) # string
    query_fname = 'covidglobal'
    
    #stream.filter(track=query)
    stream.filter(track=['covid'])