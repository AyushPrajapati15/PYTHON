# Random module

import random 

#randint() ---> it will generate random int number in between 1 to 10 
val=random.randint(1,10) # both 1 and 10 are included 
print(val)
print()


#random() ---> it will generate a random float number in between o to 1 
val=random.random()
print(val)
print()


# print(dir(random))

# print(help(random.random))

#randrange() - exactly same as randint here stop value not included 

val=random.randrange(1,10) # here 10 is not included 
print(val)
print()

#shuffel() 

#without shuffle
l=[10,20,30,40,50]
print(l)
print()

#without shuffle
l=[10,20,30,40,50]
random.shuffle(l)
print(l)
print()

#uniform() - it will generate float value in between that range
val=random.uniform(10,20)
print(val)

# print(help(random.uniform))

#sample()  - it will generate sample form data
li=['Alice','Bob','mary','Jack','David','Jerry']
val=random.sample(li,3)
print(val)
print()

# print(help(random.sample))

data=random.sample(range(10000000), 60)
print(data)
print()

#choice function 
l=[1,2,3,4,5,6]
val=random.choice(l)
print(val)
print()

l=range(10000)
val=random.choice(l)
print(val)
print()

# Question
l=[10,20,30,40,50,60]
data=random.sample(l,k=True+True*2)
print(len(data))
print()


data=random.uniform(10,20)
print(data)