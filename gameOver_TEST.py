from simple_chalk import yellow,green,blue,bgMagenta,red
gameOverOut = ""
# Prepare Game Over Screen Colours
outlineElems = ["╗","╚","═","║","╝","╔"]
gameOver = ("""
                                                                         
  ██████╗  █████╗ ███╗   ███╗███████╗   █████╗ ██╗   ██╗███████╗██████╗  
 ██╔════╝ ██╔══██╗████╗ ████║██╔════╝  ██╔══██╗██║   ██║██╔════╝██╔══██╗ 
 ██║  ██╗ ███████║██╔████╔██║█████╗    ██║  ██║╚██╗ ██╔╝█████╗  ██████╔╝ 
 ██║  ╚██╗██╔══██║██║╚██╔╝██║██╔══╝    ██║  ██║ ╚████╔╝ ██╔══╝  ██╔══██╗ 
 ╚██████╔╝██║  ██║██║ ╚═╝ ██║███████╗  ╚█████╔╝  ╚██╔╝  ███████╗██║  ██║ 
  ╚═════╝ ╚═╝  ╚═╝╚═╝     ╚═╝╚══════╝   ╚════╝    ╚═╝   ╚══════╝╚═╝  ╚═╝ 
                                                                         
""")
for i in gameOver:
    if i == "░":
        gameOverOut += (" ")
    elif i == "█":
        gameOverOut +=yellow(i)
    elif i in outlineElems:
        gameOverOut += red(i)
    else:
        gameOverOut += i

print(gameOverOut)
