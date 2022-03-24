from os import system as cmd
import platform 



# Sets clear command

global clear

if platform == "linux" or platform == "linux2" or platform == "darwin":
    clear = "clear"
else:
    clear = "cls"



# Clears Shell

def clear_shell():
    cmd(clear)



# Normalise

def normalise():
    return u"\u001b[0m"



# Standard Colours

def black(string):
    return u"\u001b[30m" + string + normalise()

def red(string):
    return u"\u001b[31m" + string + normalise()

def green(string):
    return u"\u001b[32m" + string + normalise()

def yellow(string):
    return u"\u001b[33m" + string + normalise()

def blue(string):
    return u"\u001b[34m" + string + normalise()

def magenta(string):
    return u"\u001b[35m" + string + normalise()

def cyan(string):
    return u"\u001b[36m" + string + normalise()

def white(string):
    return u"\u001b[37m" + string + normalise()



# Bright Colour Variants

def bright_black(string):
    return u"\u001b[30m;1m" + string + normalise()

def bright_red(string):
    return u"\u001b[31m;1m" + string + normalise()

def bright_green(string):
    return u"\u001b[32m;1m" + string + normalise()

def bright_yellow(string):
    return u"\u001b[33m;1m" + string + normalise()

def bright_blue(string):
    return u"\u001b[34m;1m" + string + normalise()

def bright_magenta(string):
    return u"\u001b[35m;1m" + string + normalise()

def bright_cyan(string):
    return u"\u001b[36m;1m" + string + normalise()

def white(string):
    return u"\u001b[37m;1m" + string + normalise()



# Custom 256 colour support

def colour_256(string, num): # `num` must be 0 >= 255
    num = str(num)
    return u"\u001b[38;5;" + num + "m " + string + normalise()
    