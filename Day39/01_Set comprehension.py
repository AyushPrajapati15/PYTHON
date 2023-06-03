# Set comprehension
# without Set comprehension
l=[10,20,30,40]
# s=set(l)
# print(s)
s=set()
for i in l:
    s.add(i)
print(s)


# with Set comprehension
l=[10,20,30,40,50]
s={i for i in l}
print(s)
print()

l=[11,22,33,44,55]
s={i*2 for i in l}
print(s)
print()


s={i for i in range(100,111)}
print(s)
print()

s={i**2 for i in range(11)}
print(s)
print()

# create a set by adding all the elements from 20-40 which is divisible by 4

s={i for i in range(20,41) if(i%4==0)}
print(s)
print()

# Create a set from lists called as names
names=['alice','bob','mary','jack','david']
s={i for i in names}
print(s)
# Create a set from lists called as names by adding the first character of each element in uppercase
names=['alice','bob','mary','jack','david']
s={i[0].upper() for i in names}
print(s)
print()

# Create a set from lists called as names by adding all the elements but if element is alice then print jerry
names=['alice','bob','mary','jack','david']
s={i if i!='alice' else 'jerry' for i in  names} 
print(s)