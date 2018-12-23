import requests as rq
import tweepy
import time

######KEYS SETUP############

consumer_key="pzARlvZ1U6Uwp5ulHNwtljlIG"
consumer_secret="4OpAXEZvpI2PMR5PqpzZGvpkWzg1RRhhZeGRXYDxqmBCARoSPA"
access_token="1056428604257681408-LqNLE5hn2WAph89ldZsBre8KzVyWFx"
access_token_secret="d9goxNQ2SXGvO9bPrXuPAZicdG8by2f5OkWXNXxp9Lbxm"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

############################

api.update_status('Hello wo')