# Return statement in python
def fun(a):
    print(a)
    return a*a

print(fun(10))
print()

def fun(a,b):
    print(a,b)
    return a+b

fun(10,33)
print()


def fun(a, b):
    print(a, b)
    return a+b

x = fun(10, 33)
print(x)
print()


# return a list
def fun():
    l = [10, 20, 30]
    return l

print(fun())
print()


def fun():
    l = [10, 20, 30]
    return l

x = fun()
print(x)
for i in x:
    print(i)
print()


def fun():
    t = (10, 20, 30)
    return t

x = fun()
print(x)
for i in x:
    print(i)
print()


def fun():
    print('hello')
    return 10

print(fun())
print()

# return statement should be in function definition
# def fun():
#     print('hello')
#     return 10

# print(fun())
# return 20

def fun():
    print('good morning')
    print('good afternoon')
    print('good eveneing')
    print('good night')
    return 10

fun()
print()


# python function can return multiple value
def fun(a, b, c):
    return a, b, c

print(fun(10, 11, 12))
print()


def fun(a, b, c):
    return a*2, b*3, c*4

t = fun(10, 11, 12)
print(t)
print()


def fun(a, b, c):
    return a*2, b*3, c*4

x,y,z = fun(10, 11, 12)
print(x,y,z)
print()


def fun(a, b, c):
    return a*2, b*3, c*4

x, y, z = fun(10, 11, 12)
print(x, y, z)
print()


# define a function , it will take 6 subjcet mark of a student as an argumet then return totamlmark and avg mark
def cal(p, c, m, b, i, e):
    tm = p+c+m+b+i+e
    print('total mark is ', tm)
    am = tm/6
    return am

print('avg mark is ', cal(67, 56, 90, 87, 76, 91))
print()


def cal(p, c, m, b, i, e):
    tm = p+c+m+b+i+e
    am = tm/6
    return tm, am

print(cal(67, 78, 97, 65, 48, 95))

tm, am = ((cal(67, 78, 97, 65, 48, 95)))
print('totml mark is ', tm)
print('avg ark is ', am)