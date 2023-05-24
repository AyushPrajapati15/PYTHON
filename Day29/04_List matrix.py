# Nested list as a matrix
l=[[10,20,30],[40,50,60],[70,80,90]]
print(l)
print()

print(l[0])
print(l[1])
print(l[2])
print()

# print row wise using loop
l=[[11,21,31],[41,51,61],[71,81,91]]
 
for i in l:
    print(i)
print()


# print without bracket and comma
l=[[11,21,31],[41,51,61],[71,81,91]]
 
for i in l:
    for j in i:
        print(j,end=" ")
    print()
print()


# reverse a list     
l=[10,20,30,[11,22,33],50,[12,22,32,42],70]
l.reverse()
print(l)


