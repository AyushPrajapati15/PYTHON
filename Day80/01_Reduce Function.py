#find the sum of all element present inside list without using lambda 
from functools import reduce
def add(x,y):
    return x+y
print()


l=[1,2,3,4,5]
data=reduce(add,l)
print(data)
print()


def add(x,y):
    return x*y

l=[1,2,3,4,5]
data=reduce(add,l)
print(data)
print()


#find the sum of all element present inside list with using lambda 
l1=[1,2,3,4,5]
data=reduce(lambda x,y:x+y,l1)
print(data)
print(type(data))
print()


#find the product of all element present inside list with using lambda 
l1=[1,2,3,4,5]
data=reduce(lambda x,y:x*y,l1,10)
print(data)
print()


# find out the sum of all the elements from 1 to 100
data=reduce(lambda x,y:x+y,range(1,101))
print(data)
print()


#working with list which is containg string data 
names=['surendra','priyanka','rahul','zini']
data=reduce(lambda x,y:x+y,names,'hello')
print(data)
print(type(data))