# Create a nested tuple
nested_tuple = (('a', 'b', 'c'), ('d', 'e', 'f'), ('g', 'h', 'i'))

print(nested_tuple[0][1])  # Output: b

print(nested_tuple[1][2])  # Output: f

print(nested_tuple[2][0])  # Output: g


# Create a nested tuple
nested_tuple = ((1, 2, 3), (4, 5, 6), (7, 8, 9))

nested_tuple[0] = (nested_tuple[0][0], 99, nested_tuple[0][2])

nested_tuple[1] = (nested_tuple[1][0], nested_tuple[1][1], 88)

nested_tuple[2] = (77, nested_tuple[2][1], nested_tuple[2][2])

print(nested_tuple)


# Create a nested tuple
nested_tuple = (('a', 'b', 'c'), ('d', 'a', 'e'), ('f', 'g', 'a'))


# Create two nested tuples
nested_tuple1 = ((1, 2, 3), (4, 5, 6))
nested_tuple2 = (('a', 'b', 'c'), ('d', 'e', 'f'))

# Concatenate the two nested tuples
concatenated_tuple = nested_tuple1 + nested_tuple2

print(concatenated_tuple)

# Create a nested tuple
nested_tuple = ((1, 2, 3), ('a', 'b', 'c'), (4, 5, 6))

if 'b' in nested_tuple:
    print("'b' exists in the nested tuple.")
else:
    print("'b' does not exist in the nested tuple.")

if 7 in nested_tuple:
    print("7 exists in the nested tuple.")
else:
    print("7 does not exist in the nested tuple.")


nested_tuple = ((1, 2, 3), ('a', 'b', 'c'), (4, 5, 6))


for subtuple in nested_tuple:
    for element in subtuple:
        print(element)
