# Nested dictionary
student_data = {
    'student1': {
        'name': 'John',
        'age': 18,
        'grade': 'A'
    },
    'student2': {
        'name': 'Emily',
        'age': 17,
        'grade': 'B'
    },
    'student3': {
        'name': 'Sam',
        'age': 16,
        'grade': 'A'
    }
}
print()

# Dictionary comprehension to create a new dictionary with the names of students as keys
# and their grades as values
grades_dict = {student_data[student]['name']: student_data[student]['grade'] for student in student_data}

# Print the new dictionary
print(grades_dict)
print()


# Nested dictionary
employee_data = {
    'employee1': {
        'name': 'John',
        'age': 30,
        'department': 'Sales',
        'salary': 5000
    },
    'employee2': {
        'name': 'Emily',
        'age': 28,
        'department': 'Marketing',
        'salary': 6000
    },
    'employee3': {
        'name': 'Sam',
        'age': 35,
        'department': 'Finance',
        'salary': 7000
    }
}
print()

# Dictionary comprehension to create a new dictionary with the names of employees as keys
# and their departments as values, for employees with age greater than 30
selected_employees = {employee_data[emp]['name']: employee_data[emp]['department']
                      for emp in employee_data if employee_data[emp]['age'] > 30}

# Print the new dictionary
print(selected_employees)
