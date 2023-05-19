#  sum of all the elements.

numbers = [5, 9, 2, 10, 3]

sum = 0

for num in numbers:
    sum += num

print("The sum of the list elements is:", sum)


#  remove all the even numbers from the list.
numbers = [5, 9, 2, 10, 3]

# Using list comprehension
numbers = [num for num in numbers if num % 2 != 0]

print("List after removing even numbers:", numbers)


list1 = [1, 3, 5]
list2 = [2, 4, 6]

merged_list = sorted(list1 + list2)

print("Merged and sorted list:", merged_list)


# while loop traversing
numbers = [1, 2, 3, 4, 5]

index = 0
while index < len(numbers):
    print(numbers[index])
    index += 1
