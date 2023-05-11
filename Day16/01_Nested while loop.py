# Nested while loop
i = 1
while (i <= 3):
    print("Hello!")
    j = 1
    while (j <= 3):
        print("Alice")
        j = j+1
    i = i+1

i = 1
while (i <= 5):
    print("i=   ", i)
    j = 1
    while (j <= 3):
        print("j= ", j)
        j = j+1
    i = i+1


rows = int(input("Enter the number of rows: "))
cols = int(input("Enter the number of columns: "))

row_index = 1
col_index = 1

while row_index <= rows:
    col_index = 1
    while col_index <= cols:
        product = row_index * col_index
        print(product, end="\t")
        col_index += 1
    print()
    row_index += 1

