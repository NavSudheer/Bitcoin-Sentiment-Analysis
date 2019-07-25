import tweepy
from textblob import TextBlob

consumer_key = 	'***************' #insert consumer_key here 
consumer_secret = '*******************' #insert consumer_secret here

access_token = '344622805-2YWt81TbNUkNlzmXsR10fevWiRc3MgZus5Ntz09W'
access_token_secret = 'UfSwqrLy182G01ZX1L3Qo6Uk0HWLnhLbVZPWtGO1smFaz'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

public_tweets = api.search('bitcoin')

for tweet in public_tweets:
	print(tweet.text)
	analysis = TextBlob(tweet.text)
	print(analysis.sentiment)
