# Imports

from imports import *
from functions import *


# Globals

global json_file
global accounts
global usernames
global username
global songList
global loginStatus

# Starting Variables
valid_user = False
valid_pwd = False
usernames = []
accounts = []
username = ""
loginState = False
loginStatus = "Log In       L"

# UserScreen Interface

def userScreen(login_status):
    login_status = pad(loginStatus,14)
    return f"""
New Game     N 
Create Acc.  C
{login_status}
"""


#######################


songList = open("Main-Package/songs.csv", "r")

# Starting Variables
valid_user = False
valid_pwd = False
usernames = []
accounts = []
passwords = []


###############################################################

def login():
    with open("Main-Package/accounts.csv", "r") as f:
        passwords = []
        usernames = []
        reader = csv.reader(f)
        var = list(reader)
        for i in range(1, len(var)):
            usernames.append(var[i][0])
            passwords.append(var[i][1])
    valid_user = False
    valid_pwd = False

    while not valid_user:
        clearAll()
        print(f"""
 __________________
| ________________ |
||                ||
|| {Blue("Enter Username")} ||
||                ||
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
|__________________|""")
        username = input("> ")
        clearAll()
        if username not in usernames:
            print(f"Create New Account? y/N")

            print(f"""
 __________________
| ________________ |
||                ||
|| {blue("Create Account")} ||
||                ||
||                ||
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
            choice = input("> ")
            clearAll()
            if choice.lower() == "y":
                createUser()
            else:
                valid_user = False

        else:
            while not valid_pwd:
                clearAll()
                print(f"""
 __________________
| ________________ |
||                ||
|| {yellow("Password:")}      ||
||                ||
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
|__________________|""")
                password = input("> ")
                if password != passwords[usernames.index(username)]:
                    print(f"""
 __________________
| ________________ |
||                ||
|| {red("Incorrect")}      ||
||  {red("Password")}      ||
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
|__________________|""")
                    time.sleep(3)
                    clearAll()
                    return False
                else:
                    print(f"""
 __________________
| ________________ |
||                ||
|| {green("Correct")}        ||
||  {green("Password")}      ||
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
|__________________|""")
                    valid_pwd = True
                    return True
                    break

def createUser():
    password_valid = False
    print(f"""
 __________________
| ________________ |
||                ||
||  {yellow("New Username")}  ||
||                ||
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
|__________________|""")
    new_username = input("> ")
    while not password_valid:
        clearAll()
        print(f"""
 __________________
| ________________ |
||                ||
||  New Password  ||
||                ||
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
|__________________|""")
        new_password = input("> ")
        clearAll()
        print(f"""
 __________________
| ________________ |
||                ||
||    {yellow("Confirm")}     ||
||    {yellow("Password")}    ||
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
|__________________|""")
        confirm_pwds = input("> ")
        clearAll()
        if new_password != confirm_pwds:
            print(f"""
 __________________
| ________________ |
||                ||
|| {red("Passwords Dont")} ||
||     {red("match")}      ||
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
|__________________|""")
            time.sleep(1)
            clearAll()
        else:
            print(f"""
 __________________
| ________________ |
||                ||
|| {green("Account")}        ||
||  {green("Created")}       ||
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
|__________________|""")
            password_valid = True
            newCreds = [new_username, new_password]
            with open("Main-Package/accounts.csv", "a") as f:
                f.write(f"\n{new_username},{new_password}")
            usernames.append(new_username)

#######################

# MAIN CODE

# Menu Loop
menu = True
while menu:
    clearAll()
    print(userScreen(loginStatus))
    choice = input("> ")

    if choice.lower() == "n": # New Game
        clearAll()
        print(green("Running New Game... "))
        menu = False
        runGame = True
        break

    elif choice.lower() == "c":
        print(yellow("Creating new Account..."))
        createUser()

    elif choice.lower() == "l": # Log in/ Log out.

        print(green("Running Login... "))
        clearAll()
        while not loginState:
            loginState = login()  # Runs login Screen

        if loginState == True:
            loginStatus = "Log Out      L"
        else:
            loginState = False
            loginStatus = "Log In       L"



while runGame:
    print(set_ans())
    while wrongAns != 2:
        for i in range(0, 1):
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