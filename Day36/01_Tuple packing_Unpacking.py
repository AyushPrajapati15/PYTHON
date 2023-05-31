# Tuple packing and unpacking

# Packing
a=10
b=20
c=55.5
d='Alice'
e='Bob'
t=a,b,c,d,e  #Packing
print(t)
print(type(t))
print()

# Unpacking :- At the time of unpacking the number of variables and the number of value musst be same

t=(10,20,30,'Alice','Jack',55.5)
a,b,c,d,e,f=t # Unpacking
print(a,b,c,d,e,f)
print(type(a))
print()

# Nested tuple
t=((10,20,'Alice',55.5),(40,50,'Mary',75.58))
print(t[0])
print(t[1])
print()
print(t[0][2])
print(t[1][2])
print()

for i in t:
    print(i)