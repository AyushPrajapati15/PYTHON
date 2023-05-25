# List comprehension
l=[i for i in range(11)]
print(l)
print()

l=[i*i for i in range(11)]
print(l)
print()

# print power of digits
l=[i**i for i in range(11)]
print(l)
print()

l=[i+10 for i in range(11)]
print(l)
print()

# print l if it is divisible by 2
l=[i for i in range(1,21) if i%2==0]
print(l)
print()

# name=['Alice','Bob','Mary','Jack','David']
# Expected output : ['A','B','M','J','D']
name=['Alice','Bob','Mary','Jack','David']
l=[i[0] for i in name]
print(l)
print()


l=[i[0:2] for i in name]
print(l)
print()

# Expected output : ['Ae','Bb','My','Jk','Dd']
l=[i[0]+i[-1] for i in name]
print(l)
print()

# print if a is there in names
l=[i for i in name if 'a' in i]
print(l)
print()

l=[i if i!='Mary' else 'Hello' for i in name ]
print(l)
print()


# Create a list from tuple
t=(10,20,30,40,50)
l=[i for i in t ]
print(l)
print()
 
t=(10,20,30,40,50)
l=[i for i in t if i%6==0]
print(l)
print()


# Create a list from string
name='Alice'
l=[i for i in name]
print(l)
print()


# Creation of matrix using list comprehension
m=[[j for j in range(3)] for i in range(3)]
print(m)
print()

m=[[i for j in range(3)] for i in range(3)]
print(m)
print()

m=[[i*j for j in range(3)] for i in range(3)]
print(m)