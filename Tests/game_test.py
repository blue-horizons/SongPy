import random
import csv
from os import system as command
from simple_chalk import *

global lives
global screenWidth

def pad(string, max_=screenWidth, paddingChar=" ",alignment="l"):
    max_ = int(max_)
    if len(string) > max_:
        string = string[0:max_]
    elif len(string) < max_:
        padding = max_ - len(string)
        for i in range(0, padding):
            string += " "
    return string

def jPod(line1="",line2=" ",line3=" ",line4=" ",line5=" ",line6=" ",line7=" ",line8=" ",line9=" ",line10=" ",genAlign="left",print_=False):
    battery = lives
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

game = True

with open("Tests/songs.csv") as f:
    artists = []
    songNames = []
    reader = csv.reader(f)
    var = list(reader)
    for i in range(1, len(var)):
        songNames.append(var[i][0])
        artists.append(var[i][1])

def chooseSong():
    randNum = random.randint(0, len(songNames))
    picked_song = songNames[randNum]
    picked_artist = artists[randNum]

    output_song = ""

    
    count = 0
    for i in picked_song:
        if count == 0:
            output_song += i
        elif i == " ":
            output_song += " "
            count = 0
        else:
            output_song += "_"
        count += 1
    
    jpod("line")
    output = [picked_song,picked_artist]
    return output

command("clear")

while game:
    lifeNum = 3
    score = 0

    output = chooseSong()
    picked_song = output[0].lower()

    print(f"Guess the song:          Lives: {lifeNum}        Score:{score}")
    guess = input("> ").lower()
    command("clear")
    if guess == picked_song:
        print(green("Correct Song!"))
        if lifeNum == 3:
            score += 2
        else:
            score += 1
        
    elif guess != picked_song:
        print(red("Incorrect Song"))
        lifeNum = lifeNum - 1
    if lifeNum == 0:
        game = False
    
