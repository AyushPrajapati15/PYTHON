# Creation of tuple in diff diff way
# creation of empty tuple
t=()
print(t)
print(type(t))
print()

# creation of tuple with single value
# t=(23) # error
t=(23,)
print(t)
print(type(t))
print()

# creation of tuple with different data items
t=(23,'Alice',55.55,True)
print(t)
print()

# creation of tuple without using ()
t=10,20,30,'Alice',False,55.55
print(t)
print(type(t))
print()

# creation of tuple using tuple() 
l=[10,20,30,40,50]
t=tuple(l)
print(t) #list to tuple
print(type(t))
print()

t=tuple(range(10))
print(t)
print()

t=tuple('alice')
print(t) # it will give a l i c e
t=('alice',)
print(t) # it will give alice
print()

# accessing tuple elements index wise
t=(10,20,30,40)
print(t[1])
print(t[2])
print(t[3])
print()

# Accessing by slice operator
t=(10,20,30,40,50)
print(t[::])
print(t[:2])
print(t[::2])
print()

# mathematical operations on tuple
t=(10,20,30)
u=(11,22,33)
p=(11,21,31)
l=t+u+p
print(l)
print()

# repetition operator(*)
t=(10,20,30,40,50)
l=t*3
print(l)
print()



