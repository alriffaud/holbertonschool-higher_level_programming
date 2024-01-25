#!/usr/bin/python3
import dis
from hidden_4 import *
if __name__ == "__main__":
    names = dir(hidden_4)
    # names = [name for name in dir(hidden_4) if not name.startswith("__")]
    # names.sort()

    for name in names:
        print(name)
