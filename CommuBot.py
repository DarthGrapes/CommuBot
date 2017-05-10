import os
import time
from markovbot import MarkovBot

tweetbot = MarkovBot()

dirname = os.path.dirname(os.path.abspath(__file__))
book = os.path.join(dirname, 'Communist_Manifesto.txt')
tweetbot.read(book)

my_first_text = tweetbot.generate_text(25, seedword=['communist', 'bourgoise'])
print("tweetbot says: ")
print(my_first_text)

cons_key = '' #Twitter access tokens go here
cons_secret = '' #Twitter access tokens go here
access_token = '' #Twitter access tokens go here
access_token_secret = '' #Twitter access tokens go here

tweetbot.twitter_login(cons_key, cons_secret, access_token, access_token_secret)

targetstring = '#KarlMarx'
keywords = ['communism', 'bourgoise', 'proleterian', 'proleteriat', 'marx', 'socialism']
prefix = 'Karl Marx Here!'
suffix = '#BleepBloop'
maxconvdepth = 2

tweetbot.twitter_autoreply_start(targetstring, keywords=keywords, prefix=prefix, suffix=suffix, maxconvdepth=maxconvdepth)
tweetbot.twitter_tweeting_start(days=0, hours=1, minutes=0, keywords=None, prefix=None, suffix=None)

secsinweek = 7 * 24 * 60 * 60
time.sleep(secsinweek)

tweetbot.twitter_autoreply_stop()
tweetbot.twitter_tweeting_stop()
