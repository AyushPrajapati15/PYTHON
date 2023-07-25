# Generating fake student data without faker module

#generate student name 
from random import *
alpha="abcdefghijklmnopqrstuvwxyz"

for i in range(10):
    fname=choice(alpha).upper()
    lname=choice(alpha).upper()
    for i in range(randint(3,13)):
        fname=fname+choice(alpha)
        lname=lname+choice(alpha)
    print(fname,lname)
print()

#studnet mobile no 
digits="0123456789"

for i in range(20):
    smob=choice('9876')
    for i in range(9):
        smob=smob+choice(digits)
    print(smob)
print()

#s_age
for i in range(20):
    sage=randint(16,25)
    print(sage)
print()

cities=['bbsr','cuttack','hyd','delhi','puri']
for i in range(20):
    saddr=choice(cities)
    print(saddr)
print()
  
course=['Btech','MCA','MBA','MTECH','PHD','MSC','MA']
for i in range(20):
    scourse=choice(course)
    print(scourse)
print()
   
#sid 
digits="0123456789"


for i in range(20):
    sid='xyz-'
    for i in range(6):
        sid=sid+choice(digits)

    print(sid)