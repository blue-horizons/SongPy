
# Globals

global json_file
global accounts
global usernames
global songList
global clear
global passwords

from imports import *

# Open `accounts.csv`

        

# Starting Variables
valid_user = False
valid_pwd = False
usernames = []
accounts = []
passwords = []


with open("Main-Package/accounts.csv", "r") as f:
    reader = csv.reader(f)
    var = list(reader)
    for i in range(1,len(var)):
        usernames.append(var[i][0])
        passwords.append(var[i][1])

###############################################################

# Functions

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
    print(f"""
 __________________
| ________________ |
||                ||
|| {blue("New Username")}   ||
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
|| {blue("New Password")}   ||
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
|| {blue("Confirm")}        ||
|| {blue("Password")}       ||
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
            clearAll()
            print(f"""
 __________________
| ________________ |
||                ||
|| {red("Passwords dont")} ||
|| {red("match.")}         ||
|| {red("Try Again")}      ||
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
            accounts[new_username] = confirm_pwds
            password_valid = True
            with open("accounts.csv","a") as f:
                f.write(f"{new_username},{new_password}")

def login():
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
                password = input("> ")
                if password != passes[users.index(username)]:
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

# def login(): 
#     valid_user = False
#     valid_pwd = False
#     while not valid_user:
#         print(f"""
#  __________________
# | ________________ |
# || {bold("LOG IN:")}        ||
# || UserName:      ||
# || ██████████████ ||
# || Pwd:           ||
# || ██████████████ ||
# ||________________||
# | jpod             |
# |       ______     |
# |      /\    /\    |
# |     /  \__/  \   |
# |    |   /  \   |  |
# |    |   \__/   |  |
# |     \  /  \  /   |
# |      \/____\/    |
# |                  |
# |__________________|""")
#         username = input("U > ")
#         if username not in usernames:
#             clearAll()
#             print(f"""
#  __________________
# | ________________ |
# || {red("Your account")}   ||
# || {red("doesn't exist.")} ||
# || Create a new   ||
# || one?           ||
# ||            {yellow("y/N")} ||
# ||________________||
# | jpod             |
# |       ______     |
# |      /\    /\    |
# |     /  \__/  \   |
# |    |   /  \   |  |
# |    |   \__/   |  |
# |     \  /  \  /   |
# |      \/____\/    |
# |                  |
# |__________________|""")
#             newUser = input("> ")
#             if newUser.lower() == "y":
#                 clearAll()
#                 createUser()
#             else:
#                 clearAll()
#                 break
#         else:
#             valid_user = True

#     while not valid_pwd:
#         clearAll()
#         print(f"""
#  __________________
# | ________________ |
# || {bold("LOG IN:")}        ||
# || UserName:      ||
# || {green(pad(username,14,paddingChar="█"))} ||
# || Pwd:           ||
# || ██████████████ ||
# ||________________||
# | jpod             |
# |       ______     |
# |      /\    /\    |
# |     /  \__/  \   |
# |    |   /  \   |  |
# |    |   \__/   |  |
# |     \  /  \  /   |
# |      \/____\/    |
# |                  |
# |__________________|""")
#         # print("Username")
#         # print("> " + green(username))
#         # print("P > ")
#         password = input("P > ")
#         if  password != accounts.get(username):
#             print(f"""
#  __________________
# | ________________ |
# ||                ||
# || {red("Incorrect")}      ||
# || {red("Password.")}      ||
# || {red("Try Again.")}     ||
# ||                ||
# ||________________||
# | jpod             |
# |       ______     |
# |      /\    /\    |
# |     /  \__/  \   |
# |    |   /  \   |  |
# |    |   \__/   |  |
# |     \  /  \  /   |
# |      \/____\/    |
# |                  |
# |__________________|""")
#             time.sleep(1)
#             clearAll()
#         else:
#             valid_pwd = True
#             clearAll()
#             print(f"""
#  __________________
# | ________________ |
# ||                ||
# || {green("Correct")}      ||
# || {green("Password.")}      ||
# ||                ||
# ||   {brightGreen("LOGGED  IN")}   ||
# ||________________||
# | jpod             |
# |       ______     |
# |      /\    /\    |
# |     /  \__/  \   |
# |    |   /  \   |  |
# |    |   \__/   |  |
# |     \  /  \  /   |
# |      \/____\/    |
# |                  |
# |__________________|""")

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
    

