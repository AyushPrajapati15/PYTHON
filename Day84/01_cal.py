import hello  # here we are importing hello modules  that means we can access all the mebers of hello modules 
print(hello.add(10,20))
print(hello.sub(10,20))
print(hello.mul(10,20))
print(hello.div(10,20))
print()


import math
print(math.factorial(5))
print(math.factorial(6))
print()

#module alish
import hello as h
print(h.add(100,1000))
print(h.pi)
print(hello.sub(1000,20))
print()

#Different ways of imporing modules
from hello import add ,sub,mul
print(add(100,29))
print(sub(100,20))
print(mul(10,20))
print()
from hello import *
print(add(10,30))
print(sub(10,20))
print(pi)
print()

#module member alishing 
from hello import add as a ,sub as s , pi as p 
print(a(10,1))
print(pi)
print(p)