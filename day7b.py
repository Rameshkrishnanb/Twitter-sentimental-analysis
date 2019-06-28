#!/usr/bin/env python

import tweepy
from textblob import TextBlob

from prettytable import PrettyTable


consumerKey = '0NiduTn5vlz9rsDrpaVV7E65v'
consumerKeySecret = 'LRGvbSuBcO7QjbTWPrfImZ845gzVQIV7vY3kGGOo1gYfUrfQXP'

accessToken = '1139133600165613569-nc0GgYl8ywKyvfQcEPDArUJEzxQ6YO'
accessTokenSecret = 'WoOXeCSFwOi3MvBUkcVuOn4FYMdJyNWyMgma0ycYBFwid'

a = tweepy.OAuthHandler(consumerKey, consumerKeySecret)

a.set_access_token(accessToken, accessTokenSecret)

api = tweepy.API(a)

acc=['@narendramodi','@RahulGandhi']
t1 = PrettyTable()
t1.field_names = ["account name", "Followers","Tweets","Positive Tweets","Negative Tweets","Neutral Tweets"]
	
for i in range (len(acc)):
	Tweets = api.search(acc[i])
	f= api.get_user(acc[i]).followers_count

	p=0
	n=0
	m=0
	for t in Tweets:	
		an = TextBlob(t.text)

		if an.sentiment[0]>0:
			p+=1
		elif an.sentiment[0]==0:
			m+=1
		else:
			n+=1
	s=p+n+m
	
	
	t1.add_row([acc[i],f,s,p,n,m])
print (t1)
