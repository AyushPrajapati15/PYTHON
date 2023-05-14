# Prime number within a range

n = int(input("Enter a number "))
for i in range(2, n, 1):
    for j in range(2, i, 1):
        if (i % j) == 0:
            break
    else:
        print(i)
