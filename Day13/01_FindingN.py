# Find the value of n
import math
x=int(input("Enter the value of x: "))
n=int(input("Enter the value of n: "))

if n==1:
    print(1+x)
elif n==2:
    print(1+x/n)
elif n==3:
    print(1+x**n)
# elif n==3:
#     print(1+math.pow(x,n)) 
else:
    print(1+n*x)
