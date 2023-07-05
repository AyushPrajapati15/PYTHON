# nested function
def outer_fun():
    print('i m inside outer fun')

    def inner_fun():
        print('i m inside inner fun')
    inner_fun()

outer_fun()
print()


def outer_fun():
    print('i m inside outer fun')

    def inner_fun():
        print('i m inside inner fun')

outer_fun()
# inner_fun()
print()


def outer_fun():
    print('i m inside outer fun')

    def inner_fun():
        print('i m inside inner fun')
    inner_fun()

outer_fun()
# inner_fun()




