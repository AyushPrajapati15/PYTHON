#   creation of empty  set
s={}
print(s)
print(type(s))

#   creation of set using set()
s=set()
print(s)
print(type(s))
print()

#  creation of set  with multiple elements
s={23,33,43,53,63,'Alice'} # set doesn't maintin order
print(s)
print(type(s))
print()

#  creation of set using set()
# creation of set from list
l=[10,20,30,40,50]
s=set(l)
print(s)
print(type(s))
print()

# creation of set from tuple
t=(10,20,30,40,50)
s=set(t)
print(s)
print(type(s))
print()

# creation of set from range()
s=set(range(10))
print(s)
print(type(s))
print()

# creation of set from str
name="Alice Doe"
name1="Joh doe"
s=set(name)
s1=set(name1.split())
print(s)
print(s1)
print(type(s))
print()

#   in and not in 
s={10,20,30,'Alice','John'} 
print('Alice' in s) #Case sensetive
print('Bob' in s)
print('Alice'not in s )