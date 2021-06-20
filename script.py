#!/usr/bin/env python

# Fastest Kahoot Spammer In The World!

# Made By SkiBop!
# https://github.com/skibop
# Contact Me! - haxxd#0001

from kahoot import client
import string
import random
import time
import threading
import json
import os
import time

bot = client()

if os.path.exists(os.getcwd() + "./config.json"):
    
    with open("./config.json") as f:
        configData = json.load(f)
    
else:
    configTemplate = {"gameid": "", "botamount": "", "custom_usr": ""}
    
    with open(os.getcwd() + "./config.json", "w+") as f:
        json.dump(configTemplate, f)

gameid = configData["gameid"]
botamount = configData["botamount"]
custom_usr = configData["custom_usr"]

def spamjoin():
    def joingame():

        usrname = (custom_usr + str(random.randint(1, 10000)))

        bot.join((gameid), usrname)

        def joinHandle() :
            pass

        bot.on("joined", joinHandle)
        print(f"Joined game {gameid} with username {usrname}.")

    for x in range(0, (int(botamount) )) : 
        joingame()
    time.sleep(0.3)

threads = []

for i in range(50):
    t = threading.Thread(target=spamjoin)
    t.daemon = True
    threads.append(t)

for i in range(50):
    threads[i].start()

for i in range(50):
    threads[i].join()
