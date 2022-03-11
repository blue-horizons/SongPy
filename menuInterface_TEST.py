from simple_chalk import *



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