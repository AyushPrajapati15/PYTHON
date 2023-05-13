#  break com=ntinue pass
# how to exit from the loop 
for i in range(10):
    print(i,end=" ")
    if i==5:
        break
print("")

# continue---skip
for i in range(10):
    if i==7:
        continue
    print(i,end=" ")
print("")

# pass- empty statement  
# if you want to provide empty body then go for pass statement
for i in range(10):
    if i%2==0:
        print(i,end=" ")
    else:
        pass
print("")


for i in range(10):
    if i%2==0:
        pass
    else:
        print(i,end=" ")