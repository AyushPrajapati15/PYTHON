# Create a set comprehension that contains the lengths of each word in a given sentence.
sentence = "This is a sample sentence"
word_lengths = {len(word) for word in sentence.split()}
print(word_lengths)
print()

# Create a set comprehension that contains the lowercase vowels present in a given string.
string = "Hello, World!"
vowels = {char.lower() for char in string if char.lower() in 'aeiou'}
print(vowels)
print()

# Create a set comprehension that contains the unique even numbers from a given list.
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = {num for num in numbers if num % 2 == 0}
print(even_numbers)
print()

# Create a set comprehension that contains the first letter of each word in a sentence, excluding articles ("a", "an", "the").
sentence = "The quick brown fox jumps over a lazy dog"
first_letters = {word[0] for word in sentence.split() if word.lower() not in ['a', 'an', 'the']}
print(first_letters)
print()

# Create a set comprehension that contains the unique characters present in a given string.
string = "Hello, World!"
unique_characters = {char for char in string}
print(unique_characters)
print()

# Create a set comprehension that contains the common elements between two given lists.
list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]
common_elements = {element for element in list1 if element in list2}
print(common_elements)
print()

# Create a set comprehension that contains the lengths of words starting with a vowel in a given sentence.
sentence = "The quick brown fox jumps over a lazy dog"
vowel_word_lengths = {len(word) for word in sentence.split() if word[0].lower() in 'aeiou'}
print(vowel_word_lengths)
print()


# Create a set comprehension that contains the lowercase consonants present in a given string.
string = "Hello, World!"
consonants = {char.lower() for char in string if char.isalpha() and char.lower() not in 'aeiou'}
print(consonants)
print()

# Create a set comprehension that contains the first letter of each word that starts with a vowel in a given sentence.
sentence = "An apple a day keeps the doctor away"
vowel_starting_letters = {word[0].lower() for word in sentence.split() if word[0].lower() in 'aeiou'}
print(vowel_starting_letters)
print()

# Create a set comprehension that contains the ASCII values of uppercase letters in a given string.
string = "Hello, World!"
ascii_values = {ord(char) for char in string if char.isupper()}
print(ascii_values)