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
import os
import time

bot = client()

gameid = input('Enter the game pin: ')
botamount = 100
custom_usr = input('Enter the desired username for your bots: ')

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
    time.sleep(0.2)

threads = []

for i in range(10):
    t = threading.Thread(target=spamjoin)
    threads.append(t)

for i in range(10):
    threads[i].start()

for i in range(10):
    threads[i].join()
