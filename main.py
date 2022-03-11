# Imports

import os
import time
from getpass import getpass, getuser
import json
from simple_chalk import green, red

# Globals

global json_file
global accounts
global usernames
global songList

# Starting Variables
valid_user = False
valid_pwd = False
usernames = []

# File Opening
json_file = open('accounts.json')
accounts = json.load(json_file)
for i in accounts.keys():
    usernames.append(i)

songList = open("songs.csv","r")

# Functions

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
        os.system("clear")
        confirm_pwds = input("Confirm Password \n> ")
        os.system("clear")
        if new_password != confirm_pwds:
            print(red("Passwords don't match. Try again."))
            time.sleep(1)
            os.system("clear")
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
        print("Username")
        username = input("> ")
        if username not in usernames:
            print("Your account doesn't exist")
            time.sleep(1)
            os.system("clear")
            print("""Do you want to create a new User?
y/N
""")
            newUser = input("> ")
            if newUser.lower() == "y":
                createUser()
            else:
                quit()
        else:
            valid_user = True

    while not valid_pwd:
        os.system("clear")
        print("Username")
        print("> " + green(username))
        print("Password")
        password = input("> ")
        if  password != accounts.get(username):
            print(red("Incorrect Password"))
            time.sleep(1)
            os.system("clear")
        else:
            valid_pwd = True
            os.system("clear")
            print(green("Correct Password"))

def set_ans():
    with open("songs.csv", "r"):
        randomLine = random.randint(1,len(songList))
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
    


# Main Code
menu = True
while menu:
    choice = input("A/B > ")
    if choice.lower() == "a":
        print(green("Running New Game... "))
        menu = False
        runGame = True
    elif choice.lower() == "b":
    #     print(green("Opening Settings... "))
    #     setting_state = True
    # elif choice.lower() == "c":
        print(green("Running Login... "))
        login() # Runs login Screen

while runGame:
    set_ans()
    while wrongAns != 2:
        for i in range(0,1):
            input(guess)
            if guess != answer:
                correctGuess = False
                wrongAns += 1
            else:
                correctGuess = True
                i += 1
                if i == 0:
                    score += 3
                elif i == 1:
                    score += 1
    rungame = False
