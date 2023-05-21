# program to count the occurrence of each element in a list 
my_list = [1, 2, 1, 3, 4, 2, 1, 3, 4, 5, 1]
count_dict = {}
for element in my_list:
    if element in count_dict:
        count_dict[element] += 1
    else:
        count_dict[element] = 1

for element, count in count_dict.items():
    print(f"{element}: {count}")




# prog to find the second smallest element in a list.
my_list = [5, 2, 8, 1, 9, 3, 7]
smallest = float('inf')
second_smallest = float('inf')
for num in my_list:
    if num < smallest:
        second_smallest = smallest
        smallest = num
    elif num < second_smallest and num != smallest:
        second_smallest = num

print("Second smallest element:", second_smallest)



# program to find the maximum element in a list 
my_list = [5, 2, 8, 1, 9, 3, 7]

maximum = float('-inf')

for num in my_list:
    if num > maximum:
        maximum = num

print("Maximum element:", maximum)

