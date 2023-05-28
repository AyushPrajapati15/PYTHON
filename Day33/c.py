# Example: Matrix Subtraction

# Matrix A: 3x3
matrix_A = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Matrix B: 3x3
matrix_B = [
    [9, 8, 7],
    [6, 5, 4],
    [3, 2, 1]
]

# Result Matrix: 3x3
result_matrix = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

# Matrix subtraction
for i in range(len(matrix_A)):
    for j in range(len(matrix_A[0])):
        result_matrix[i][j] = matrix_A[i][j] - matrix_B[i][j]

# Displaying the result matrix
print("Result Matrix:")
for row in result_matrix:
    print(row)
