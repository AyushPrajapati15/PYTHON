# Accessing String elements by using slice operator
# Slice represents a part or a piece of string
#  Syntax --->  [start index : stop index : step size] --> [1:10:1] - o/p-> 1,2,3,4,5,6,7,8,9
str="Hello python"
print(str[1:5:1])

print(str[::]) # --> it will take the default value i.e [0:12:1]

print(str[::2]) # --> [0:12:2]
print(str[:5000:2])
print(str[::-1]) # backward printing -1 to 12

print(str[::-2])
print(str[-9:-7:-1])
print(str[5:10:-1])
print(str[5000:2:-1])

print(str[-5::]) 
print(str[-1:-4:-1])
print(str[:-4:])
print(str[-4:-1:])
print(str[2:9])
print(str[2:])
print(str[::+-1])
print(str[::-+1])

print(str[1:-9:])
print(str[-2:-9:])
print(str[True:-1:1])
print(str[False+10:(True-True):-1])


