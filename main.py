import csv
import random
from simple_chalk import *
import os
import platform
import sqlite3

# # Open songList file
SONG_CSV = open("songs.csv", "r")
songFile = songFile.readlines()
run = True
login = False
diffuculty = 1 # Default Difficulty

accountDB = open("accouts.sql","r")


def setGuess(songList):
    # Picks random song
    songChoice = random.randint(1, max(songFile))

    for i in len(songChoice[1]):
        if i == 0:
            ques1 += songChoice[i]
        elif songChoice[i] == " ":
            i += 1
            ques1 += yellow(songChoice[i])
        else:
            ques1 += red("_")
        i += 1
    return ques1

while menu:
    if login == False:
        loginStatus = "Log In        "
    if platform.system().lower()== "linux" or platform.system().lower()=="Darwin":
        os.system("clear")
    else:
        os.system("cls")
    print(f"""
 ___________________
| _________________ |
||""" + "green( New Game      N )" +"""||
||                 ||
||""" + blue(f" Difficulty {diffuculty}  D") + """ ||
||                 ||
|| """ + {loginStatus} L ||
||_________________||
| jPod              |
|      _______      |
|     /\     /\     |
|    /  \___/  \    |
|   |   /   \   |   |
|   |   \___/   |   |
|    \  /   \  /    |
|     \/_____\/     |
|                   |
|___________________|""")

while run:
    RunLoop

    



