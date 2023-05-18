# List traversing

l=[0,1,2,3,4,5,6,7,8,9]
print(l)

# # traversing using for loop
l=[10,20,30,40,50,60]
for i in l:
    print(i)
print()
    
# traversing using while loop
l=[11,22,33,44,55,66,77,88,99]
i=0
while i<9: # or i<len(l)
    print(l[i])
    i=i+1
print()

# print if l[i]%2==0 
l=[15,25,45,66,39,84,23,64,67]
for i in l:
    if i%2==0 and i%4==0:
        print(i)
print()

for i in l:
    if i%2==0:
        print(i)