for i in range(3):
    for j in range(3):
        print(i,j)
        # print("i is ={} j is = {}".format(i,j))
print("")

for i in range(3):
    for j in range(3):
        print('*',end="")
    print("")

for i in range(0,6,1):
    for j in range(0,i,1):
        print("*",end="")
    print("")
print("")


for i in range(5,0,-1):
    for j in range(i,0,-1):
        print("*",end="")
    print("")