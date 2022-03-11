import os
import time
from getpass import getpass, getuser
import json
from simple_chalk import green, red

#print(red(usernames)) # DEBUG

def createUser():
    global accounts
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


