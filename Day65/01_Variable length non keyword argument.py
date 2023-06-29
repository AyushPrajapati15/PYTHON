# variable length argumnet (non-keyword)
# issues

def fun(a, b, c, d, e):
    print(a, b, c, d, e)

fun(10, 20, 30, 40, 50)
print()

# solution
def fun(*a):
    # print(type(a))
    print(a)

fun(10, 20)
fun(10, 20, 30)
fun(10, 20, 77, 89, 67)
fun(10)
fun()
print()

def fun(*args):
    print(args)

fun(10, 20, 33, 56)
print()

def fun(*args):
    print(args)

fun(10, 20, 33, 56, [88, 89, 78],
    (10, 20, 33, 41, 23, 11, 67), True, False, 10+20j)
print()


# variable length keyword argument + positional argumnet
def fun(x, *a):
    print('x is :', x)
    print('a is :', a)

fun(10, 20, 30, 40)
print()


def fun(*a, x):
    print('x is :', x)
    print('a is :', a)

# fun(10, 20, 30, 40)
fun(10, 20, 30, 40,x=55)
print()


# missing 1 required keyword-only argument: 'x'
def fun(*a, x):
    print('x is :', x)
    print('a is :', a)

fun(10, 20, 30, x=40)
print()


def fun(*a, x):
    print('x is :', x)
    print('a is :', a)

# fun(x=40,10, 20, 30)
fun(10,20,30,4,50,x=55)
print()


def fun(x, *a):
    print('x is :', x)
    print('a is :', a)

# fun(10, 20, 30, x=40)
fun(10, 20, 30)
print()


def fun(*a, x):
    print('x is :', x)
    print('a is :', a)

fun(10, 20, 30, x=40)
print()


def fun(*a, x):
    print('x is :', x)
    print('a is :', a)

fun(10,20,x=40)
print()


# deafult argument + variable length argumnet
def fun(*a,x=10):
    print('a is ',a)
    print('x is ',x)

fun(99)
print()


def fun(*a, x=10):
    print('a is ', a)
    print('x is ', x)

fun(99, 123, 44, 12, 78, 900, x=789)
print()


def fun(x=10, *a):
    print('a is ', a)
    print('x is ', x)

# fun(99, 123, 44, 12, 78, 900, x=789)
fun(99, 123, 44, 12, 78, 900)
print()


def fun(x=10, *a):
    print('a is ', a)
    print('x is ', x)

fun(99, 123, 44, 12, 78, 900)
print()


def fun(x=10, *a):
    print('a is ', a)
    print('x is ', x)

fun(99, 123, 44, 12, 78, 900)
print()


# keyword argument + positional argumnet + varible length argumnet
def fun(a, b, *n, x=10):
    print(a)
    print(b)
    print(n)
    print(x)

fun(10, 20)
print()


def fun(a, b, *n, x=10):
    print(a)
    print(b)
    print(n)
    print(x)

fun(10, 20, 30, 40, 50, x=999)
print()


def fun(a, b, x=10, *n):
    print(a)
    print(b)
    print(n)
    print(x)

# fun(10, 20, 30, 40, 50, x=999)
fun(10, 20, 30, 40, 50)
print()


def fun(a, b, x=10, *n):
    print(a)
    print(b)
    print(n)
    print(x)

fun(10, 20, 30, 40, 50)
print()


def fun(a, b, x=10, *n):
    print(a)
    print(b)
    print(n)
    print(x)

# fun(10, 20, x=30, 40, 50)
fun(10,20,30,40,50,60)

