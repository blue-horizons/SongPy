
# Globals

global accounts
global usernames
global songList
global clear
global passwords

from imports import *

# Open `accounts.csv`

songList = open("Main-Package/songs.csv","r")

# Starting Variables
valid_user = False
valid_pwd = False
usernames = []
accounts = []
passwords = []


###############################################################

# Functions

def setFile():
    with open("Main-Package/accounts.csv", "r") as f:
        reader = csv.reader(f)
        var = list(reader)
        for i in range(1,len(var)):
            usernames.append(var[i][0])
            passwords.append(var[i][1])


def setClear():
    # Sets clear command to `clear` if on MacOS or Linux, 
    #   or `cls` if on Windows
    if platform == "linux" or platform == "linux2" or platform == "darwin":
        clear = "clear"
    elif platform == "win32":
        clear = "cls"
    return clear


def clearAll():
    os.system(setClear()) # Clears Terminal

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
    print("New Username")
    new_username = input("> ")
    while not password_valid:
        clearAll()
        print("New Password")
        new_password = input("> ")
        clearAll()
        print("Confirm Password")
        confirm_pwds = input("> ")
        clearAll()
        if new_password != confirm_pwds:
            print("passwords dont match")
            time.sleep(1)
            clearAll()
        else:
            password_valid = True
            newCreds = [new_username,new_password]
            with open("Main-Package/accounts.csv","a") as f:
                f.write(f"\n{new_username},{new_password}")

def login():
    with open("Main-Package/accounts.csv", "r") as f:
        passwords = []
        usernames = []
        reader = csv.reader(f)
        var = list(reader)
        for i in range(1,len(var)):
            usernames.append(var[i][0])
            passwords.append(var[i][1])
    valid_user = False
    valid_pwd = False

    while not valid_user:
        clearAll()
        print(f"""
 __________________
| ________________ |
|| {bold("LOG IN:")}        ||
|| {bold("Username:")}      ||
|| ██████████████ ||
|| {bold("Password:")}      ||
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
        username = input("> ")
        clearAll()
        if username not in usernames:
            print(f"""
 __________________
| ________________ |
|| {red("This account")}   ||
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
|| {bold("LOG IN:")}        ||
|| {bold("Username:")}      ||
|| {green(pad(username,14,paddingChar="█"))} ||
|| {bold("Password:")}      ||
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
                password = input("> ")
                if password != passwords[usernames.index(username)]:
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
                    time.sleep(3)
                    clearAll()
                else:
                    print("Correct Password")
                    valid_pwd = True
                    loginStatus = username
                    break

def set_ans():
    with open("Main-Package/songs.csv", "r"):
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
    

