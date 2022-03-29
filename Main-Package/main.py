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
global battery
global screenWidth
global loadingIcons

# Starting Variables
valid_user = False
valid_pwd = False
usernames = []
accounts = []
username = ""
loginState = False
loginStatus = "LOG IN "
battery = green("▊▊▊")
screenWidth = 38
loadingIcons = ["|","/","—","\\","—"]

def pad(string, max_=screenWidth, paddingChar=" ",alignment="l"):
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

# def pad(string,maxLength=screenWidth,padChar=" ",alignment="l"):
#     stringLength = len(string)
#     padding = ""
#     outputString = ""

#     if stringLength < maxLength:
#         difference = maxLength - stringLength
        
#         for i in range(0,difference):
#             padding += padChar

#         if alignment.lower() == "l":
#             outputString += string + padding
#         elif alignment.lower() == "r":
#             outputString += padding + string
#         elif alignment.lower() == "c":
#             if difference % 2 == 1:
#                 padL = difference/2 + 0.5
#                 padR = difference/2 - 0.5
#             else:
#                 padL = difference/2 
#                 padR = difference/2
#             outputString += padL + string + padR

#     elif stringLength > maxLength:
#         outputString += string[0,maxLength]
    
#     return outputString
        
def jPod(line1,line2=" ",line3=" ",line4=" ",line5=" ",line6=" ",line7=" ",line8=" ",line9=" ",line10=" ",genAlign="left",print_=False):
    lines = []
    outLines = []

    empty_space = "                              " # END

    lines.append(line1)
    lines.append(line2)
    lines.append(line3)
    lines.append(line4)
    lines.append(line5)
    lines.append(line6)
    lines.append(line7)
    lines.append(line8)
    lines.append(line9)
    lines.append(line10)

    for i in lines:
        outLines.append(pad(i))

    # Usable Width = 30
    jpod = f"""
╭────────────────────────────────────╮
│ ╭────────────────────────────────╮ │
│ │              jPod        │{battery}] │ │
│ ├────────────────────────────────┤ │
│ │ {outLines[0]} │ │
│ │ {outLines[1]} │ │
│ │ {outLines[2]} │ │
│ │ {outLines[3]} │ │
│ │ {outLines[4]} │ │
│ │ {outLines[5]} │ │
│ │ {outLines[6]} │ │
│ │ {outLines[7]} │ │
│ │ {outLines[8]} │ │
│ │ {outLines[9]} │ │
│ ╰────────────────────────────────╯ │
│  jPod                              │
│                                    │
│           _____________            │
│          /\    MENU    /\          │
│         /  \          /  \         │
│        /    \        /    \        │
│       |      \______/      |       │
│       |      /      \      |       │
│       |  ◄◄ |        | ►►  |       │
│       |      \______/      |       │
│       |      /      \      |       │
│        \    /        \    /        │
│         \  /  ► / ||  \  /         │
│          \/____________\/          │
│                                    │
│                                    │
╰────────────────────────────────────╯
"""
    if print_ == False:
        return jpod
    else: 
        print(jpod)

# USERSCREEN

# UserScreen Interface

def userScreen(login_status):
    login_status = pad(loginStatus,14)
    
    line1 = bold("NEW GAME")
    line2 = pad(bold("> N "))
    line3 = bold("CREATE ACCOUNT")
    line4 = pad(bold("> C "))
    line5 = bold(login_status)
    line6 = pad(bold("> L "))
    line7 = bold("SCOREBOARD")
    line8 = pad(bold("> S "),alignment="r")
    line9 = bold("RESET")
    line10 = pad(bold("> R "),alignment="r")
    return jPod(line1,line2,line3,line4,line5,line6,line7,line8,line9,line10)

