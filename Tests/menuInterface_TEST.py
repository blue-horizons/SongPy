from simple_chalk import *

loginStatus = red("Log In       L")
loginStatus = input(green("Username > "))

def menu():
    login = bool(input(red("Login > ")))

    userName = input(green("Username > "))

    if login == False:
        loginStatus = red("Log In       L")
    else:
        loginStatus = pad(userName, 11) + "  A"
        loginStatus = yellow(loginStatus)


    print(""" __________________
| ________________ |""")
    print("|| " + green("New Game     N ") + "||")
    print("||                ||")
    print("|| " + blue("Difficulty   D") + " ||")
    print("||                ||")
    print(f"|| {loginStatus} ||")
    print("""||________________||
| jpod             |
|       ______     |
|      /\    /\    |
|     /  \__/  \   |
|    |   /  \   |  |
|    |   \__/   |  |
|     \  /  \  /   |
|      \/____\/    |
|                  |
|__________________|
""")

userScreen = f"""
 __________________
| ________________ |
|| {green("New Game     N ")}||
||                ||
|| {blue("Difficulty   D")} ||
||                ||
|| {yellow(loginStatus)} ||
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
|__________________|
"""
print(userScreen)