l=[1,2,3,5,6,7,9,11,12,17,18,23,24,25,67,92,99]
ch=int(input("Enter your lucky number "))

if ch in l:
    print("Yes your lucky number is present in the lst")
else:
    print("No your lucky number is not present in the ist")
print()


# Wap to check your lucky no until your lucky no is matched with list elements


l=[1,2,3,5,6,7,9,11,12,17,18,23,24,25,67,92,99]
ch=int(input("Enter your lucky number"))

while True:
    if ch in l:
        print("Yes your lucky number is present in the lst")
    else:
        print("No your lucky number is not present in the ist")
        ch=int(input("Enter your lucky number again: "))
