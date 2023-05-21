# calculate the average of numbers in a given list 
num = [2, 4, 6, 8, 10]
sum = 0
count = 0

for i in num:
    sum += i
    count += 1

average = sum / count
print("Average:", average)
print("")

#  program to remove duplicates from a list
list = [1, 2, 3, 4, 1, 2, 5, 6, 3, 4, 7, 8, 9, 5]
list = set(list)
print(list)

