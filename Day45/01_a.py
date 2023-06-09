student_scores = {
    "John": 85,
    "Emily": 92,
    "Michael": 78,
    "Sarah": 95,
    "Daniel": 88
}

for key, value in student_scores.items():
    print("Key:", key)
    print("Value:", value)
    print()
print()

    
# Python program to check if a key exists in a dictionary:
student_scores = {
    "John": 85,
    "Emily": 92,
    "Michael": 78,
    "Sarah": 95,
    "Daniel": 88
}

key = "John"

if key in student_scores:
    print("Key", key, "exists in the dictionary.")
else:
    print("Key", key, "does not exist in the dictionary.")
print()


# Python program to find the maximum and minimum value in a dictionary:
student_scores = {
    "John": 85,
    "Emily": 92,
    "Michael": 78,
    "Sarah": 95,
    "Daniel": 88
}

max_value = max(student_scores.values())
min_value = min(student_scores.values())

print("Maximum value:", max_value)
print("Minimum value:", min_value)
print()


# Python program to count the frequency of elements in a list and store the results in a dictionary:
numbers = [1, 2, 3, 2, 1, 3, 4, 2, 1, 5]
frequency = {}

for element in numbers:
    if element in frequency:
        frequency[element] += 1
    else:
        frequency[element] = 1

print("Element frequencies:", frequency)
# Python program to sort a dictionary by its values:
scores = {"John": 85, "Emily": 92, "Michael": 78, "Sarah": 95, "Daniel": 88}
sorted_scores = dict(sorted(scores.items(), key=lambda item: item[1]))

print("Sorted scores:", sorted_scores)

# Python program to find the common keys between two dictionaries:
dict1 = {"A": 1, "B": 2, "C": 3}
dict2 = {"B": 4, "C": 5, "D": 6}

common_keys = []

for key in dict1:
    if key in dict2:
        common_keys.append(key)

print("Common keys:", common_keys)
# Python program to add a key-value pair to a dictionary:
student_scores = {
    "John": 85,
    "Emily": 92,
    "Michael": 78
}

student_scores["Sarah"] = 95

print("Updated dictionary:", student_scores)
# Python program to remove a key-value pair from a dictionary:
student_scores = {
    "John": 85,
    "Emily": 92,
    "Michael": 78,
    "Sarah": 95
}

del student_scores["Michael"]

print("Updated dictionary:", student_scores)