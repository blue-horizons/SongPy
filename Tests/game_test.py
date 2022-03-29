import random

game = True

with open("songs.csv") as songFile:
    artists = []
    songNames = []
    reader = csv.reader(f)
    var = list(reader)
    for i in range(1, len(var)):
        artists.append(var[i][0])
        songNames.append(var[i][1])

def chooseSong():
    randNum = random.randint(0, len(songNames))
    picked_song = songNames[randNum]
    picked_artist = artists[randNum]

    output_song = ""

    for i in picked_song:
        if i == 0 or picked_song[i-1] == " ":
            output_song += i
        else:
            output_song += "_"
    
    print(f"Song: {output_song}; Artist: {picked_artist}")
    
while game:
    tryNum = 0
    chooseSong()
    print(f"Guess the song:          {tryNum}")
    guess = input("> ")
    if guess == picked_song and tryNum == 0:
        print("Correct Song!")
        score += 2
        
    elif guess != picked_song and tryNum < 2:
        print("Incorrect Song")
        score += 1
        tryNum += 1
    elif tryNum == 2:
        print("Incorrect Song")
        game = False
    
