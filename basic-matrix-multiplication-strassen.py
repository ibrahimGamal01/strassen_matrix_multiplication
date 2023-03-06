import random

# you can read this code as an explaniation for the basic operation of strassen to build it to a recursion

r1 = c1 = r2 = c2 = 2

mat1 = [[random.randint(1, 20) for j in range(c1)] for i in range(r1)]
mat2 = [[random.randint(1, 20) for j in range(c2)] for i in range(r2)]


def print_matrix(matrix):
    for row in matrix:
        for val in row:
            print(val, end=" ")
        print()


def strass(mat1, mat2):
    result_matrix = [[0 for j in range(len(mat2[0]))]
                     for i in range((len(mat1)))]

    a = mat1[0][0]
    b = mat1[0][1]
    c = mat1[1][0]
    d = mat1[1][1]

    e = mat2[0][0]
    f = mat2[0][1]
    g = mat2[1][0]
    h = mat2[1][1]

    p1 = a * (f - h)
    p2 = h * (a + b)
    p3 = e * (c + d)
    p4 = d * (g - e)
    p5 = (a + d) * (e + h)
    # p6 = (b - d) * (f - h)  lab wrong answer
    p6 = (b - d) * (g + h)
    p7 = (a - c) * (e + f)

    result_matrix[0][0] = p6 + p5 + p4 - p2
    result_matrix[0][1] = p1 + p2
    result_matrix[1][0] = p3 + p4
    result_matrix[1][1] = p1 + p5 - p3 - p7

    return result_matrix


print_matrix(mat1)

print("*************************")  # print

print_matrix(mat2)

print("=========================")  # print

ansMat = strass(mat1, mat2)
print_matrix(ansMat)
