# create 8 char password that contains alphanumeric and special symbols
import random as rn

alpha ='ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
digits='0123456789'
special_symbols='!@#$%^&*()_+{}<>' 
print(rn.choice(alpha),
      rn.choice(digits),
      rn.choice(special_symbols),
      rn.choice(digits),
      rn.choice(alpha),
      rn.choice(alpha),sep='')
print()


# sometimes alpha sometime digits
print(rn.choice(alpha+digits),
      rn.choice(special_symbols+digits),sep='')
print()

alpha ='ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
digits='0123456789'
special_symbols='!@#$%^&*()_+{}<>' 
print(rn.choice(alpha+digits),
      rn.choice(digits+alpha),
      rn.choice(special_symbols),
      rn.choice(digits),
      rn.choice(alpha),
      rn.choice(alpha),
      sep='')
print()


for i  in range(10):
    print(rn.choice(alpha+digits),
      rn.choice(digits+alpha),
      rn.choice(special_symbols),
      rn.choice(digits),
      rn.choice(alpha),
      rn.choice(alpha),
      sep='')