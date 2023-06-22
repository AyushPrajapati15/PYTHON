# define user defined function
# def keyword is ued to defined user defined function

def add(a, b, c):
    '''This function is used to perform addition of three numbers'''
    print(a+b+c)


add(10, 20, 30)
add(11,12,13)


add(10, 20, 30)
add(11, 12, 13)

print(add.__doc__)
print()
print(len.__doc__)
print()
print(input.__doc__)
print()

def add(a, b, c):
    print(a+b+c)


add(10, 20, 30)
add(11,12,13)
print()

def add(a, b, c):
    print(a+b+c)


add(10, 20, 30)
add(11, 12, 13)
print()


def add(a, b, c):
    print('Inside function')
    print(id(a))
    print(id(b))
    print(id(c))
    print(a, b, c)


a, b, c = 10, 20, 30
add(a, b, c)
print()

print('Outside function')
print(id(a))
print(id(b))
print(id(c))
print(a, b, c)
print()


def add(x, y, z):
    print('Inside function')
    print(id(x))
    print(id(y))
    print(id(z))
    print(x, y, z)


a, b, c = 10, 20, 30
add(a, b, c)
print()

print('Outside function')
print(id(a))
print(id(b))
print(id(c))
print(a, b, c)
print()


def add(x, y, z):
    print(id(x))
    x = 1008
    print('Inside function')
    print(id(x))
    print(id(y))
    print(id(z))
    print(x, y, z)



a, b, c = 10, 20, 30
add(a, b, c)
print()

print('Outside function')
print(id(a))
print(id(b))
print(id(c))
print(a, b, c)


