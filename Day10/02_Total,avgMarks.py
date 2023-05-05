marks1=int(input("Enter your marks1: "))
marks2=int(input("Enter your marks2: "))
marks3=int(input("Enter your marks3: "))
marks4=int(input("Enter your marks4: "))
marks5=int(input("Enter your marks5: "))
marks6=int(input("Enter your marks6: "))

total=marks1+marks2+marks3+marks4+marks5+marks6
avg=total/6
print(total)
print(avg)

if avg>=90:
    print("O Grade")
elif avg>=80 and avg<=89:
    print("A Grade")
elif avg>=70 and avg<=79:
    print("B Grade")
elif avg>=60 and avg<=69:
    print("C Grade")
elif avg>=50 and avg<=59:
    print("D Grade")
elif avg>=40 and avg<=49:
    print("E Grade")
else :
    print("Fail---Better luck next time")