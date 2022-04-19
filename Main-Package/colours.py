
# COLOURS

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

# Background Colours

def bg_black(string):
    return u"\u001b[40m" + string + normalise()

def bg_red(string):
    return u"\u001b[41m" + string + normalise()

def bg_green(string):
    return u"\u001b[42m" + string + normalise()

def bg_yellow(string):
    return u"\u001b[43m" + string + normalise()

def bg_blue(string):
    return u"\u001b[44m" + string + normalise()

def bg_magenta(string):
    return u"\u001b[45m" + string + normalise()

def bg_cyan(string):
    return u"\u001b[46m" + string + normalise()

def bg_white(string):
    return u"\u001b[47m" + string + normalise()

# Light Variant Backgrounds

def bg_bright_black(string):
    return u"\u001b[40;1m" + string + normalise()

def bg_bright_red(string):
    return u"\u001b[41;1m" + string + normalise()

def bg_bright_green(string):
    return u"\u001b[42;1m" + string + normalise()
def bg_bright_yellow(string):
    return u"\u001b[43;1m" + string + normalise()

def bg_bright_blue(string):
    return u"\u001b[44;1m" + string + normalise()

def bg_bright_magenta(string):
    return u"\u001b[45;1m" + string + normalise()

def bg_bright_cyan(string):
    return u"\u001b[46;1m" + string + normalise()

def bg_bright_white(string):
    return u"\u001b[47;1m" + string + normalise()

def bold(string):
    return u"\u001b[1m" + string + normalise()