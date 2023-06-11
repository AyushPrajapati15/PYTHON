#Nested Dictionary (inner dictionary)
d={1:{'name':'Alce'},2:{'name':'bob'},30:{'name':'jack'},4:{'name':'mary'}}
print(d)

for i in d:
    print(i)

for i in d.values():
    print(i)

for i,j in d.items():
    print(i,j)

print(d[1])

print(d[1]['name'])


d={10:{'name':'alice'},20:{'name':'bob'},30:{40:{50:{60:70}}}}

print(d[30])
print(d[30][40])
print(d[30][40][50])
print(d[30][40][50][60])


d={1:{'name':'surendra'},2:{'name':'priyanka'},30:{40:{50:{60:70}}}}


d[30][40][50][60]=5000
print(d[30][40][50][60])

print(d)


# Write a Python program to iterate over a nested list.
nested_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

for inner_list in nested_list:
    for element in inner_list:
        print(element, end=" ")

    print()


# Write a Python program to access and print values from a nested dictionary.
nested_dict = {
    "person1": {"name": "John", "age": 25, "city": "New York"},
    "person2": {"name": "Emily", "age": 30, "city": "London"},
    "person3": {"name": "Michael", "age": 35, "city": "Paris"}
}

for person, details in nested_dict.items():
    print("Person:", person)
    print("Name:", details["name"])
    print("Age:", details["age"])
    print("City:", details["city"])
    print()


# Write a Python program to count the occurrence of an element in a nested list.
nested_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 2, 3], [4, 5, 6]]

element = 2
count = 0

for inner_list in nested_list:
    count += inner_list.count(element)

print("Count of", element, ":", count)

# Write a Python program to find the maximum value in a nested dictionary.
nested_dict = {
    "person1": {"name": "John", "age": 25, "score": {"math": 80, "english": 75}},
    "person2": {"name": "Emily", "age": 30, "score": {"math": 90, "english": 85}},
    "person3": {"name": "Michael", "age": 35, "score": {"math": 95, "english": 88}}
}

max_score = float("-inf")

for person, details in nested_dict.items():
    math_score = details["score"]["math"]
    max_score = max(max_score, math_score)

print("Maximum math score:", max_score)