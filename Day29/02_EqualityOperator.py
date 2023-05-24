# List comparison using equality operator
l=['alice','bob','mary','jack']
s=['Alice','Bob','Mary','jack']
p=['alice','bob','mary','jack']

print(l==s)
print(l==p)

l=['alice','bob','mary','jack']
s=['Alice','Bob','Mary','jack']
print(l>s) # ASCII of A<a so a is greater

l=[10,20,30,40]
s=[11,22,33,44]
print(l!=s)

l=[10,20,30,40]
l=[20,10,30,40]  # contents are not same
print(l==s)

l=[10,20,30,40]
s=[11]
print(l>s)
l=[10,20,30,40]
s=[11] # 10<11
print(l>s)

l=[10,20,30,40]
s=[9]
print(l>s) # 10>9