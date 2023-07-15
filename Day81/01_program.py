from functools import reduce


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)
print()


names = ["Alice", "Bob", "Charlie", "Dave"]
uppercase_names = list(map(lambda x: x.upper(), names))
print(uppercase_names)
print()



numbers = [1, 2, 3, 4, 5]
product = reduce(lambda x, y: x * y, numbers)
print(product)
print()


strings = ["apple", "banana", "carrot", "date", "eggplant"]
filtered_strings = list(filter(lambda x: len(x) > 5, strings))
print(filtered_strings)
print()



numbers = [1, 2, 3, 4, 5]
squared_numbers = list(map(lambda x: x ** 2, numbers))
print(squared_numbers)
print()


strings = ["apple", "banana", "carrot", "date", "eggplant"]
filtered_strings = list(filter(lambda x: x[0].lower() in ['a', 'e', 'i', 'o', 'u'], strings))
print(filtered_strings)
print()



names = ["Alice", "Bob", "David", "Mary"]
concatenated_names = list(reduce(lambda x, y: x + " " + y, names))
print(concatenated_names)
print()


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
divisible_by_3_numbers = list(filter(lambda x: x % 3 == 0, numbers))
print(divisible_by_3_numbers)
print()


strings = ["apple", "banana", "carrot", "date", "eggplant"]
capitalized_strings = list(map(lambda x: x.capitalize(), strings))
print(capitalized_strings)
