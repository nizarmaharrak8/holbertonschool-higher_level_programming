#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    x = []
    for y in my_list:
        if y % 2 == 0:
            x.append(True)
        else:
            x.append(False)
    return x
