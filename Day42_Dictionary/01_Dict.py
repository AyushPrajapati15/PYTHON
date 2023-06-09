myInfo={
    'name':'Alice',
    'email':'alice@gmail.com',
    'address':'bhubaneswar',
    'mobile':9876543211
}

print(myInfo['name'])
print(myInfo)
print()

# different ways for creating a dict

# empty dict
d={}
print(d)
print(type(d))
print()


# create empty dict then add item
d={}
d['name']='jack'
d['address']='cuttack'
d['email']='jack@gmail.com'
d['mobile']=9987666987
print(d)
print()

# creating dict directly
d={1:'Alice',2:'Jack',3:'Bob',4:'Mary',5:'David'}
print(d)
print(d[1])
print()

# Empty dictionary using dict()
d=dict()
print(d)
print(type(d))
print()

# check the key is exist or not
d={1:'Alice',2:'Jack',3:'Bob',4:'Mary',5:'David'}
print(2 in d)
print(2 not in d)
print()
# create a dictionary dynamically by taking user input 
d={}
while True:
    key=input("Enter the key: ")
    val=input("Enter the val: ")
    d[key]=val

    choice=input('Do you want to addd more element Y/N : ' ).upper()
    if choice=='N':
        break
print(d)
print()

# traversing a dict
d={1:'Alice',2:'Jack',3:'Bob',4:'Mary',5:'David'}
for i in d:
    print(i)
print()

# print key and value\
d={1:'Alice',2:'Jack',3:'Bob',4:'Mary',5:'David'}
for i in d:
    print(i,d[i])
print()

# Add items
d={1:'Alice',2:'Jack',3:'Bob',4:'Mary',5:'David'}
d[2]='Jim'
print(d)
print()

# update
d={1:'Alice',2:'Jack',3:'Bob',4:'Mary',5:'David'}
d[1024]='Harry'
print(d)
print()

# delete
# d={1:'Alice',2:'Jack',3:'Bob',4:'Mary',5:'David'}
# del d[1024]
# print(d)
# print()

# delete all the items
# d={1:'Alice',2:'Jack',3:'Bob',4:'Mary',5:'David'}
# d.clear()
# print(d)
# print ()

# how to delete entire dictionary
# d={1:'Alice',2:'Jack',3:'Bob',4:'Mary',5:'David'}
# print(d)
# del d
# print(d)


# dict key immutable in nature hence we can't use list,set,dict ad a dict key but we can use number tuple,frozenset as a dict key otherwise we will get TypeError

# dict using list 
# d={[10,20,30]:'alice',40:'Jack',50:'bob'}
# print(d)     ketError 

#dict using tuple 
d={(10,20,30):'alice',40:'Jack',50:'bob'}
print(d)
print()

# dict key using set
# s=set((10,20,30))
# d={s:'alice',40:'bob',50:'jack'}
# print(d)      keyError

# dict key using frozenset
s=set((10,20,30))
d={frozenset(s):'alice',40:'bob',50:'jack'}
print(d)
print()

d={12.5:'alice',40:'bob',50:'jack'}
print(d)
print()

d={10+20:'alice',40:'bob',50:'jack'}
print(d)
print()

d={10+20j:'alice',40:'bob',50:'jack'}
print(d)
print()

d={True:'alice',40:'bob',50:'jack'}
print(d)