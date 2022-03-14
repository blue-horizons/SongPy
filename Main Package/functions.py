
# Globals

global json_file
global accounts
global usernames
global songList
global clear

import json
import os
import time
from random import randint
from sys import platform

# Sets clear command to `clear` if MacOS or Linux, or `cls` if Windows
if platform == "linux" or platform == "linux2" or platform == "darwin":
    clear = "clear"
elif platform == "win32":
    clear = "cls"

os.system("pip install simple_chalk") # Installs simple_chalk library
os.system(clear)

from simple_chalk import *


# Starting Variables
valid_user = False
valid_pwd = False
usernames = []

###############################################################

# Functions
def clearAll():
    os.system(clear) # Clears Terminal

def pad(string, max_, paddingChar=" "):
    # Pads a string with a certain amount of 
    # characters, or truncuates the string to 
    # a certain length.

    max_=int(max_)
    if len(string) > max_:
        string = string[0:max_]
    elif len(string) < max_:
        padding = max_ - len(string)
        for i in range(0,padding):
            string += " "
    return string

def createUser():
    password_valid =False
    new_username = input("New Username \n> ")
    while not password_valid:
        new_password = input("New password \n> ")
        clearAll()
        confirm_pwds = input("Confirm Password \n> ")
        clearAll()
        if new_password != confirm_pwds:
            print(red("Passwords don't match. Try again."))
            time.sleep(1)
            clearAll()
        else:
            accounts[new_username] = confirm_pwds
            password_valid = True
            with open("accounts.json","w") as f:
                json.dump(accounts,f)
            usernames.append(new_username)

def login(): 
    valid_user = False
    valid_pwd = False
    while not valid_user:
        print(f"""
 __________________
| ________________ |
|| {bold("LOG IN:")}        ||
|| UserName:      ||
|| ██████████████ ||
|| Pwd:           ||
|| ██████████████ ||
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
|__________________|""")
        username = input("U > ")
        if username not in usernames:
            print(f"""
 __________________
| ________________ |
|| {red("Your account")}   ||
|| {red("doesn't exist.")} ||
|| Create a new   ||
|| one?           ||
||            {yellow("y/N")} ||
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
|__________________|""")
            time.sleep(1)
            clearAll()
            print(f"""
 __________________
| ________________ |
||                ||
|| Do you want to ||
|| create a new   ||
|| account?       ||
||            {yellow("y/N")} ||
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
|__________________|""")
            newUser = input("> ")
            if newUser.lower() == "y":
                createUser()
            else:
                quit()
        else:
            valid_user = True

    while not valid_pwd:
        clearAll()
        print(f"""
 __________________
| ________________ |
|| {bold("LOG IN:")}        ||
|| UserName:      ||
|| {green(pad(username,14,paddingChar="█"))} ||
|| Pwd:           ||
|| ██████████████ ||
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
|__________________|""")
        # print("Username")
        # print("> " + green(username))
        # print("P > ")
        password = input("P > ")
        if  password != accounts.get(username):
            print(f"""
 __________________
| ________________ |
||                ||
|| {red("Incorrect")}      ||
|| {red("Password.")}      ||
|| {red("Try Again.")}     ||
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
|__________________|""")
            time.sleep(1)
            clearAll()
        else:
            valid_pwd = True
            clearAll()
            print(f"""
 __________________
| ________________ |
||                ||
|| {green("Correct")}      ||
|| {green("Password.")}      ||
||                ||
||   {brightGreen("LOGGED  IN")}   ||
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
|__________________|""")

def set_ans():
    with open("songs.csv", "r"):
        randomLine = random.randint(1,max(songList))
        songAns_pick = randomLine[1]
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
    

