#!/usr/bin/python3
from sys import argv

if __name__ == "__main__":
    leng = len(argv) - 1
    if leng > 1:
        print("{} arguments:".format(leng))
    elif leng == 0:
        print("{} arguments.".format(leng))
    elif leng == 1:
        print("1 argument:")

    for i in range(1, leng + 1):
        print("{}: {}".format(i, argv[i]))
