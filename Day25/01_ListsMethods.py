# count()
l=[10,10,20,50,90,50,10,30,50,30,10]
print(l.count(10))
print(l.count(30))
print(l.count(50)) 
print(l.count(44)) # it will give 0
print()


# index()
l=[10,20,30,40,50,60,70,80,90]
print(l.index(50))
print(l.index(90))
print(l.index(10))
# print(l.index(100)) it will give value error
print()


#  remove()
l=[11,22,33,22,44,55,66]
l.remove(22)
# l.remove(65) it will give value error as 65 is not present in the list
print(l)
print()


#  pop()
l=[12,22,32,42,52,62]
l.pop()
print(l)
l.pop(3)
print(l)
# l.pop(55)  it will give index error
print()

# extend()
l=[10,20,30,40,50]
s=[100,200,300]
l.extend(s)
print(l)
print()

# reverse()
l=[13,23,33,43,53]
l.reverse()
print(l)
print()

#  sort()
l=[10,25,15,22,30,19,11,]
l.sort()
print(l)
l.sort(reverse=True)
print(l)
l=['bob','alice','mary','jack']
l.sort()
print(l)
print()


#  clear()
l=[1,4,61,5,2,4,3,4,56,1,4,5,1]
print(l)
l.clear()
print(l)
print()


# copy()
l=[11,22,33,44,55,66,77,88]
s=l.copy()
print(l)
print(s)
print(id(l))
print(id(s))

s[2]=25 #update
print(l)
print(s)

