from simple_chalk import *

login = True

userName = "theyoungest.camel"
userName.split()
if login == False:
    loginStatus = red("Log In       L")
else:
    loginStatus = userName[0,10] + "  A"
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