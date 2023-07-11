# Addition of two number without using lambda
def add(a,b):
    return a+b
print(add(10,20))
print()


# Addition of two number with using lambda
f= lambda a,b:a+b
print(f(10,20))
print(type(f))
print()


# square of a number without using lambda
def sq(n):
    return n*n
print(sq(10))
print()


# square of a number with using lambda
x=lambda n:n*n
print(x(10))
print()


# Fid out the greatest among two number without using lambda
def fun(a,b):
    if a>b:
        return a
    else:
        return b
print(fun(10,2))
print()


# Fid out the greatest among two number without using lambda
a=lambda a,b: a if a>b else b
print(a(11,22))
print()

a=lambda a,b: a+a if a>b else b+b
print(a(10,20))
print()


# normal function can return multiple value
def fun(a,b):
    return a,b
print(fun(10,20))
print()


# Lambda will return only one value(Only one expression it will return )

# z=lambda a,b:a,b   # Error-name b is not defined
# print(z(1,2))

z=lambda a,b:a
print(z(1,2))
print()


# lambda can return collection
l=lambda a,b:(a,b)
print(l(10,20))
print()


l=lambda a,b:[10,20,30,40,50]
print(l(10,20))
print()


y=lambda :"India"
print(y())
print()

y=lambda :"I love "+"India"
print(y())
print()


#  find out the greatest among two number in one line


print((lambda a,b: a if a>b else b )(10,20))