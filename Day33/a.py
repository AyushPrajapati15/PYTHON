matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]

rotated_matrix = list(zip(*matrix[::-1]))

for row in rotated_matrix:
    print(row)




# Matrix A: 2x3
matrix_A = [
    [1, 2, 3],
    [4, 5, 6]
]

# Matrix B: 3x2
matrix_B = [
    [7, 8],
    [9, 10],
    [11, 12]
]

result_matrix = [[0, 0], [0, 0]]

for i in range(len(matrix_A)):
    for j in range(len(matrix_B[0])):
        for k in range(len(matrix_B)):
            result_matrix[i][j] += matrix_A[i][k] * matrix_B[k][j]


print("Result Matrix:")
for row in result_matrix:
    print(row)



# Example: Matrix Determinant

matrix_A = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

determinant = (
    matrix_A[0][0] * (matrix_A[1][1] * matrix_A[2][2] - matrix_A[2][1] * matrix_A[1][2]) -
    matrix_A[0][1] * (matrix_A[1][0] * matrix_A[2][2] - matrix_A[2][0] * matrix_A[1][2]) +
    matrix_A[0][2] * (matrix_A[1][0] * matrix_A[2][1] - matrix_A[2][0] * matrix_A[1][1])
)

print("Determinant:", determinant)

