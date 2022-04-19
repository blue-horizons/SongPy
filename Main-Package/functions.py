# IMPORTS
import csv
import json
import os
import random
import time
from getpass import getpass, getuser
from sys import platform
import colours

# GLOBALS

global accounts
global usernames
global username
global songList
global clear
global passwords
global screenWidth


# Open `songs.csv`

songList = open("Main-Package/songs.csv", "r")

# Starting Variables
valid_user = False
valid_pwd = False
usernames = []
accounts = []
passwords = []
screenWidth = 38


###############################################################

# Functions

def setFile():
    with open("Main-Package/accounts.csv", "r") as f:
        reader = csv.reader(f)
        var = list(reader)
        for i in range(1, len(var)):
            usernames.append(var[i][0])
            passwords.append(var[i][1])

def setSong():
    with open("Main-Package/songs.csv", "r") as f:
        reader = csv.reader(f)
        var = list(reader)
        for i in range(1, len(var)):
            songs.append(var[i][0])
            artists.append(var[i][1])

def pause(length):
    time.sleep(length)

def setClear():
    # Sets clear command to `clear` if on MacOS or Linux,
    #   or `cls` if on Windows
    if platform == "linux" or platform == "linux2" or platform == "darwin":
        clear = "clear"
    elif platform == "win32":
        clear = "cls"
    return clear


def clearAll():
    os.system(setClear())  # Clears Terminal


def set_ans():
    songAns_pick = (songs)
    for i in range(0, len(songAns_pick)):

        if songAns_pick[i] == " ":
            out_Ans += " "
            out_Ans += songAns_pick[i+1]
            i += 2
        elif i == 0:
            out_Ans += songAns_pick[0]
            i += 1
        else:
            out_Ans += "_"
            i += 1

    output = blue(f"Song: {out_Ans}") + "\n" + f"Artist: {randomLine[0]}"
    return output
