# Setdefault
# if the key is not available then it is going to add the key and value to the dict 
d={10:'alice',20:'bob',30:'mary',40:'jack',50:'david',}
print(d.setdefault(55,'jerry'))
print()
print(d)
print()

#  if the key is available then t will return the corresponding vlue
d={10:'alice',20:'bob',30:'mary',40:'jack',50:'david',}
print(d.setdefault(20,'jim'))
print()
print(d)
print()

#update() 
d1={10:'alice',20:'bob',30:'mary',40:'jack',50:'david',}
d2={1:'college',2:'unniversity'}
d1.update(d2)
print(d1)
print()
print(d2)
print()


d1={10:'alice',20:'bob',30:'mary',40:'jack',50:'david',}
d2={10:'college',2:'unniversity'}
d1.update(d2)
print(d1)
print()
print(d2)
print()


# copy()
d1={10:'alice',20:'bob',30:'mary',40:'jack',50:'david',}
d2={}

d2=d1.copy()
# d2=d1  pointig to same memory location
print(d2)
print()
print(id(d1))
print()
print(id(d2))
print()

d1[20]='jerry'
print(d1)
print(d2)
print()


# clear()
d={10:'alice',20:'bob',30:'mary',40:'jack',50:'david',}
d.clear()
print(d)


# fromkeys()
# dict from list
l=[10,20,30,40,50]
d=dict.fromkeys(l)
print(d)
print()

# dict from tuple
l=(10,20,30,40,50)
d=dict.fromkeys(l)
print(d)
print()


l=(10,20,30,40,50)
d=dict.fromkeys(l,'hello')
print(d)
print()

d=dict.fromkeys(range(5))
print(d)
print()

d=dict.fromkeys(range(5),[1,2,3])
print(d)
print()

d=dict.fromkeys([],[1,2,3])
print(d)
print()

d=dict.fromkeys([],[])
print(d)
print()

d=dict.fromkeys([1],[1])
print(d)
print()


l=(10,20,30,40,50)
d={}.fromkeys(l,'hello')
print(d)
print()