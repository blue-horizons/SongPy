import random
import csv
import time
from os import system as command

# from simple_chalk import *

global screenWidth
screenWidth = 32

sleep = 5


def green(string):
    return u"\u001b[32m" + string + u"\u001b[0m"
def red(string):
    return u"\u001b[31m" + string + u"\u001b[0m"

global battery
battery =  green("▊▊▊")

game = True

def pad(string, max_=screenWidth, paddingChar=" ",alignment="l"):
    # Pads a string with a certain amount of
    # characters, or truncuates the string to
    # a certain length.

    max_ = int(max_)
    if len(string) > max_:
        string = string[0:max_]
    elif len(string) < max_:
        padding = max_ - len(string)
        for i in range(0, padding):
            string += " "
    return string

with open("Tests/songs.csv") as f:
    artists = []
    songNames = []
    reader = csv.reader(f)
    var = list(reader)
    for i in range(1, len(var)):
        songNames.append(var[i][0])
        artists.append(var[i][1])

def jPod(line1,line2=" ",line3=" ",line4=" ",line5=" ",line6=" ",line7=" ",line8=" ",line9=" ",line10=" ",genAlign="left",print_=False):
    lines = []
    outLines = []

    empty_space = "                              " # END

    lines.append(line1)
    lines.append(line2)
    lines.append(line3)
    lines.append(line4)
    lines.append(line5)
    lines.append(line6)
    lines.append(line7)
    lines.append(line8)
    lines.append(line9)
    lines.append(line10)

    for i in lines:
        outLines.append(pad(i))

    # Usable Width = 30
    jpod = f"""
╭────────────────────────────────────╮
│ ╭────────────────────────────────╮ │
│ │              jPod        │{battery}] │ │
│ ├────────────────────────────────┤ │
│ │{outLines[0]}│ │
│ │{outLines[1]}│ │
│ │{outLines[2]}│ │
│ │{outLines[3]}│ │
│ │{outLines[4]}│ │
│ │{outLines[5]}│ │
│ │{outLines[6]}│ │
│ │{outLines[7]}│ │
│ │{outLines[8]}│ │
│ │{outLines[9]}│ │
│ ╰────────────────────────────────╯ │
│  jPod                              │
│                                    │
│           _____________            │
│          /\    MENU    /\          │
│         /  \          /  \         │
│        /    \        /    \        │
│       |      \______/      |       │
│       |      /      \      |       │
│       |  ◄◄ |        | ►►  |       │
│       |      \______/      |       │
│       |      /      \      |       │
│        \    /        \    /        │
│         \  /  ► / ||  \  /         │
│          \/____________\/          │
│                                    │
│                                    │
╰────────────────────────────────────╯
"""
    if print_ == False:
        return jpod
    else: 
        print(jpod)


def chooseSong():
    song_words = []
    randNum = random.randint(0, len(songNames)-1)
    picked_song = songNames[randNum]
    picked_artist = artists[randNum]

    output_song = ""

    song = picked_song

    output_song = (" ".join(word[0] + "_"*(len(word)-1) for word in song.split()))
    
    output = [picked_song,picked_artist,output_song]
    return output



while game == True:
    command("clear")

    lifeNum = 3
    score = 0

    output = chooseSong()
    picked_song = output[0].lower()

    jPod(f"Score:    {score}",line7="Guess the Song:",line8=f"{output[2]}",line9=f" by {output[1]}",print_=True)
    guess = input("> ").lower()

    if guess == picked_song:
        jPod("",line5 = green(output[0]),line6=green("Correct!"))
        if lifeNum == 3:
            score += 2
        else:
            score += 1
        
    elif guess != picked_song:
        jPod(red("Incorrect Song"))
        time.sleep(sleep)
        if battery == "▊▊▊":
            battery = "▊▊ "
        elif battery == "▊▊ ":
            battery = "▊  "
        elif battery == "▊  ":
            battery = "   "
            break

jPod(red("GAME OVER"))
time.sleep(sleep)
