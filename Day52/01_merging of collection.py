# list merging
l=[10,20,30,40,50]
s=[100,'alice',200]
b=l+s
b2=[*l,*s]
print(b)
print(b2)
print()


# tuple merging
t=(10,20,30,40,50)
p=(100,'alice',200)
b=t+p
b=(*t,*p)
print(b)
print(b2)
print()


# Set merging
s1={10,20,30,40,50}
s2={100,'alice',200}
# s=s1+s2 --> this will not work
s={*s1,*s2}
print(s)
print()


# dictionary merging
d1={1:'Alice',2:'Bob'}
d2={3:'Jack',4:'jerry'}
d={*d1,*d2} # it will only print key for values we wllhave to use double star(**) 
print(d)
d={**d1,**d2}
print(d)
print()

dict1 = {'a': 1, 'b': 2}
dict2 = {'c': 3, 'd': 4}
dict1.update(dict2)
print(dict1)