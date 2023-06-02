# pop()
s={10,20,30,40,50}
s.pop()
print(s)
print()

s={11,22,33,44,55}
print(s.pop())
print()

# copy :- Shallow copy

s1={10,20,30,40,50}
s2=s1.copy()
print(s1)
print(s2)
print(id(s1))
print(id(s2))
print()

s1.add(9999) # it will add to s1 only
print(s1)
print(s2)
print()

# copy:- Deep copy
s1={10,20,30,40,50}
s2=s1 #Here both will point to same memory location it is called assigning
print(s1)
print(s2)
print(id(s1))
print(id(s2))
print()

s1.add(999) # it will add to both 
print(s1)
print(s2)
print()


# clear()
s={11,22,33,44,55}
print(s)
s.clear()
print(s)
print()


# enumerate()
s={10,20,30,40,50}
for i in enumerate(s):
    print(i)
print()

for i,j in enumerate(s):
    print(i,j)
print()

# min() and max()
s={12,22,32,42,52}
print("The minimum of s elements is ",min(s))
print("The maximum of s elements is ",max(s))
print()

# Sum()
s={11,22,33,44,55}
print(sum(s))
print()

# Sorted()
s={5,1,2,4,3,6}
print(sorted(s))
print(sorted(s,reverse=True)) # it will sort in decending order 