# It is of two types --> Implicit And Explicit Typecasting
#  Implicit Typecasting --> it means automatic typecasting by python
a=100
b=3
c=a/b
print(type(c))
print(c)

a1 = 10
b1 = 20.33
c1 = a1 + b1
print(c1)
print(type(c1))

#  Explicit Typecasting --> Here user will convert

# Other to int 

# other(float,bool,str) to int possible except complex / str to int possible but it must contain int value

# float to int--------------

num=int(33.33)
print(num)
print(type(num))

# complex to int-------------

# num1=int(50+60j) ----------> invalid not possible
# print(num1)

# bool to int ------------
num2 = int(True)
print(num2)
print(type(num2))

num2 = int(False)
print(num2)

num2 = int(True+True+True)
print(num2)

num2 = int(True+True+False)
print(num2)

# str to int -------------------
# val = int('Hello')---> not possible we have to pass value
# print(val)

val1=int('100')
print(val1)

# ***********************other to float****************

# other(float,bool,str) to float possible except complex / str to float possible but it must contain float value

# int to float--------------

num=float(30)
print(num)
print(type(num))

# complex to float-------------

# num1=float(50+60j) ----------> invalid not possible
# print(num1)

# bool to float ------------
num2 = float(True)
print(num2)
print(type(num2))

num2 = float(False)
print(num2)

num2 = float(True+True+True)
print(num2)

num2 = float(True+True+False)
print(num2)

# str to float -------------------
# val = int('Hello')---> not possible we have to pass value
# print(val)

val1=float('100')
print(val1)


# ***********************other to complex****************

# other(float,bool,str) to complex possible but str must contain int or float value

# int to complex--------------

num=complex(30)
print(num)
print(type(num))

# float to complex-------------

num1=complex(33.33) 
print(num1)

# bool to complex ------------
num2 = complex(0b1111)
print(num2)
print(type(num2))

# str to complex -------------------
# val = int('Hello')---> not possible we have to pass value
# print(val)

val1=complex('100')
print(val1)
