#!/usr/bin/env python3.4
# Encoding: Utf-8
import random
from collections import OrderedDict, deque
import keys  # create a keys.py file with your twitter tokens if you want to run your own instance !
import logging
import json
from TwitterAPI import TwitterAPI, TwitterRequestError
logging.basicConfig(filename="/tmp/coffebot.log", level=logging.INFO)

coffeeFile  = open("coffeeType.json")
coffeeTypes = json.load(coffeeFile)
intro       = coffeeTypes['intro']
multi       = coffeeTypes['multi']
size        = coffeeTypes['size']
coffee      = coffeeTypes['coffee']
attribute   = coffeeTypes['attribute']
syrup_type  = coffeeTypes['syrup_type']
syrup       = coffeeTypes['syrup']
appendition = coffeeTypes['appendition']

pick = input("Main/daily")
if pick == "Main"
def order():
    order = OrderedDict()
    order[random.choice(multi)] = True
    for i in range(random.randint(0,5)):
        order[random.choice(attribute)] = True
    order[random.choice(size)] = True
    order[random.choice(coffee)] = True
    order[random.choice(syrup_type)] = True
    order[random.choice(syrup)] = True
    for i in range(random.randint(0,2)):
        order[random.choice(appendition)] = True
    return " ".join(" ".join(order.keys()).split())

def make_tweet(username):
    while True:
        a, b = random.choice(intro)
        o = u"@"+username+" "+a+" "+order()+" "+b
        if len(o) < 140:
            return o

logging.info("Connecting to Twitter API")
api = TwitterAPI(keys.consumer_key, keys.consumer_secret, keys.access_token_key, keys.access_token_secret)
bot = api.request('account/verify_credentials').json()["screen_name"]
msgs = deque(maxlen=1000)  # we keep the last 1000 messages and do not reply to those again
logging.info("Connected")
try:
    for msg in api.request('user', {'replies': 'all'}):
        logging.info("New event")
        logging.debug(msg)
if pick == "Daily"
def order():
    order = OrderedDict()
    order[random.choice(multi)] = True
    for i in range(random.randint(0,5)):
        order[random.choice(attribute)] = True
    order[random.choice(size)] = True
    order[random.choice(coffee)] = True
    order[random.choice(syrup_type)] = True
    order[random.choice(syrup)] = True
    for i in range(random.randint(0,2)):
        order[random.choice(appendition)] = True
    return " ".join(" ".join(order.keys()).split())

def make_tweet():
    while True:
        o = u"Coffee of the day :\n"+order()
        if len(o) < 140:
            return o

logging.info("Connecting to Twitter API")
api = TwitterAPI(keys.consumer_key, keys.consumer_secret, keys.access_token_key, keys.access_token_secret)
bot = api.request('account/verify_credentials').json()["screen_name"]
logging.info("Connected")

try:
    logging.info("Sending COTD")
    t = make_tweet()
    r = api.request('statuses/update', {'status' : t})
    logging.info("COTD with status : {}".format(r.status_code))
    logging.info("Done !")
except TwitterRequestError as e:
    logging.exception(e)
