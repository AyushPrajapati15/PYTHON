# direct recursion 

# it wil run for infinite no of times
# def fun():
#     print("1")
#     fun()

# fun()


print("Indirect recursion")
# Indirect recursion 
def fun1(num):
    if num<=6:
        print(f'fun1 is {num*2}')
        fun2(num+1)
    return


def fun2(num):
    if num<=6:
        print(f'Fun2 is {num*100}')
        fun1(num+1)
    return

fun1(1)
print()


print("tail recursion")
# tail recursion
def fun(num):
    if num == 4:
        return
    else:
        print(num)
        fun(num+1)

fun(1)
print()


print("non-tail recursion")
# non - tail recursion

def fun(num):
    if num == 4:
        return
    else:
        fun(num+1)
        print(num)


fun(0)