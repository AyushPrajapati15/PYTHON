def fun(a):
    print('inside fun', a)
    print('inside fun ', id(a))
    print()

a = 23
print('outside fun', a)
fun(a)
print('outside fun', a)
print('outside fun ', id(a))
print()

def fun(x):
    print('inside fun', x)
    print('inside fun ', id(x))
    print()


a = 23
print('outside fun', a)
fun(a)
print('outside fun', a)
print('outside fun ', id(a))
print()


# call by value
# pass int (immutable objcet )
def fun(a):
    print('inside fun before modification  : ', a)
    print('inside fun before modification  : ', id(a))
    print()
    a = 1000
    print('inside fun after modification  : ', a)
    print('inside fun after modification  : ', id(a))
    print()


a = 23
print('outside fun before calling  : ', a)
print('outside fun before calling: ', id(a))
print()
fun(a)
print('outside fun after calling: ', a)
print('outside fun after calling: ', id(a))
print()


# call by referance
# pass int (mutable  object )
def fun(l):
    print('inside fun ', l)
    print('inside fun ', id(l))
    print()
    l.append(1000)
    print('inside fun ', l)
    print('inside fun ', id(l))
    print()


l = [23, 33, 43]
print('outside fun ', l)
print('outside fun ', id(l))
print()
fun(l)
print('outside fun ', l)
print('outside fun ', id(l))
print()