# from simple_chalk import *

# # Prepare Game Over Screen Colours
# gameOverOut = ""
# outlineElems = ["╗","╚","═","║","╝","╔"]
# gameOver = [
# "                                                                          ",
# "   ██████╗  █████╗ ███╗   ███╗███████╗    █████╗ ██╗   ██╗███████╗██████╗  ",
# "  ██╔════╝ ██╔══██╗████╗ ████║██╔════╝   ██╔══██╗██║   ██║██╔════╝██╔══██╗ ",
# "  ██║  ██╗ ███████║██╔████╔██║█████╗     ██║  ██║╚██╗ ██╔╝█████╗  ██████╔╝ ",
# "  ██║  ╚██╗██╔══██║██║╚██╔╝██║██╔══╝     ██║  ██║ ╚████╔╝ ██╔══╝  ██╔══██╗ ",
# "  ╚██████╔╝██║  ██║██║ ╚═╝ ██║███████╗   ╚█████╔╝  ╚██╔╝  ███████╗██║  ██║ ",
# "   ╚═════╝ ╚═╝  ╚═╝╚═╝     ╚═╝╚══════╝    ╚════╝    ╚═╝   ╚══════╝╚═╝  ╚═╝ ",
# "                                                                          "]

# for x in gameOver:
#     for i in gameOver[x]:
#         if i == "█":
#             gameOverOut +=yellow(i)
#         elif i in outlineElems:
#             gameOverOut += red(i)
#         else:
#             gameOverOut += i
# shwfeig


# for i in len(gameOver[0]):
#     jpod = f"""
# ╭────────────────────────────────────╮
# │ ╭────────────────────────────────╮ │
# │ │             jPod          ▊▊▊] │ │
# │ │ {outLines[0]} │ │
# │ │ {outLines[1]} │ │
# │ │ {outLines[2]} │ │
# │ │ {outLines[3]} │ │
# │ │ {outLines[4]} │ │
# │ │ {outLines[5]} │ │
# │ │ {outLines[6]} │ │
# │ │ {outLines[7]} │ │
# │ │ {outLines[8]} │ │
# │ │ {outLines[9]} │ │
# │ ╰────────────────────────────────╯ │
# │  jPod                              │
# │                                    │
# │           _____________            │
# │          /\    MENU    /\          │
# │         /  \          /  \         │
# │        /    \        /    \        │
# │       |      \______/      |       │
# │       |      /      \      |       │
# │       |  ◄◄ |        | ►►  |       │
# │       |      \______/      |       │
# │       |      /      \      |       │
# │        \    /        \    /        │
# │         \  /  ► / ||  \  /         │
# │          \/____________\/          │
# │                                    │
# │                                    │
# ╰────────────────────────────────────╯
# """




# for i in gameOverOut:
#     print(i)









def pad(string,maxLength,padChar=" ",alignment="l"):
    stringLength = len(string)
    padding = ""

    if stringLength < maxLength:
        difference = maxLength - stringLength
        
        for i in range(0,difference):
            padding += padChar

        if alignment.lower() == "l":
            outputString = string + padding
        elif alignment.lower() == "r":
            outputString = padding + string
        elif alignment.lower() == "c":
            if difference % 2 == 1:
                padL = difference/2 + 0.5
                padR = difference/2 - 0.5
            else:
                padL = difference/2 
                padR = difference/2
            outputString = padL + string + padR

    elif stringLength > maxLength:
        outputString = string[0,maxLength]
    
    return outputString


# Align Left
"""                        |
text is here               
               text is here
       text is here        
"""