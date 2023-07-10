# print number from 1 to 5 using recursion

def fun(num):
    if num == 6:
        return
    else:
        print(num)
        fun(num+1)


fun(1)
print()


# print number from 1 to 5 using recursion in reverse order
def fun(num):
    if num == 5:
        return
    else:
        fun(num+1)
        print(num)


fun(1)
print()


# *
# **
# ***
# ****
# *****

def star(num):
    print('*'*num)
    if num == 5:
        return
    star(num+1)


star(1)
print()

# Alternate way
# *****
# ****
# ***
# **
# *
def starrev(num):
    if num==6:
        return
    else:
        starrev(num+1)
        print('*'*num)

starrev(1)
print()

# *****
# ****
# ***
# **
# *

def star(num):
    print('*'*num)
    if num == 1:
        return
    star(num-1)


star(5)

print()


# find out sum of n natural number

def sumofallno(n):
    if n == 1:
        return n
    return n+sumofallno(n-1)


print(sumofallno(5))
print()


# factorial of a number using recursion

def fact(num):
    if num == 1:
        return 1
    return num*fact(num-1)


print(fact(4))
print()


# Fibonacci Series using Recursion(0,1,1,2,3,5,8,13................)
def fib(num):
    if num <= 1:
        return num
    else:
        return fib(num-1)+fib(num-2)


print(fib(6))