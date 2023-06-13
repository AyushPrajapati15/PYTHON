dict = {
    "Group1": {"person1": {"name": "alice", "age": 25},
               "person2": {"name": "bob", "age": 30}},
    
    "Group2": {"person3": {"name": "mary", "age": 35},
               "person4": {"name": "david", "age": 28}}
}

for i, j in dict.items():
    print("Group:", i)
    total_age = 0
    num_people = 0
    for person, details in j.items():
        total_age += details["age"]
        num_people += 1
    average_age = total_age / num_people
    print("Average Age:", average_age)
    print()