# Write a Python program to iterate over a nested dictionary and print all key-value pairs.
nested_dict = {
    "person1": {"name": "John", "age": 25},
    "person2": {"name": "Emily", "age": 30},
    "person3": {"name": "Michael", "age": 35}
}

for person, details in nested_dict.items():
    print("Person:", person)
    for key, value in details.items():
        print(key + ":", value)
    print()
print()
# Write a Python program to find the sum of values in a nested dictionary.
nested_dict = {
    "person1": {"math": 80, "english": 75},
    "person2": {"math": 90, "english": 85},
    "person3": {"math": 95, "english": 88}
}

total_score = 0

for person, scores in nested_dict.items():
    for score in scores.values():
        total_score += score

print("Total score:", total_score)
print()
# Write a Python program to flatten a nested dictionary into a single-level dictionary.
nested_dict = {
    "person1": {"name": "John", "age": 25},
    "person2": {"name": "Emily", "age": 30},
    "person3": {"name": "Michael", "age": 35}
}

flattened_dict = {}

for person, details in nested_dict.items():
    for key, value in details.items():
        flattened_dict[key] = value

print("Flattened dictionary:", flattened_dict)
print()
# Write a Python program to count the occurrence of a specific value in a nested dictionary.
nested_dict = {
    "person1": {"math": 80, "english": 75},
    "person2": {"math": 90, "english": 85},
    "person3": {"math": 95, "english": 88}
}

value_to_count = 75
count = 0

for scores in nested_dict.values():
    if value_to_count in scores.values():
        count += 1

print("Count of", value_to_count, ":", count)