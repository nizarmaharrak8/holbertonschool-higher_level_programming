#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    for row in matrix:
        for x in range(len(row)):
            if x != len(row) - 1:
                print("{:d}".format(row[x]), end=" ")
            else:
                print("{:d}".format(row[x]), end="")
    print()



matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

new_matrix = square_matrix_simple(matrix)
print(new_matrix)
print(matrix)