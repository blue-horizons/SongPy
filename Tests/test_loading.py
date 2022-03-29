from time import sleep
from os import system as cmd
from simple_chalk import * 
loadingIcons = ["|","/","—","\\","|","/","—","\\","|"]

# for x in range(0,1):
#     for i in loadingIcons:
#         cmd("clear")
#         print(i)
#         sleep(0.5)

loadingBar = "["
for i in range(0,30):
    cmd("clear")
    print(loadingBar)
    loadingBar += "█"
    sleep(0.1)
loadingBar += "]"
cmd("clear")
print(loadingBar)

def calcPercent(numberNeeded, count):
    maxLength = 25
    stepNum = count/maxLength
    for i in range(0, 100,stepNum):

