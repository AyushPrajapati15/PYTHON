# creation of 4 digit OTP using manual way

import random



print(random.randint(0,9),
      random.randint(0,9),
      random.randint(0,9),
      random.randint(0,9),sep='')
print()


# Generating 4 digit OTP using loop

otp=''
for i in range(4):
    otp=otp + str(random.randint(0,9))

print(otp)