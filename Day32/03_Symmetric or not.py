# A matrix is symmetric or not

matrix = [[1, 2, 3],
          [2, 4, 5],
          [3, 5, 6]]

is_symmetric = True

print("The current matrix is ")

for i in matrix:
    print(i)


for i in range(len(matrix)):
    for j in range(len(matrix[0])):
        if matrix[i][j] != matrix[j][i]:
            is_symmetric = False
            break

if is_symmetric:
    print("The matrix is symmetric.")
else:
    print("The matrix is not symmetric.")
