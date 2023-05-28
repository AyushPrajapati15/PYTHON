# Example: Matrix Rotation

matrix_A = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

n = len(matrix_A)

rotated_matrix = [[0 for _ in range(n)] for _ in range(n)]

for i in range(n):
    for j in range(n):
        rotated_matrix[j][n - i - 1] = matrix_A[i][j]

print("Rotated Matrix:")
for row in rotated_matrix:
    print(row)



# Example: Matrix Diagonal Sum

matrix_A = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

n = len(matrix_A)

diagonal_sum = 0
for i in range(n):
    diagonal_sum += matrix_A[i][i]

print("Sum of the main diagonal:", diagonal_sum)