# self variable

#create a class Student having 3 attributes and 1 methods 

     
class Student:
    def __init__(self):
        self.name=input("Enter Your Name : ")
        self.age=int(input("Enter Your Age : "))
        self.course=input("Enter Your Course: ")
        
    def printDetails(self):
        print('-'*30)
        print(f'Name is {self.name}')
        print(f'Age is {self.age}')
        print(f'Course is {self.course}')
        

s1=Student()

s2=Student()

s3=Student()

s2.printDetails()
s1.printDetails()
s3.printDetails()
print()

# here self and s1 pointing to same memory location
class Student:
    def __init__(self):
        print(id(self))
        
s1=Student()
print(id(s1))
print()

class Student:
    def __init__(self):
        print(id(self))
        
s1=Student()
print(id(s1))

print("-"*20)
        
s2=Student()
print(id(s2))
print()

#self is not a keyword 

class Student:
    def __init__(x):
        x.name=input("Enter Your Name : ")
        x.age=int(input("Enter Your Age : "))
        x.course=input("Enter Your Course: ")
        
    def printDetails(x):
        print('-'*30)
        print(f'Name is {x.name}')
        print(f'Age is {x.age}')
        print(f'Course is {x.course}')
        

s1=Student()
s1.printDetails()
print()

# class Student:
#     def __init__(name,age,course):
#         x.name=name
#         x.age=age
#         x.course=course
        
#     def printDetails(x):
#         print('-'*30)
#         print(f'Name is {x.name}')
#         print(f'Age is {x.age}')
#         print(f'Course is {x.course}')
        

# s1=Student('Priynka',24,"Mtech")
# s1.printDetails()

#here name is acting as self
class Student:
    def __init__(name,age,course):
        name.age=age
        name.course=course
        
    def printDetails(name):
        print('-'*30)
        print(f'Age is {name.age}')
        print(f'Course is {name.course}')
        

s1=Student(24,"Mtech")
s1.printDetails()
