a=[10,20,30,40] # lists 
b=bytes(a) # lists to bytes
print(a[0])
print(a[1])
print(a[2])
print(a[3])
print(b[-1])
print(a[-2])
print(a[-3])
print(a[-4])

# a=[10,500] # Range=0-255    NOT VALID
# b=bytes(a)
# print(b[1])

a=[10,20,30,40,50 ]
b=bytearray(a)
print(b[1])
print(a[2])
print(a[3])
print(a[-1])
print(a[-2])
print(a[-3])

# nmodifying the index value
b[1]=200
print(b[1])