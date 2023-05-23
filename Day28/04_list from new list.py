#  Input:
# l=['Alice','Bob','Mike','Jack','Mary']
# Expected output
# ['Ae', 'Bb', 'Me', 'Jk', 'My']
l=['Alice','Bob','Mike','Jack','Mary']

new_list=[]
# for i in l:
#     new_list.append(i[0]+i[-1])
for i in l:
    n=len(i)
    new_list.append(i[0]+i[n-1])

print(new_list)