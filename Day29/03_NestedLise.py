# Nested list
l=[10,20,30,[11,22,33],50,60,70]
print(l)
print(l[2])
print(l[3])
print(l[-4])
print(l[3][2])
print(l[-4][-3])
print(l[3][1])
print()

l=[10,20,30,[11,22,33],50,[12,22,32,42],70]
print(l)
print(l[2:6]) # using slice operator
print(l[3])
print(l[3][1])
print(l[5])
print(l[5][2])
print()

l=[10,20,30,[11,22,[1,2,3],33],50,[12,22,32,42],70]
print(l)
print(l[3][2][1])