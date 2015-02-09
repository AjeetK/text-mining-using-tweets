#Import the necessary methods from tweepy library
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

#Variables that contains the user credentials to access Twitter API 
access_token = "2507812099-Pj3dhFZl9CW40l0bwjxALA4Rv2MqksLey36Bw60"
access_token_secret = "3gMtceKmqLZdvvJqIBLkbrGlZ83tQi7ZcXEQpeycPSPP3"
consumer_key = "mlxnL0b3iPVo65Vwv8Sv4Pvf4"
consumer_secret = "VYq0PrbWGjxodAaEhI5wIatxWMpZZzOJ4KvC7R42l1Z0jIfPWE"


#This is a basic listener that just prints received tweets to stdout.
class StdOutListener(StreamListener):

    def on_data(self, data):
        print data
        return True

    def on_error(self, status):
        print status


if __name__ == '__main__':

    #This handles Twitter authetification and the connection to Twitter Streaming API
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    stream = Stream(auth, l)

    #This line filter Twitter Streams to capture data by the keywords: 'python', 'javascript', 'ruby'
    stream.filter(track=['python', 'javascript', 'ruby'])
