#         1 
#       2 3 4 
#     5 6 7 8 9 
#   10 11 12 13 14 15 
# 16 17 18 19 20 21 22 23

rows = int(input("Enter the number of rows: "))

num = 1
for i in range(1, rows + 1):
    for j in range(1, rows - i + 1):
        print(" ", end=" ")

    for k in range(1, i + 1):
        print(num, end=" ")
        num += 1

    for l in range(i - 1, 0, -1):
        print(num, end=" ")
        num += 1

    print()
