# wap to read the numbers until -1 is entered, also count the negatives, positives, and zeros entered by the user
# neg=0
# pos=0
# zero=0
# while 1:
#     i=int(input("Enter a number: (If you want to exit enter -1)"))
#     if i==(-1):
#         break
#     elif i==0:
#         zero=zero+1
#     elif i<0:
#         neg=neg+1
#     else :
#         pos=pos+1

# print("The no of positive number is ",pos)
# print("The no of negative number is ",neg)
# print("The no of zero's  is ",zero)


# other ways

num=int(input("Enter a number: (If you want to exit enter -1)"))
np=0
nn=0
nz=0
while num!=-1:
    if num> 0:
        np=np+1
    elif num<0:
        nn=nn+1
    else:
        nz=nz+1
    num=int(input("Enter a number: (If you want to exit enter -1)"))

print("The no of positive number is ",np)
print("The no of negative number is ",nn)
print("The no of zero's  is ",nz)


