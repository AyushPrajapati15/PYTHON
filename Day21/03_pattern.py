#     1 
#    1 2 1 
#   1 2 3 2 1 
#  1 2 3 4 3 2 1 
# 1 2 3 4 5 4 3 2 1
rows = int(input("Enter the number of rows: "))

for i in range(1, rows + 1): 

    for j in range(1, rows - i + 1):
        print(" ", end="")


    for k in range(1, i + 1):
        print(k, end=" ")


    for l in range(i - 1, 0, -1):
        print(l, end=" ")

    print()
