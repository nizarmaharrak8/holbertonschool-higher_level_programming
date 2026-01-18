#!/usr/bin/python3
def no_c(my_string):
    new_string = ""
    for char1 in my_string:
        if char1 != 'C' and char1 != 'c':
            new_string += char1
    return new_string
