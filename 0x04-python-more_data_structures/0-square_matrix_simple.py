#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new = matrix.copy()

    for o in range(len(matrix)):
        new[o] = list(map(lambda x: x**2, matrix[i]))

    return (new)

