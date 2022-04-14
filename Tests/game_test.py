import random
import csv
from os import system as command
from simple_chalk import *

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
    song_words = []
    randNum = random.randint(0, len(songNames))
    picked_song = songNames[randNum]
    picked_artist = artists[randNum]

    output_song = ""

    count = 0
    song_words = picked_song.split()
    for i in song_words:
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


while game == True:
    print(123456)
    lifeNum = 3
    score = 0

    output = chooseSong()
    picked_song = output[0].lower()

    print(f"""Lives: {lifeNum}
    Score: {score}
    Guess the song: 
    "{output[2]}" by {output[1]}
    """)
    guess = input("> ").lower()
    # command("clear")
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
    