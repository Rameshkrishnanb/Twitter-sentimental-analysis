#!/usr/bin/env python

import tweepy
from textblob import TextBlob

consumerKey = '0NiduTn5vlz9rsDrpaVV7E65v'
consumerKeySecret = 'LRGvbSuBcO7QjbTWPrfImZ845gzVQIV7vY3kGGOo1gYfUrfQXP'

accessToken = '1139133600165613569-nc0GgYl8ywKyvfQcEPDArUJEzxQ6YO'
accessTokenSecret = 'WoOXeCSFwOi3MvBUkcVuOn4FYMdJyNWyMgma0ycYBFwid'

a = tweepy.OAuthHandler(consumerKey, consumerKeySecret)

a.set_access_token(accessToken, accessTokenSecret)

api = tweepy.API(a)

Tweets = api.search('@MarvelStudios')

p=0
n=0

for t in Tweets:	
	an = TextBlob(t.text)

	if an.sentiment[0]>0:
		p+=1
	else:
		n+=1

print("Positive tweets :%d "%(p))
print("Negative tweets :%d "%(n))
