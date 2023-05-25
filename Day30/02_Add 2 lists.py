# Addition of two lists of same size
list1 = [1, 2, 3, 4, 5]
list2 = [6, 7, 8, 9, 10]

if len(list1) == len(list2):
    sum_list = []

    for i in range(len(list1)):
        sum_list.append(list1[i] + list2[i])

    print("Sum list:", sum_list)


else:
    print("Error: Lists are not of the same size")

