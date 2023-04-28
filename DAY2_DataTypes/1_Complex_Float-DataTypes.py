# Float DataType Scientific notations


# j=2.2e450  # --> 2.2 * 10^450 = Infinity(Inf)
i=2.2e4  # --> 2.2 * 10^4 = 22000.0
print(i)

k = 2255_5474.1465464_46466
print(k)

# f = 0b1111.10 # -- > we can't store binary, octal, hexadecimal no in float.

# --------- Complex DataType  ---------

#                Syntax
#    
#         a + bj   ---> a - real i.e we can store in,float values
#                  ---> bj - it is the imaginary part. Here 'j' is not_case sensitive
a =50+60j
print(type(a))
print(a)

b = 45.55+50j
print(b)

c = 45.555+22.336J # it will automatically print small 'j' .
# c=25+55k  ----> Error we can only use 'j' or 'J' 
print(c)
print(c.real) # --> it will only print "real" part
print(c.imag) # --> it will only print "imag" part without 'j'

#  In real part we can set any type of values i.e int,decimal,bool,hexa.. etc byt in inaginary part we cam set only decimal values

d = 0b1111+50j #--> Valid
print(d)

# e = 0b1111 + 0b1111j ----> Invalid
# print(e)

f = 10j+20j # ---> ir=t will add two numbers
print(f)

num1=50+40j
num2=60+70j
res=num1+num2
print(res)
