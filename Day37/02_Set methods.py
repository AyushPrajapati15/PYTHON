# set methods
# add()
s={10,20,30,40,50}
s.add('alice')
print(s)
# s={10,20,30,40,50}  it has no effect
# s.add(20)
# print(s)
print()
 
# update()
s={10,20,30,40,50}
l=[11,22,33,44,55]
t=('alice',32,42,52)
s.update(l,t)
print(s)
print()

s={10,20,30,40,50}
l=[11,22,33,44,55]
t=('alice',32,42,52)
s.update(l,t,range(50,60))
print(s)
print()

# remove()
s={10,20,30,40,50}
s.remove(40)
# s.remove(55) :-key error
print(s)
print()


# discard()
s={10,20,30,40,50}
s.discard(10)
s.discard(55)
print(s)
