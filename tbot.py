#!/usr/bin/env python
# -*- coding: utf-8 -*-

import tweepy
import time
import sys

CONSUMER_KEY = 'fZH6HUEvs8XqLH7vNQAJL3HiC'
CONSUMER_SECRET = 'BOkmyn1gVGjaZmjJOJJ1MvY9PV78CqvLpCE0VSeHiSWBw8KPuU'
ACCESS_KEY = '3073859186-GpQyaGJMm9HoR7WZ7s7ftUqzl86oJyTYVZoeZPT'
ACCESS_SECRET = 'MVDjEFkeuyscXNCbRhOppvjlwxMIhfSR9JYdVRwIH7fX4'

argfile = str(sys.argv[1])

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

filename=open(argfile,'r')
f=filename.readlines()
filename.close()

for line in f:
    api.update_status(status=line)
    time.sleep(2900)
