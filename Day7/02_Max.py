a = 5
print("a is 5")
b = 10
print("b is 10")
c = 7
print("c is 7")
max_num = a
max_num = (b > max_num) and b or max_num
max_num = (c > max_num) and c or max_num
print("The maximum of three number is ",max_num) # output: 10
