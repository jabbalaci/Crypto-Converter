import sys


def get_platform():
    text = sys.platform
    if text.startswith("linux"):
        return "linux"
    if text.startswith("win"):
        return "windows"
    # else
    # raise RuntimeError("unknown platform")
    return "else"