def scoreBoard():
    with open("accounts.csv","r") as scores:
        reader = csv.reader(f)
        var = list(reader)
        for i in range(1, len(var)):
            usernames.append(var[i][0])
            scores.append(var[i][3])
    
    lines = []
    for i in range(1, len(usernames)):
        lines.append(f"{i}|{pad(usernames[i])}|{pad(scores[i])}")

    jPod(lines[0],lines[1],lines[3],lines[4],lines[5],lines[6],lines[7],lines[8],lines[9],print_=True)
    


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
        print(jPod(bold(blue("Enter Username "))))
        username = input("> ")
        clearAll()
        if username not in usernames:
            print(jPod(bold(blue("Create New Account?"), line8=yellow("y/N"))))
            choice = input("> ")
            clearAll()
            if choice.lower() == "y":
                createUser()
            else:
                valid_user = False

        else:
            while not valid_pwd:
                clearAll()
                print(jPod(bold(yellow("Enter Password: "))))
                password = input("> ")
                if password != passwords[usernames.index(username)]:
                    for i in range(0,10):
                        for i in loadingIcons:
                            clearAll()
                    print(jPod(bold(red("INCORRECT PASSWORD")), line3 = pad(yellow("Try Again"),align="r")))
                    clearAll()
                    return False
                else:
                    clearAll()
                    print(jPod(green("Correct Password"),line4=blue("Logged In")))
                    valid_pwd = True
                    return True
                    break

def createUser():
    password_valid = False
    print(jPod(yellow("New Username: ")))
    new_username = input("> ")
    while not password_valid:
        clearAll()
        print(jPod(blue("New Password")))
        new_password = input("> ")
        clearAll()
        jPod(yellow("Confirm Password"),genAlign="c",print_=True)
        confirm_pwds = input("> ")
        clearAll()
        if new_password != confirm_pwds:
            for i in range(0,40):
                clearAll()
                jPod(red(Bold("Passwords don't match")), line6=yellow(bold("Try Again")))
                time.sleep(0.1)
                clearAll()
                jPod(bgRed(Bold("Passwords don't match")), line6=bgYellow(bold("Try Again")))
                time.sleep(0.1)
            clearAll()
        else:
            password_valid = True
            newCreds = [new_username, new_password]
            with open("Main-Package/accounts.csv", "a") as f:
                f.write(f"\n{new_username},{new_password},0")
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
        if loginState != True:
            jPod("Sorry, You're not logged in.",line5="Create an account or login",print_=True)
            pause(5)
        else:
            jPod(green("Running New Game... "),print_=True)
            menu = False
            runGame = True
            break

    elif choice.lower() == "c": # Create New Account
        jPod(yellow("Creating New Account..."),print_=True)
        createUser()

    elif choice.lower() == "l": # Log in/ Log out.

        print(green("Running Login... "))
        clearAll()
        while not loginState:
            loginState = login()  # Runs login Screen

        if loginState == True:
            loginStatus = "Log Out"
        else:
            loginState = False
            loginStatus = "Log In "

    elif choice.lower() == "s":
        scoreBoard()
    else:
        jPod("Invalid Argument")
        pause(3)


while runGame:
    print(set_ans())
    while wrongAns != 2:
        for i in range(0, 1):
            input(guess)
            if guess != answer:
                correctGuess = False
                wrongAns += 1
                if wrongAns == 2:
                    jPod(red("Too many guesses"))
                    clearAll()
                    jPod()
                    break

            else:
                correctGuess = True
                i += 1
                if i == 0:
                    score += 3
                elif i == 1:
                    score += 1

    rungame = False


"""
╭────────────────────────────────────╮
│ ╭────────────────────────────────╮ │
│ │             jPod          ▊▊▊] │ │
│ ├────────────────────────────────┤ │
│ │      ████  ███  █   █ █████    │ │
│ │     █     █   █ ██ ██ █        │ │
│ │     █  ██ █   █ █ █ █ ████     │ │
│ │     █   █ █████ █ █ █ █        │ │
│ │      ████ █   █ █   █ █████    │ │
│ │                                │ │
│ │      ███  █   █ █████ ████     │ │
│ │     █   █ █   █ █     █   █    │ │
│ │     █   █  █ █  ████  ████     │ │
│ │     █   █  █ █  █     █  █     │ │
│ │      ███    █   █████ █   █    │ │
│ ╰────────────────────────────────╯ │
│  jPod                              │
│                                    │
│           _____________            │
│          /\    MENU    /\          │
│         /  \          /  \         │
│        /    \        /    \        │
│       |      \______/      |       │
│       |      /      \      |       │
│       |  ◄◄ |        | ►►  |       │
│       |      \______/      |       │
│       |      /      \      |       │
│        \    /        \    /        │
│         \  /  ► / ||  \  /         │
│          \/____________\/          │
│                                    │
│                                    │
╰────────────────────────────────────╯"""