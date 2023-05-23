# Wap tp search an value form a list then display its index("If the value is present multiple times then print its all indices and also count the number of times that value repeated in the list")
l=[10,20,30,10,20,40,50,10,60]
key=int(input("Enter an element to search "))

i=0
count=0

while i<len(l):
    if key==l[i]:
        print(f'{key} is present at {i} index')
        count=count+1
    i=i+1

print(f'{key} is present {count} times')
