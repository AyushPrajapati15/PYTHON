# calender module
import calendar as c 
days_name=list(c.day_name)
print(days_name)
print()

for i in days_name:
    print(i)
print()

for i in days_name:
    print(i[:-3])
print()

da=list(c.day_abbr)
print(da)
print()

for i in da:
    print(i)
print()
   
mn=list(c.month_name)
print(mn)
print()

for i in mn:
    if i=='':
        continue
    print(i)
print()

print(c.isleap(2020))

print(c.isleap(2010))

print(c.isleap(2012))

print(c.leapdays(2000,2022))

print(c.weekday(2022,9,7))

print(c.weekday(2022,9,9))

print(c.weekheader(3))
print()

print(c.calendar(2022))
print()


print(c.calendar(2000))
print()


print(c.monthcalendar(2022,9))
print()

print(c.monthcalendar(2022,1))
print()

# print(help(c.day_name))

# print(help(c.monthcalendar))


# print(help(c.day_name))

# print(dir(c))