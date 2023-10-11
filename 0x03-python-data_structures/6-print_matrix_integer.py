#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for dom in matrix:
        for mil in dom:
            print("{:d}".format(mil), end=" " if mil != dom[-1] else "")
        print()

