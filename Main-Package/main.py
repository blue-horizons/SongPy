# Imports

from imports import *
from functions import *



# Globals

global json_file
global accounts
global usernames
global songList

# Starting Variables
valid_user = False
valid_pwd = False
usernames = []
accounts = []
loginStatus = "Log In       L"




# UserScreen Interface
userScreen = f"""
 __________________
| ________________ |
|| {green("New Game     N ")}||
||                ||
|| {blue("Difficulty   D")} ||
||                ||
|| {yellow(loginStatus)} ||
||________________||
| jpod             |
|       ______     |
|      /\    /\    |
|     /  \__/  \   |
|    |   /  \   |  |
|    |   \__/   |  |
|     \  /  \  /   |
|      \/____\/    |
|                  |
|__________________|
"""



#######################

songList = open("Main-Package/songs.csv","r")

#######################
# FUNCTIONS WERE HERE #
#######################


# Menu Loop
menu = True
while menu:
    print(userScreen)
    choice = input("> ")
    if choice.lower() == "n":
        clearAll()
        print(green("Running New Game... "))
        menu = False
        runGame = True
    elif choice.lower() == "l":
    #     print(green("Opening Settings... "))
    #     setting_state = True
    # elif choice.lower() == "c":
        print(green("Running Login... "))
        clearAll()
        login() # Runs login Screen

while runGame:
    print(set_ans())
    while wrongAns != 2:
        for i in range(0,1):
            input(guess)
            if guess != answer:
                correctGuess = False
                wrongAns += 1
                if wrongAns == 2:
                    print(red("Too many guesses:"))
                    clearAll()
                    print(gameOver)
                    break

            else:
                correctGuess = True
                i += 1
                if i == 0:
                    score += 3
                elif i == 1:
                    score += 1
    
    rungame = False
