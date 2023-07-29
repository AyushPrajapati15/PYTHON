# Date Time module

import datetime

d=datetime.date(2023,5,9)
print("Date")
print(d)
print(d.day)
print(d.month)
print(d.year)
print()

t=datetime.time(17,55,45,458665)
print("Time")
print(t)
print(t.minute)
print(t.second)
print(t.minute)
print()

dt=datetime.datetime(2023,7,29,17,15,50,4585)
print("DateTime")
print(dt)
print()

ct=datetime.datetime.now()
print("Current DateTime")
print(ct)
print(ct.day)
print(ct.month)
print(ct.year)
print(ct.hour)
print(ct.minute)
print(ct.second)
print(ct.microsecond)
print()

ct=datetime.datetime.now()
h=ct.hour
print(h)

if h>=6 and h<12:
    print("Good morning...!")
elif h>=12 and h<18:
    print("Good afternoon...!")
elif h>=18 and h<24:
    print("Good evening...!")
else:
    print("Good night...!")
print()

# Custom dateTime
ct=datetime.datetime.now()
print(ct)
print(ct.strftime('%a'))
print(ct.strftime('%A'))
print(ct.strftime('%w'))
print(ct.strftime('%W'))
print(ct.strftime('%m'))
print(ct.strftime('%M'))
print(ct.strftime('%d'))
print(ct.strftime('%D'))
print(ct.strftime('%y'))
print(ct.strftime('%Y'))
