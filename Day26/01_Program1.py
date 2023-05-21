# calculate the average of numbers in a given list 
numbers = [2, 4, 6, 8, 10]
sum_of_numbers = 0
count = 0

for num in numbers:
    sum_of_numbers += num
    count += 1

average = sum_of_numbers / count
print("Average:", average)



#  program to remove duplicates from a list
my_list = [1, 2, 3, 4, 1, 2, 5, 6, 3, 4, 7, 8, 9, 5]
my_list = list(set(my_list))
print(my_list)

