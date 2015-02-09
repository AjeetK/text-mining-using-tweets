import json
import pandas as pd
import matplotlib.pyplot as plt

tweets_data_path = 'twitter_data.txt'

tweets_data = []
tweets_file = open(tweets_data_path, "r")
for line in tweets_file:
    try:
        tweet = json.loads(line)
        tweets_data.append(tweet)
    except:
        continue

#print tweets_data
print len(tweets_data)
tweets =  pd.DataFrame()
tweets['text'] = map(lambda tweet: tweet['text'], tweets_data)
tweets_by_language = tweets['text'].count
print tweets_by_language