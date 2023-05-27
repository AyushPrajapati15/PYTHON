# Transpose of a matrix

matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]

transpose = [[0, 0, 0],
             [0, 0, 0],
             [0, 0, 0]]

for i in range(len(matrix)):
    for j in range(len(matrix[0])):
        transpose[j][i] = matrix[i][j]

print("The current matrix is ")
for i in matrix:
    print(i)
print()


print("The matrix after transpose is: ")
for i in transpose:
    print(i)
