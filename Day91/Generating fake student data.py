# Generating fake student data without faker module

#generate student name 
from random import *
alpha="abcdefghijklmnopqrstuvwxyz"

for i in range(20):
    fname=choice(alpha).upper()
    lname=choice(alpha).upper()
    for i in range(randint(3,13)):
        fname=fname+choice(alpha)
        lname=lname+choice(alpha)
    print(fname,lname)

#studnet mobile no 
digits="0123456789"

for i in range(20):
    smob=choice('9876')
    for i in range(9):
        smob=smob+choice(digits)
    print(smob)

#sage
for i in range(20):
    sage=randint(16,25)
    print(sage)
    
cities=['bbsr','cuttack','hyd','delhi','puri']
for i in range(20):
    saddr=choice(cities)
    print(saddr)
    
course=['Btech','MCA','MBA','MTECH','PHD','MSC','MA']
for i in range(20):
    scourse=choice(course)
    print(scourse)
    
#sid 
digits="0123456789"


for i in range(20):
    sid='xyz-'
    for i in range(6):
        sid=sid+choice(digits)

    print(sid)