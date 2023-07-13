# add 4 to each and every element present in list without using lambda 
#craete the body for add4 function 
def add4(x):
    return x+4
l=[10,20,30,40,50]
data=list(map(add4,l))
print(data)
 

# add 4 to each and every element present in list with using lambda 
l=[100,200,300,400,500]
data=list(map(lambda x:x+4,l))
print(data)


#find out square of ecah number preset inside tuple 
t=(1,2,3,4,5,6)
data1=tuple(map(lambda x:x*x,t))
data=list(map(lambda x:x*x,t))
print(data)
print(data1)


#add individual elemenet of both list
l1=[10,20,30,40,50]
l2=[11,12,13,14,15]
data=list(map(lambda x,y:x+y,l1,l2))
print(data)


l1=[10,20,30,40,50]
l2=[11,12,13,14,15]
l3=[111,112,113,114,115]
data=list(map(lambda x,y,z:x+y+z,l1,l2,l3))
print(data)


#find the length of each words preset in a list 
names=['Alice','Bob','Jack','Marry']
data=list(map(lambda x:len(x),names))
print(data)


names=['Alice','Bob','Jack','zini']
data=map(lambda x:len(x),names)


# print(type(data))
for i in data:
    print(i)

    
# find out the length of each words preset in a string 
msg='hello everyone welcome to python'
s=msg.split(' ')
print(s)
