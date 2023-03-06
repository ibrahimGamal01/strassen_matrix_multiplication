import random

# Strassen Algorithm works only on square matrices so on input is enough

s = int(input("Enter both square matrices size: "))


def print_matrix(matrix):
    for row in matrix:
        for val in row:
            print(val, end=" ")
        print()


def add_matrices(mat1, mat2):
    result_matrix = [[0 for j in range(len(mat1[0]))]
                     for i in range(len(mat1))]
    for i in range(len(mat1)):
        for j in range(len(mat1[0])):
            result_matrix[i][j] = mat1[i][j] + mat2[i][j]
    return result_matrix


def sub_matrices(matrix1, matrix2):
    result_matrix = [[0 for j in range(len(matrix1[0]))]
                     for i in range(len(matrix1))]
    for i in range(len(matrix1)):
        for j in range(len(matrix1[0])):
            result_matrix[i][j] = matrix1[i][j] - matrix2[i][j]
    return result_matrix


def spilt_matrix(matrix, size):
    a = [[matrix[i][j] for j in range(size)] for i in range(size)]


# mat1 = [[random.randint(1, 20) for j in range(s)] for i in range(s)]
# mat2 = [[random.randint(1, 20) for j in range(s)] for i in range(s)]
