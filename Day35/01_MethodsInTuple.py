original_tuple = (1, 2, 3, 4, 5)
reversed_tuple = tuple(reversed(original_tuple))
print(reversed_tuple)


my_tuple = ('apple', 'banana', 'cherry', 'apple', 'orange')
element = 'apple'
index = my_tuple.index(element)
print(f"The index of '{element}' is: {index}")


my_tuple = ('H', 'e', 'l', 'l', 'o')
string = ''.join(my_tuple)
print(string)


my_tuple = (1, 2, 3, 4, 5)
length = len(my_tuple)
print(f"The length of the tuple is: {length}")


tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)
concatenated_tuple = tuple1 + tuple2
print(concatenated_tuple)


my_tuple = (1, 2, 3, 4, 5)
sliced_tuple = my_tuple[1:4]
print(sliced_tuple)

my_tuple = ('apple', 'banana', 'cherry', 'apple', 'orange')
element = 'apple'
count = my_tuple.count(element)
print(f"The count of '{element}' is: {count}")

my_tuple = (1, 1, 1, 1)
are_all_same = len(set(my_tuple)) == 1
print(are_all_same)

my_tuple = (5, 9, 3, 1, 7)
maximum = max(my_tuple)
minimum = min(my_tuple)
print(f"Maximum: {maximum}, Minimum: {minimum}")

my_tuple = (1, 2, 3, 4, 5)
element = 3
new_tuple = tuple(filter(lambda x: x != element, my_tuple))
print(new_tuple)

