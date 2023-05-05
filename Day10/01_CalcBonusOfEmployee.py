sal=int(input("Enter your Salary\n"))
gender=input("enter yor gender\n")

if gender=='m':
    bonus=0.05*sal
else:
    bonus=0.1*sal
if sal<15000:
    bonus=bonus+0.03*sal

sal=bonus+sal
print("Salary is",sal)
