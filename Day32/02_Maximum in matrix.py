# Maximum element in a matrix
matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]

max_element = matrix[0][0]

print("The current matrix is ")

for i in matrix:
    print(i)

print()

for i in matrix:
    for j in i:
        if j > max_element:
            max_element = j

print("The maximum element of the matrix is: ")

print(max_element)
