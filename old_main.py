import csv
import os
import platform
import random
import sqlite3
from getpass import getpass, getuser

os.system("pip install simple_chalk && clear")
from simple_chalk import *

# # Open songList file
SONG_CSV = open("songs.csv", "r")
songFile = SONG_CSV.readlines()

if platform.system().lower()== "linux" or platform.system().lower()=="Darwin":
    clear = "clear"
else:
    clear = "cls"

run = True
login = False
menu = True
diffuculty = 1 # Default Difficulty

accountDB = open("accounts.sql","r")


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

def errorScreen(errorNumber):
    os.system(clear)
    print(f"""
 __________________
| ________________ |""")
print("||" + red("ERROR: {errorNumber}")+ """       ||
||        !       ||
||      #~~#      ||
||                ||
||                ||
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
""")

def pad(string, max_, paddingChar=" "):
    max_=int(max_)
    if len(string) > max_:
        string = string[0:max_]
    elif len(string) < max_:
        padding = max_ - len(string)
        for i in range(0,padding):
            string += " "
    return string

def login():
    username = getuser()
    if username in row[0] == False:
        errorScreen(1)
    else:
        menu = True
        loginStatus = username




while menu:
    if login == False:
        loginStatus = "Log In     "
    os.system(clear)

    login()

    if login == False:
        loginStatus = red("Log In       L")
    else:
        loginStatus = pad(userName, 11) + "  A"
        loginStatus = yellow(loginStatus)
    option = input("> ")

    print(""" __________________
| ________________ |""")
    print("|| " + green("New Game     N ") + "||")
    print("||                ||")
    print("|| " + blue("Difficulty   D") + " ||")
    print("||                ||")
    print(f"|| {loginStatus} ||")
    print("""||________________||)
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
""")

while run:
    RunLoop

    



