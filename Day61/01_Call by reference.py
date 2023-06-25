# Write a Python program to swap two elements in a list using call by reference.
def swap_elements(arr, index1, index2):
    arr[index1], arr[index2] = arr[index2], arr[index1]

my_list = [1, 2, 3, 4, 5]
print("Before swap:", my_list)
swap_elements(my_list, 1, 3)
print("After swap:", my_list)

# Write a Python program to modify the values of a dictionary using call by reference.
def modify_dictionary(data):
    data["name"] = "John"
    data["age"] = 30

person = {"name": "Alice", "age": 25}
print("Before modification:", person)
modify_dictionary(person)
print("After modification:", person)

# Write a Python program to append elements to a list using call by reference.
def append_to_list(my_list, new_elements):
    my_list.extend(new_elements)

numbers = [1, 2, 3]
print("Before appending:", numbers)
append_to_list(numbers, [4, 5, 6])
print("After appending:", numbers)

# Write a Python program to update a dictionary using call by reference.
def update_dictionary(data, new_data):
    data.update(new_data)

person = {"name": "Alice", "age": 25}
print("Before updating:", person)
update_dictionary(person, {"city": "New York", "occupation": "Engineer"})
print("After updating:", person)

# Write a Python program to clear a list using call by reference.
def clear_list(my_list):
    my_list.clear()

numbers = [1, 2, 3, 4, 5]
print("Before clearing:", numbers)
clear_list(numbers)
print("After clearing:", numbers)

# Write a Python program to reverse a string using call by reference.
def reverse_string(text):
    text.reverse()

message = list("Hello")
print("Before reversing:", "".join(message))
reverse_string(message)
print("After reversing:", "".join(message))