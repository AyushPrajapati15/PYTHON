# Filter function

#write a program to filter all the even value from a list without using lambda
def checkEven(x):
    if x%2==0:
        return True 
    else:
        return False

l=[10,20,21,13,15,16,18,67,51]
data=list(filter(checkEven,l))
print(data)

#write a program to filter all the even value from a list with using lambda
l=[10,20,21,11,33,17,89,56,19,50]
data=list(filter(lambda x:x%2==0,l))
print(data)

 
l=[10,20,21,33,17,89,56,19]
data=tuple(filter(lambda x:x%2==0,l))
print(data)

l=[10,20,21,33,17,89,56,19]
data=set(filter(lambda x:x%2==0,l))
print(data)

#write a program to filter all the even value from a list with using lambda in single 
print(list(filter(lambda x:x%2==0,[10,20,33,12,32,89,76])))

print(tuple(filter(lambda x:x%2==0,[10,20,33,12,32,89,76])))

print(list(filter(lambda x:x%2!=0,[10,20,33,12,32,89,76,111,231])))

#filter all the negative from a sequence using filter 
l=[10,20,-39,49,-87,-65,-31]
data=list(filter(lambda x:x<0,l))
print(data)
# print(list(filter(lambda x:x<0,l)))

# filter out all the common element from both list using filter() function 
a=[10,20,30,40,50]
l=[100,200,30,40,70]

data=list(filter(lambda x:x in a,l))
print(data)

# filter only one name Bob from a list uisng filter function
names=['Alice','Bob','Jack','Jerry','Bob']
data=list(filter(lambda x:x=='David',names))
print(data)

names=['Alice','Bob','Jack','Jerry','Bob']
data=list(filter(lambda x:x!='David',names))
print(data)

d={
    1:'Alice',
    2:'Bob',
    3:'Jack',
    4:'Jerry',
    5:'David',
    6:'Marry'
}

data=dict(filter(lambda x:x[0]%2==0,d.items()))
print(data)

d={
    1:'Alice',
    2:'Bob',
    3:'Jack',
    4:'Jerry',
    5:'David',
    6:'Marry'
}

data=list(filter(lambda x:x%2==0,d.keys()))
print(data)
print(d.keys())
