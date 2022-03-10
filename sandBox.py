from simple_chalk import *

login = bool(input(red("Login > ")))

userName = input(green("Username > "))

def pad(string, max_, paddingChar=" "):
    max_=int(max_)
    if len(string) > max_:
        string = string[0:max_]
    elif len(string) < max_:
        padding = max_ - len(string)
        for i in range(0,padding):
            string += " "
    return string

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
print("""||________________||)
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