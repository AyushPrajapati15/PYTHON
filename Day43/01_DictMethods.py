# ictionary methods
# get()
d={10:'alice',20:'bob',30:'mary',40:'jack',50:'david',}

print(d.get(10))
print()
print(d.get(30))
print()
print(d.get(99)) #o/p-none
print()
print(d.get(99,'Unknown')) 
print()


# items()
d={10:'alice',20:'bob',30:'mary',40:'jack',50:'david',}
print(d.items())
print()

# printing line by line
d={10:'alice',20:'bob',30:'mary',40:'jack',50:'david',}
for i in d.items():
    print(i)
print()


d={10:'alice',20:'bob',30:'mary',40:'jack',50:'david',}
for i,j in d.items():
    print(i,' ',j)
print()


# pop()
d={10:'alice',20:'bob',30:'mary',40:'jack',50:'david',}
print(d.pop(10))
print(d)
print()


# popitems()
d={10:'alice',20:'bob',30:'mary',40:'jack',50:'david',}
print(d.popitem())
print()
print(d)
print()


# keys()
d={10:'alice',20:'bob',30:'mary',40:'jack',50:'david',}
print(d.keys())
print()

d={10:'alice',20:'bob',30:'mary',40:'jack',50:'david',}
for i in d.keys():
    print(i)
print()


# values()
d={10:'alice',20:'bob',30:'mary',40:'jack',50:'david',}
print(d.values())
print()

d={10:'alice',20:'bob',30:'mary',40:'jack',50:'david',}
for i in d.values():
    print(i)
print()


