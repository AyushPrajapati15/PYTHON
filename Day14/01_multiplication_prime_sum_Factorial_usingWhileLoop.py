# Multiplication table
n=int(input("Enter the number whose table is to be printed: "))
i=1
while i<=10:

    # print(n,'x',i,'=',n*i)
    print(f'{n} * {i} = {n*i}')
    i=i+1


# Factorial of a number
n=int(input("Enter a number: "))
fact=1
while n>0:
    fact=fact*n
    n=n-1
print(fact)

# prime or not using while loop

n = int(input("Enter a number"))
i=1
count=0
while i<=n:
    if n%i==0:
        count=count+1
    i=i+1
if count==2:
    print(n," is a prime number")
else:
    print(n," is not a prime number")

# sum of its digits using a while loop.
n = int(input("Enter a number: "))
sum=0
while n>0:
    r=int(n%10)
    sum=sum+r
    n=n/10
print(sum)
