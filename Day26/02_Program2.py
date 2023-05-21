# program to find the maximum element in a list 
list = [5, 2, 8, 1, 9, 3, 7]

maximum = float('-inf')

for i in list:
    if i > maximum:
        maximum = i

print("Maximum element:", maximum)


# program to find the minimum element in a list 
list = [5, 2, 8, 1, 9, 3, 7]

minimum = float('inf')

for i in list:
    if i < minimum:
        minimum = i

print("Minimum element:", minimum)
