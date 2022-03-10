import csv
import random
from simple_chalk import *
import os

# # Open songList file
SONG_CSV = open("songs.csv", "r")
songFile = songFile.readlines()

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
    



