n = int(input("Enter the number of rows (odd number): "))


for i in range(1, n//2 + 1):
    spaces = " " * (n//2 - i + 1)
    stars = "*" * (2*i - 1)
    print(spaces + stars)


print("*" * n)


for i in range(n//2, 0, -1):
    spaces = " " * (n//2 - i + 1)
    stars = "*" * (2*i - 1)
    print(spaces + stars)
