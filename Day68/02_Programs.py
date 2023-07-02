# program to calculate the area of a rectangle using local variables for length and width.
def calculate_area():
    length = 5
    width = 3
    area = length * width
    print("Area:", area)

calculate_area()
# program to increment a global variable within a function and print its value.
counter = 0

def increment_counter():
    global counter
    counter += 1
    print("Counter:", counter)

increment_counter()
increment_counter()
# program to demonstrate variable scope by using both local and global variables.
def calculate_area():
    length = 5
    width = 3
    area = length * width
    print("Local Area:", area)

length = 10
width = 8
calculate_area()
area = length * width
print("Global Area:", area)
# program to concatenate a global string variable with a local string variable inside a function and print the result.
name = "John"

def add_surname():
    surname = "Doe"
    full_name = name + " " + surname
    print("Full Name:", full_name)

add_surname()