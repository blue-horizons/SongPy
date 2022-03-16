
# Globals

from imports import *
global accounts
global usernames
global username
global songList
global clear
global passwords


# Open `accounts.csv`

songList = open("Main-Package/songs.csv", "r")

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
        for i in range(1, len(var)):
            usernames.append(var[i][0])
            passwords.append(var[i][1])

def setSong():
    with open("Main-Package/songs.csv", "r") as f:
        reader = csv.reader(f)
        var = list(reader)
        for i in range(1, len(var)):
            songs.append(var[i][0])
            artists.append(var[i][1])


def setClear():
    # Sets clear command to `clear` if on MacOS or Linux,
    #   or `cls` if on Windows
    if platform == "linux" or platform == "linux2" or platform == "darwin":
        clear = "clear"
    elif platform == "win32":
        clear = "cls"
    return clear


def clearAll():
    os.system(setClear())  # Clears Terminal


def pad(string, max_, paddingChar=" "):
    # Pads a string with a certain amount of
    # characters, or truncuates the string to
    # a certain length.

    max_ = int(max_)
    if len(string) > max_:
        string = string[0:max_]
    elif len(string) < max_:
        padding = max_ - len(string)
        for i in range(0, padding):
            string += " "
    return string

def set_ans():
    
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
