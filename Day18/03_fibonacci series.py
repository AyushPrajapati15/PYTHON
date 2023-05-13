# fibonacci series
n=int(input("Enter the number of terms: "))
a=0
b=1
c=a+b
for i in range(n):
    print(a,end=" ")
    a=b
    b=c
    c=a+b
print("")

# factorial of a number
n = int(input("Enter a number: "))
fact = 1

for i in range(1, n + 1):
    fact= fact* i

print("The factorial of", n, "is", fact)
