for i in range(10):
    print("Alice",end=" ")
print("\n")

# Odd no's
for i in range(1,11,1):
    print(i,end=" ")
print("\n")

# Even no's
for i in range(0,11,2):
    print(i,end=" ")
print("\n")

# 100 200 300 400 500 600 700 800 900 1000

for i in range(100,1001,100):
    print(i,end=" ")
print("\n")

# 10 9 8 7 6 5 4 3 2 1
for i in range(10,0,-1):
    print(i,end=" ")
print("\n")

# print even no's from 100-120
for i in range(100,121,1):
    if i%2==0:
        print(i,end=" ")
print("\n")

# 
name="Alice"
for i in name:
    print(i,end="")
print("\n")

# Sum of first 10 number
sum=0
for i in range(0,11,1):
    sum=sum+i
print(sum)