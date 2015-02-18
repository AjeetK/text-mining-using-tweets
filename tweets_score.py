import json
import re
import numpy as np
from matplotlib import pyplot as plt

twitter_data_file = 'twitter_data.txt'

#tweets_file = open(twitter_data_file, "r")
with open(twitter_data_file) as tf:
	tweets = [json.loads(line).get('text') for line in tf]

print len(tweets)

#### Function to classify the tweets by finding suitable keyword in the tweet
def tweets_related_to(word,text):
	text = text.lower()
	word = word.lower()
	match = re.search(word, text)
	if match:
		return text



##### Fetching hashtags related to python ####
hashtags = {"python":[], "ruby":[], "javascript":[]}
def hashtags_related_to(lang,text):
	text =  text.lower()
	lang = lang.lower()
	#print lang

	my_regex = r'^#.*' + re.escape(lang) + r'.*'
	for word in text.split():
		match = re.search(my_regex,word)
		
		if match:
			print word
			#print "\n"
			return word
			

			#hashtags = hashtags.append(match)
		
		

	

languages = ["python","ruby","javascript"]
# for tweet in tweets:
# 	hashtags_related_to(tweet)
rtags = []

rtags = [hashtags_related_to(item,tweet) for item in languages for tweet in tweets]
#rtags = [hashtags_related_to('python',tweet) for tweet in tweets]

print "list"
rtags = filter(None,rtags)



all_tags = []
for i in rtags:
  if i not in all_tags:
    all_tags.append(i)
# for item in ruby_tags:
# 	print item
print "lenth of rtags"
print len(rtags)

#### writing list of hashtags to a file hashtag_tweets.txt
with open('hashtags.txt','w') as hf:
	for item in all_tags:
		hf.write("%s\n" %item)


#### appending tags for key-ruby in hashtags dictionary
# for item in ruby_tags:
# 	hashtags["ruby"].append(item)

print len(hashtags)
for k in hashtags:
	print hashtags["ruby"]
print len(hashtags["ruby"])

#### Fetching tweets associated with different keywords and counting the number of tweets ####

#getting tweets associated with python and assigning it to python list variable
python = [tweets_related_to('python',tweet) for tweet in tweets]
#Filtering python list as it contains none values
python = filter(None, python)
print "tweets associated with python :"
print len(python)

ruby = [tweets_related_to('ruby',tweet) for tweet in tweets]
ruby = filter(None, ruby)
print "tweets associated with ruby :"
print len(ruby)

javascript = [tweets_related_to('javascript',tweet) for tweet in tweets]
javascript = filter(None, javascript)
print "tweets associated with javascript :"
print len(javascript)

#### Calculating positivity of each tweets related to different category of tweets ####
score_file = 'AFINN-111.txt'
with open(score_file) as sf:
        scores =  {line.split('\t')[0]: int(line.split('\t')[1]) for line in sf}


#### Function to calculate score of each tweet related to each category
def calculate_score(text):
	sum = 0
	for word in text.split():
		sum += scores.get(word,0)
	if sum >= 0:
		return text

#### calculating score of python related tweets and assigning tweets(having score>=0) to python_positive list 
python_positive = [calculate_score(tweet) for tweet in python]
python_positive =  filter(None, python_positive)
print "No. of Python related positive tweets are :"
print len(python_positive)

ruby_positive = [calculate_score(tweet) for tweet in ruby]
ruby_positive =  filter(None, ruby_positive)
print "No. of ruby related positive tweets are :"
print len(ruby_positive)

javascript_positive = [calculate_score(tweet) for tweet in javascript]
javascript_positive =  filter(None, javascript_positive)
print "No. of javascript related positive tweets are :"
print len(javascript_positive)




#### Plotting figur
OX = ["python", "ruby", "javascript"]
OY = [len(python_positive), len(ruby_positive), len(javascript_positive)]
print OY
fig = plt.figure()

width = .35
ind = np.arange(len(OY))
plt.bar(ind, OY)
plt.xticks(ind + width / 2, OX)

fig.autofmt_xdate()
plt.show()
#plt.savefig("figure.pdf")
