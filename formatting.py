def colour_red(s):
    new_string = "\033[1;31m" + s + "\033[0;0m"
    return new_string

def colour_yellow(s):
    new_string = "\033[1;33" + s + "\033[0;0m"
    return new_string


def underline(s):
    new_string = "\033[4m" + s + "\033[0m"
    return new_string
