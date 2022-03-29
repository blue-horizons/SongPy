from simple_chalk import *
import os
import time

global screenWidth, battery
screenWidth = 38
battery = green("▊▊▊")



string = ""
temp = []
for i in string:
    if i == "\u000a":
        count += 1

    rowx.append(string[i])






rowx = [p0,p1,p2,p3,p4,p5,p6,p7,p8,p9,pa,pb,pc,pd,pe,pf,pg,ph,pi,pj,pk,pl,pm,pn,po,pp,pq,pr,ps,pt,pu,pv]

row0 = ["","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","",""]
row1 = ["","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","",""]
row2 = ["","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","",""]
row3 = ["","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","",""]
row4 = ["","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","",""]
row5 = ["","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","",""]
row6 = ["","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","",""]
row7 = ["","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","",""]
row8 = ["","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","",""]
row9 = ["","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","",""]

screen = [row0,row1,row2,row3,row4,row5,row6,row7,row8,row9]

def pad(string, max_=screenWidth, paddingChar=" ",align="l"):
    padding_string = ""
    padding = 0
    # Pads a string with a certain amount of
    # characters, or truncuates the string to
    # a certain length.

    max_ = int(max_)


    if len(string) > max_:
        string = string[0:max_]

    elif len(string) < max_:
        padding = max_ - len(string)
    
    if align.lower() == "l":              # ALIGN LEFT (STANDARD)
        for i in range(0, padding):
            padding_string += paddingChar
        string += padding_string
    
    if align.lower() == "c":              # ALIGN CENTRE
        if padding % 2 == 1:
            leftPaddingLen = padding/2 + 0.5
            rightPaddingLen = padding/2 - 0.5

        for i in range(0,leftPaddingLen):
            leftPadding += paddingChar
        for i in range(0, rightPaddingLen):
            rightPadding += paddingChar
        
        string = leftPadding + string + rightPadding

    if align.lower() == "r":              # ALIGN RIGHT
        for i in range(0, padding):
            padding_string += paddingChar
        string = padding_string + string

    return string

def jPod(line1,line2=" ",line3=" ",line4=" ",line5=" ",line6=" ",line7=" ",line8=" ",line9=" ",line10=" ",genAlign="left",print_=False):
    
    
    normal = bgBlack.white
    lines = ["","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","",""]
    outLines = ["","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","",""]

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
    jpod = f"""╭────────────────────────────────────╮
│ ╭────────────────────────────────╮ │
│ │              jPod        │{battery}] │ │
│ ├────────────────────────────────┤ │
{normal("│ │ ")}{outLines[0]}{normal(" │ │")}
{normal("│ │ ")}{outLines[1]}{normal(" │ │")}
{normal("│ │ ")}{outLines[2]}{normal(" │ │")}
{normal("│ │ ")}{outLines[3]}{normal(" │ │")}
{normal("│ │ ")}{outLines[4]}{normal(" │ │")}
{normal("│ │ ")}{outLines[5]}{normal(" │ │")}
{normal("│ │ ")}{outLines[6]}{normal(" │ │")}
{normal("│ │ ")}{outLines[7]}{normal(" │ │")}
{normal("│ │ ")}{outLines[8]}{normal(" │ │")}
{normal("│ │ ")}{outLines[9]}{normal(" │ │")}
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
    if print_ == False:
        return jpod
    else: 
        print(jpod)


# jPod(red.bgYellow(
# "     ████  ███  █   █ █████   "),red.bgYellow(
# "    █     █   █ ██ ██ █       "),red.bgYellow(
# "    █  ██ █   █ █ █ █ ████    "),red.bgYellow(
# "    █   █ █████ █ █ █ █       "),red.bgYellow(
# "     ████ █   █ █   █ █████   "),yellow.bgRed(
# "     ███  █   █ █████ ████    "),yellow.bgRed(
# "    █   █ █   █ █     █   █   "),yellow.bgRed(
# "    █   █  █ █  ████  ████    "),yellow.bgRed(
# "    █   █  █ █  █     █  █    "),yellow.bgRed(
# "     ███    █   █████ █   █   "),
# print_ = True)
style1 = red.bgGreen
style2 = green.bgRed

for i in range(0,100):
    os.system("clear")
    jPod(style1(
"     ████  ███  █   █ █████   "),style1(
"    █     █   █ ██ ██ █       "),style1(
"    █  ██ █   █ █ █ █ ████    "),style1(
"    █   █ █████ █ █ █ █       "),style1(
"     ████ █   █ █   █ █████   "),style1(
"     ███  █   █ █████ ████    "),style2(
"    █   █ █   █ █     █   █   "),style2(
"    █   █  █ █  ████  ████    "),style2(
"    █   █  █ █  █     █  █    "),style2(
"     ███    █   █████ █   █   "),
print_ = True)
    time.sleep(0.1)
    os.system("clear")
    jPod(style2(
"     ████  ███  █   █ █████   "),style2(
"    █     █   █ ██ ██ █       "),style2(
"    █  ██ █   █ █ █ █ ████    "),style2(
"    █   █ █████ █ █ █ █       "),style2(
"     ████ █   █ █   █ █████   "),style2(
"     ███  █   █ █████ ████    "),style1(
"    █   █ █   █ █     █   █   "),style1(
"    █   █  █ █  ████  ████    "),style1(
"    █   █  █ █  █     █  █    "),style1(
"     ███    █   █████ █   █   "),
print_ = True)
    time.sleep(0.1)