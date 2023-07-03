# Global keyword and global functions()
# global keyword

def fun():
    global a
    a = 23
    print(a)



def fun2():
    print(a)

fun()
fun2()


def fun():
    global a  # global variable
    b = 123  # local variable
    a = 23
    print(a)
    print(b)


def fun2():
    print(a)
    # print(b)

fun()
fun2()


# By using global keyword we can perform modification on global variable inside function
a = 23 # ----> Global variable


def fun():
    global a
    a = 999
    print(a)

fun()
print(a)


a = 23 # ----> Global variable

def fun():
    # print(a)    ---> Global will declare first, we can use any other variable but to change 'a' which is global variable first we have to write global 
    global a
    a = 999
    print(a)

fun()
print(a)


a = 23 # ----> Global variable

def fun():
    b = 789
    print(b)
    global a
    a = 999
    print(a)

fun()
print(a)


# globals()

a = 23


def fun():
    a = 999
    print(a)
    print(globals()['a'])


fun()


globals()

a = 23


def fun():
    a = 999
    print(a)
    data = globals()['a']
    print(data)


fun()
print(a)
# print(data)