import csv
from getpass import getpass, getuser

supplied_username = input("username > ")

if supplied_username not in open("Login.txt"):
    print("Youre Not in my list")
    # do you want to register?
    # if not check password
    
else:
    Login = True
