#!/usr/bin/python
# -*- coding: utf-8 -*-

import re
from textblob import TextBlob


class Sentiments:
    POSITIVE = 'Positive'
    NEGATIVE = 'Negative'
    NEUTRAL = 'Neutral'
    CONFUSED = 'Confused'


id_field = 'id_str'
emoticons = {Sentiments.POSITIVE: '😀|😁|😂|😃|😄|😅|😆|😇|😈|😉|😊|😋|😌|😍|😎|😏|😗|😘|😙|😚|😛|😜|😝|😸|😹|😺|😻|😼|😽',
             Sentiments.NEGATIVE: '😒|😓|😔|😖|😞|😟|😠|😡|😢|😣|😤|😥|😦|😧|😨|😩|😪|😫|😬|😭|😾|😿|😰|😱|🙀',
             Sentiments.NEUTRAL: '😐|😑|😳|😮|😯|😶|😴|😵|😲',
             Sentiments.CONFUSED: '😕'
             }

tweet_mapping = {
    'mappings': {
        'properties':
        {'timestamp_ms': {
            'type': 'date'
        },
            'text': {
            'type': 'string'
        },
            'coordinates': {
            'properties': {
                'coordinates': {
                    'type': 'geo_point'
                },
                'type': {
                    'type': 'string',
                    'index': 'not_analyzed'
                }
            }
        },
            'user': {
            'properties': {
                'id': {
                    'type': 'long'
                },
                'name': {
                    'type': 'string'
                }
            }
        },
            'sentiments': {
                         'type': 'string',
                         'index' : 'not_analyzed'
                     }
        }
    }
}


# https://www.elastic.co/blog/strings-are-dead-long-live-strings
tweet_mapping_v5 = {
    'properties':
    {'timestamp_ms': {
        'type': 'date'
    },
        'text': {
        'type': 'text'
    },
        'coordinates': {
        'properties': {
            'coordinates': {
                'type': 'geo_point'
            },
            'type': {
                'type': 'keyword'
            }
        }
    },
        'user': {
        'properties': {
            'id': {
                'type': 'long'
            },
            'name': {
                'type': 'text'
            }
        }
    },
        'sentiments': {
                     'type': 'keyword'
                 }
    }
}


def _sentiment_analysis(tweet):
   tweet['emoticons'] = []
   tweet['sentiments'] = []
   _sentiment_analysis_by_emoticons(tweet)
   if len(tweet['sentiments']) == 0:
      _sentiment_analysis_by_text(tweet)


def _sentiment_analysis_by_emoticons(tweet):
   for sentiment, emoticons_icons in emoticons.items():
      matched_emoticons = re.findall(emoticons_icons, tweet['text'])
      if len(matched_emoticons) > 0:
         tweet['emoticons'].extend(matched_emoticons)
         tweet['sentiments'].append(sentiment)

   if Sentiments.POSITIVE in tweet['sentiments'] and Sentiments.NEGATIVE in tweet['sentiments']:
      tweet['sentiments'] = Sentiments.CONFUSED
   elif Sentiments.POSITIVE in tweet['sentiments']:
      tweet['sentiments'] = Sentiments.POSITIVE
   elif Sentiments.NEGATIVE in tweet['sentiments']:
      tweet['sentiments'] = Sentiments.NEGATIVE

def _sentiment_analysis_by_text(tweet):
   blob = TextBlob(tweet['text'])
   sentiment_polarity = blob.sentiment.polarity
   if sentiment_polarity < 0:
      sentiment = Sentiments.NEGATIVE
   elif sentiment_polarity <= 0.2:
      sentiment = Sentiments.NEUTRAL
   else:
      sentiment = Sentiments.POSITIVE
   tweet['sentiments'] = sentiment


def get_tweet(doc):
    tweet = {}
    tweet[id_field] = doc[id_field]

    tweet['hashtags'] = [x['text'] for x in doc['entities']['hashtags']]
    tweet['coordinates'] = doc['coordinates']

    tweet['timestamp_ms'] = doc['timestamp_ms']


    tweet['text'] = doc['text']

    tweet['user'] = {'id': doc['user']['id'], 'name': doc['user']['name']}

    tweet['mentions'] = re.findall(r'@\w*', doc['text'])

    _sentiment_analysis(tweet)
    
    return tweet


def get_tweet_mapping(es_version_number_str):
    major_number = int(es_version_number_str.split('.')[0])
    if major_number >= 5:
        return tweet_mapping_v5
    return tweet_mapping
