from imports import *



def jpod(line1message,line2message="",line3message="",line4message="",line5message=""): # Set colours to variables first 
    
    checkedNum = 0
    
    # Adds all messages to list
    messages = []
    messages.append(line1message)
    if line2message != "":
        messages.append(line2message)
    if line3message != "":
        messages.append(line3message)
    if line4message != "":
        messages.append(line4message)
    if line5message != "":
        messages.append(line5message)
    outMessages = []
    while checkedNum != 2:
        for i in messages:
            if len(i) > 14:
                string = string[0:14]
                outMessages.append[i]
                outMessages.append[string[15:len(string)]]

            elif len(i) < 14:
                string = ""
                padding = 14 - len(string)
                for i in range(0,padding):
                    string += " "
                outMessages.append[string]
        checkedNum += 1
        

    jpod = f"""
 __________________
| ________________ |
|| {outMessages[0]} ||
|| {line2message} ||
|| {line3message} ||
|| {line4message} ||
|| {line5message}{scrollNeeded}||
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
|__________________|"""
    return jpod

print(jpod(input("1 > "),input("2 > ")))