# Write a Python program to swap two variables using object references.
def swap_variables(a, b):
    a, b = b, a

x = 10
y = 20
print("Before swapping:", x, y)
swap_variables(x, y)
print("After swapping:", x, y)


# Write a Python program to concatenate two strings using object references.
def concatenate_strings(s1, s2):
    s1 += s2

str1 = "Hello, "
str2 = "World!"
print("Before concatenation:", str1, str2)
concatenate_strings(str1, str2)
print("After concatenation:", str1, str2)

# Write a Python program to modify a list element using object references.
def modify_list_element(my_list):
    my_list[0] = "Modified"

items = ["Apple", "Banana", "Orange"]
print("Before modification:", items)
modify_list_element(items)
print("After modification:", items)

# Write a Python program to modify a dictionary value using object references.
def modify_dictionary_value(data):
    data["name"] = "John"

person = {"name": "Alice", "age": 25}
print("Before modification:", person)
modify_dictionary_value(person)
print("After modification:", person)

# Write a Python program to modify a class attribute using object references.
class Car:
    max_speed = 200

def modify_max_speed(car):
    car.max_speed = 250

my_car = Car()
print("Before modification:", my_car.max_speed)
modify_max_speed(my_car)
print("After modification:", my_car.max_speed)