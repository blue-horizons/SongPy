import random
import csv
from os import system as command
# from simple_chalk import *

lives = "♥ ♥ ♥"

def green(string):
    return u"\u001b[32m" + string + u"\u001b[0m"
def red(string):
    return u"\u001b[31m" + string + u"\u001b[0m"

game = True

with open("songs.csv") as f:
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
            output_song += " " + i
            count += 1
        else:
            output_song += "_"
        count += 1
    
    output = [picked_song,picked_artist,output_song]
    return output

command("cls")

while game == True:
    command("cls")

    lifeNum = 3
    score = 0

    output = chooseSong()
    picked_song = output[0].lower()

    print(f"""Lives: {lives}
    Score: {score}
    Guess the song: 
    "{output[2]}" by {output[1]}
    """)
    guess = input("> ").lower()
    if guess == picked_song:
        print(green("Correct Song!"))
        if lifeNum == 3:
            score += 2
        else:
            score += 1
        
    elif guess != picked_song:
        print(red("Incorrect Song"))
        if lives == "♥ ♥ ♥":
            lives = "♥ ♥"
        elif lives == "♥ ♥":
            lives = "♥"
        elif lives == "♥":
            lives = ""
            break

print(red("GAME OVER"))

