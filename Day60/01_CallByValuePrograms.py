def update_value(num):
    num = num + 10
    print("Inside the function:", num)

value = 20
print("Before the function call:", value)
update_value(value)
print("After the function call:", value)


# Write a Python program to demonstrate call by value for mutable data types.
def update_list(my_list):
    my_list.append(4)
    print("Inside the function:", my_list)

my_list = [1, 2, 3]
print("Before the function call:", my_list)
update_list(my_list)
print("After the function call:", my_list)


# Write a Python program to swap two numbers using call by value.
def swap_numbers(a, b):
    temp = a
    a = b
    b = temp
    print("Inside the function: a =", a, "b =", b)

num1 = 10
num2 = 20
print("Before the function call: num1 =", num1, "num2 =", num2)
swap_numbers(num1, num2)
print("After the function call: num1 =", num1, "num2 =", num2)


# Write a Python program to modify a list inside a function using call by value.
def modify_list(my_list):
    my_list.append(4)
    my_list = [1, 2, 3]
    print("Inside the function:", my_list)

my_list = [10, 20, 30]
print("Before the function call:", my_list)
modify_list(my_list)
print("After the function call:", my_list)


# Write a Python program to demonstrate call by value for string data type.
def modify_string(text):
    text += " World"
    print("Inside the function:", text)

message = "Hello"
print("Before the function call:", message)
modify_string(message)
print("After the function call:", message)


# Write a Python program to pass a dictionary to a function and modify its values.
def modify_dict(data):
    data["name"] = "John"
    data["age"] = 30
    print("Inside the function:", data)

person = {"name": "Alice", "age": 25}
print("Before the function call:", person)
modify_dict(person)
print("After the function call:", person)


# Write a Python program to pass a list to a function and modify its elements.
def modify_list_elements(my_list):
    for i in range(len(my_list)):
        my_list[i] += 10
    print("Inside the function:", my_list)

numbers = [1, 2, 3, 4, 5]
print("Before the function call:", numbers)
modify_list_elements(numbers)
print("After the function call:", numbers)


# Write a Python program to demonstrate call by value for tuple data type.
def modify_tuple(my_tuple):
    my_tuple += (4, 5)
    print("Inside the function:", my_tuple)

numbers = (1, 2, 3)
print("Before the function call:", numbers)
modify_tuple(numbers)
print("After the function call:", numbers)