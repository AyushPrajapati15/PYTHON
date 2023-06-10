Write a Python program to check if a key exists in a dictionary.
python
Copy code
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

student_scores = {
    "John": 85,
    "Emily": 92,
    "Michael": 78
}

student_scores["Sarah"] = 95

print("Updated dictionary:", student_scores)



# Write a Python program to remove a key-value pair from a dictionary.
student_scores = {
    "John": 85,
    "Emily": 92,
    "Michael": 78,
    "Sarah": 95
}

del student_scores["Michael"]

print("Updated dictionary:", student_scores)


# Write a Python program to iterate over the keys and values of a dictionary.
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
# Write a Python program to find the maximum and minimum value in a dictionary.
student_scores = {
    "John": 85,
    "Emily": 92,
    "Michael": 78,
    "Sarah": 95,
    "Daniel": 88
}

max_score = max(student_scores.values())
min_score = min(student_scores.values())

print("Maximum score:", max_score)
print("Minimum score:", min_score)