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



# sometimes alpha sometime digits
print(rn.choice(alpha+digits))

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


for i  in range(10):
    print(rn.choice(alpha+digits),
      rn.choice(digits+alpha),
      rn.choice(special_symbols),
      rn.choice(digits),
      rn.choice(alpha),
      rn.choice(alpha),
      sep='')