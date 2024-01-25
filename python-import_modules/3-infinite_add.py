#!/usr/bin/python3
import sys

if __name__ == "__main__":
    argc = len(sys.argv) - 1  # subtract 1 to exclude the script name itself

    if argc == 0:
        print("0")
    else:
        sum = 0
        for i in range(1, argc + 1):
            sum += int(sys.argv[i])
        print(sum)
