def transpose_matrix(matrix):
    return list(zip(*matrix))


def magic_square(matrix):
    diagonal1 = 0
    diagonal2 = 0
    for i in range(len(matrix)):
        diagonal1 += matrix[i][i]
        rows = 0
        colomns = 0
        for j in range(len(matrix)):
            rows += matrix[i][j]
            colomns += matrix[j][i]
    transpose_matrix(matrix)
    for i in range(len(matrix)):
        diagonal2 += matrix[i][i]
    return diagonal1 == diagonal2 == rows == colomns
