a = int(input("Enter 1st number "))
b = int(input("Enter 2nd number "))

ch=input("Enter your choice: \nadd\nsub\nmul\ndiv:---- ")

if ch=='add':
    print(a+b)
elif ch=='sub':
    print(a-b)
elif ch == 'mul':
    print(a*b)
elif ch == 'div':
    print(a/b)
else:
    print("Invalid input")