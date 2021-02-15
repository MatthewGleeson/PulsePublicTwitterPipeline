import sys
import string
import time
from tweepy import Stream
from tweepy.streaming import StreamListener
from twitterClient import get_twitter_auth


class CustomListener(StreamListener):
    """ Custom StreamListener for streaming twitter data."""

    def __init__(self, fname):

        safe_filename = ''.join(convert_valid(one_char) for one_char in fname)
        self.outfile = "stream_%s.jsonl" % safe_filename

    def on_data(self, data):
        try:
            with open(self.outfile, 'a') as f:
                f.write(data)
                #write to .jsonl file, every line = 1 tweet
                return True
        except BaseException as e:
            sys.stderr.write("Error on_data: {}\n".format(e))
            #wait 5 seconds, then re-enter normal execution process
            time.sleep(5)
        return True

    def on_error(self, status):
        #420 = rate limit error. In this case we definitely want to stop
        if status == 420:
            sys.stderr.write("Rate limit exceeded")
            return False
        else:
            sys.stderr.write("Error {}\n".format(status))
            return True


def format_filename(fname):
    

    return 

def convert_valid(one_char):

    """ Converts a character into '_' if "invalid".
        Return string.
    """

    valid_chars = "-_.%s%s" % (string.ascii_letters, string.digits)
    if one_char in valid_chars:
        return one_char
    else:
        return '_'


if __name__ == '__main__':
    #query = sys.argv[1:] # list of CLI argumentsquery_fname
    #query_fname = ' '.join(query) # string
    query_fname = 'bostonListener'
    auth = get_twitter_auth()
    twitter_stream = Stream(auth, CustomListener(query_fname))
    #twitter_stream.filter(track=query, is_async=True)

    #ALL US TWEETS
    #twitter_stream.filter(locations = [32.491230,-117.498920,44.871443,-67.440434], is_async=True)

    #ONLY BOSTON SEARCH PARAMETERS:
    twitter_stream.filter(locations = [42.187452, -71.321879,42.476259, -70.863781], is_async=True)

    #BOSTON OR COVID:
    #twitter_stream.filter(track=['covid'],locations = [42.187452, -71.321879,42.476259, -70.863781], is_async=True)

#ex:
#python3 twitter_streaming.py \#covid has:geo (point_radius:[42.361145 -71.057083  25mi] OR place:"Boston, MA” OR (profile_locality:boston profile_region:Massachusetts ))