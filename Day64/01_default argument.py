def fun(name):
    print(f'hi {name} good morning')

fun('Alice')
print()


def fun(name):
    print(f'hi {name} good morning')
print()

# fun()


# default argumnet
def fun(name='Jack'):
    print(f'hi {name} good morning')

fun()
print()


def fun(name='Jack'):
    print(f'hi {name} good morning')

fun('Alice')
print()



# postional and default argument
def msg(a, b='hello'):
    print(f'hi {a}  {b}')

msg('Bob', 'mary')
msg('Alice')
print()


def msg(a='Alice', b='How are you'):
    print(f'hi {a}  {b}')

msg('bob', 'alice')
msg('jerry')
print()


def msg(a='Alice', b='How are you'):
    print(f'hi {a}  {b}')

msg('Bob', 'alice')
msg(a='bob', b='jack')
print()
# def student(name,id,email='no',mark):
#     print('name is  ',name)
#     print('id  is ',id)
#     print('email  is ', email)
#     print('mark  is ', mark)

# student('Alice',123,25)


def student(name, id, mark, email='no'):
    print('name is  ', name)
    print('id  is ', id)
    print('email  is ', email)
    print('mark  is ', mark)

student('Alice', 123, 25)
print()


def student(name, id, mark, email='no'):
    print('name is  ', name)
    print('id  is ', id)
    print('email  is ', email)
    print('mark  is ', mark)

student('Alice', 123, 25, 'Alice@gmail.com')
print()


def student(name, id, mark, email='no', addr='no'):
    print('name is  ', name)
    print('id  is ', id)
    print('email  is ', email)
    print('mark  is ', mark)
    print('addr is ', addr)

student('Alice', 123, 25, 'Alice@gmail.com')
print()


def student(name, id, mark, email='no', addr='no'):
    print('name is  ', name)
    print('id  is ', id)
    print('email  is ', email)
    print('mark  is ', mark)
    print('addr is ', addr)

student('Alice', 123, 25, addr='Bhubaneswar')
