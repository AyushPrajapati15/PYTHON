x = float(input("Enter the value of x: "))
n = int(input("Enter the number of terms: "))

sum = 0
sign = 1
term = x

for i in range(n):
    sum += sign * term
    sign *= -1
    term *= x * x
    print(int(term))

print("Sum of the series:", sum)
