# Object oriented programming 
class student:
    def __init__(self,name,age,id):
        self.name=name
        self.age=age
        self.id=id


    def getdetails(self):
        print(f"Name is {self.name}")
        print(f"Age is {self.age}")
        print(f"Id is {self.id}")


s1=student("Alice",25,101)
s1.getdetails()


s2=student("Bob",27,102)
s2.getdetails