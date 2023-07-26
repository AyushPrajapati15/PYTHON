import random

first_names = ["John", "Emma", "Michael", "Sophia", "William", "Olivia", "James", "Ava", "Elijah", "Isabella"]
last_names = ["Smith", "Johnson", "Williams", "Brown", "Jones", "Miller", "Davis", "Garcia", "Martinez", "Wilson"]
subjects = ["Math", "Science", "History", "English", "Art", "Computer Science", "Music", "Physics", "Chemistry"]


def generate_student_data():
    first_name = random.choice(first_names)
    last_name = random.choice(last_names)
    age = random.randint(18, 25)
    subject = random.choice(subjects)
    grade = random.randint(60, 100)

    return {
        "First Name": first_name,
        "Last Name": last_name,
        "Age": age,
        "Subject": subject,
        "Grade": grade
    }

for i in range(10):
    student_data = generate_student_data()
    print(f"Student {i+1}:")
    print("Name:", student_data["First Name"], student_data["Last Name"])
    print("Age:", student_data["Age"])
    print("Subject:", student_data["Subject"])
    print("Grade:", student_data["Grade"])
    print()
