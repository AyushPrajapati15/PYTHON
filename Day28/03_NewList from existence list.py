# s=['Alice','Bob','Mike','Jack','Mary']
# Expected output:
# ['HiAlice', 'HiBob', 'HiMike', 'HiJack', 'HiMary']
# ['HiAlice', 'HiBob', 'HiMike', 'HiJack', 'HiMary', 'HelloAlice', 'HelloBob', 'HelloMike', 'HelloJack', 'HelloMary']

l=['Hi','Hello']
s=['Alice','Bob','Mike','Jack','Mary']

new_list=[]

for i in l:
    for j in s:
      new_list.append(i+''+j)  
    print(new_list)