# Single(*) and double star(*) function call

def fun(a, x, y, z):
    print(a)
    print(x)
    print(y)
    print(z)

fun(10, 20, 30, 40)
print()


def fun(a, x, y, z):
    print(a)
    print(x)
    print(y)
    print(z)

l = [10, 20, 30, 40]
fun(*l)
print()


def fun(a, x, y, z):
    print(a)
    print(x)
    print(y)
    print(z)

l = [10, 20, 30]
# fun(*l)
fun(55,*l)
print()


def fun(a, x, y, z):
    print(a)
    print(x)
    print(y)
    print(z)

l = [10, 20, 30]
fun(*l, 777)
print()


def fun(a, x, y, z):
    print(a)
    print(x)
    print(y)
    print(z)

l = [10, 20, 30]
fun(777, *l)
print()


def fun(a, x, y, z):
    print(a)
    print(x)
    print(y)
    print(z)

l = [10, 20]
# fun(777, *l)
fun(777, *l,55)
print()


def fun(a, x, y, z):
    print(a)
    print(x)
    print(y)
    print(z)

l = [10, 20]
fun(777, 888, *l)
print()


def fun(a, x, y, z):
    print(a)
    print(x)
    print(y)
    print(z)

l = [10, 20, 30]
# fun(777, 888, *l)
fun(12,*l)
print()


def fun(a, x, y, z):
    print(a)
    print(x)
    print(y)
    print(z)

t = (10, 20, 30, 40)
fun(*t)
print()


def fun(a, x, y, z):
    print(a)
    print(x)
    print(y)
    print(z)

s = {10, 20, 30, 40}
fun(*s)
print()


# ** in function call
def fun(a, **s):
    print(a)
    print(s)

fun(10, i=100)
print()


def fun(a, **s):
    print(a)
    print(s)

d = {'i': 100, 'j': 200, 'k': 300}
fun(10, **d)
print()


def fun(a, **s):
    print(a)
    print(s)

d = {'i': 100, 'j': 200, 'k': 300}
fun(10, i=100,j=200,k=300)