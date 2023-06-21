# Write a Python function to check if a given string is a palindrome:
def is_palindrome(string):
    reversed_string = string[::-1]
    if string.lower() == reversed_string.lower():
        return True
    else:
        return False

print(is_palindrome("level"))  # Output: True
print(is_palindrome("python"))  # Output: False


# Write a Python function to find the maximum element in a list:
def find_max_element(lst):
    if len(lst) == 0:
        return None
    else:
        max_element = lst[0]
        for element in lst:
            if element > max_element:
                max_element = element
        return max_element
print(find_max_element([2, 5, 1, 9, 4]))  # Output: 9
print(find_max_element([10, 3, 8, 6]))  # Output: 10


# Write a Python function to count the occurrence of a specific element in a list:
def count_occurrence(lst, element):
    count = 0
    for item in lst:
        if item == element:
            count += 1
    return count
print(count_occurrence([1, 2, 3, 4, 2, 2], 2))  # Output: 3
print(count_occurrence(["apple", "banana", "apple", "orange"], "apple"))  # Output: 2


# Write a Python function to calculate the area of a circle given its radius:
import math

def calculate_circle_area(radius):
    area = math.pi * radius**2
    return area

# Test the function
print(calculate_circle_area(5))  # Output: 78.53981633974483
print(calculate_circle_area(2.5))  # Output: 19.634954084936208



# Write a Python function to find the sum of all elements in a list.
def find_sum(lst):
    sum = 0
    for num in lst:
        sum += num
    return sum

# Test the function
print(find_sum([1, 2, 3, 4, 5]))  # Output: 15
print(find_sum([-1, 0, 1]))  # Output: 0


