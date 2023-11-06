#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if matrix is None:
        return

    for mat in matrix:
        list_len = len(mat)
        for int in mat:
            if (mat.index(int) == list_len - 1):
                print("{:d} ".format(int))
            else:
                print("{:d} ".format(int), end="")
        print()
