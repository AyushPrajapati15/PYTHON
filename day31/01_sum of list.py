# sum of rows and columns of a list
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

rows = len(matrix)
columns = len(matrix[0]) if rows > 0 else 0

row_sums = [0] * rows
column_sums = [0] * columns

for i in range(rows):
    for j in range(columns):
        row_sums[i] += matrix[i][j]
        column_sums[j] += matrix[i][j]

print("Row sums:")
for i in range(rows):
    print(f"Row {i+1}: {row_sums[i]}")

print("Column sums:")
for j in range(columns):
    print(f"Column {j+1}: {column_sums[j]}")

