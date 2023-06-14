# Dictionary Comprehensions

d={i for i in range(1,6)}
print(d)
print(type(d))


d={i:i for i in range(1,6)}
print(d)
print(type(d))

d={i:i*i for i in range(1,6)}
print(d)
print(type(d))

d={i:i*i for i in range(1,6)}
print(d)
print(type(d))

# working with list to create dict 

l=[2.3,4.2,5.6,7.8]
d={r:3.14*r*r for r in l}
print(d)


names=['alice','bob','jack','mary']
d={i:len(i) for i in names}
print(d)

names=['alice','bob','jack','mary']
d={i:len(i) for i in names if len(i)>6}
print(d)



numbers = [1, 2, 3, 4, 5]
squared_dict = {num: num**2 for num in numbers}
print(squared_dict)

# Question: Create a dictionary comprehension to map each character in a string to its ASCII value.
word = "hello"
ascii_dict = {char: ord(char) for char in word}
print(ascii_dict)

# Question: Create a dictionary comprehension to count the frequency of elements in a list.
fruits = ['apple', 'banana', 'cherry', 'apple', 'banana', 'apple']
frequency_dict = {fruit: fruits.count(fruit) for fruit in fruits}
print(frequency_dict)
{'apple': 3, 'banana': 2, 'cherry': 1}

# Question: Create a dictionary comprehension to filter out elements from a list that satisfy a certain condition.
numbers = [1, 2, 3, 4, 5]
even_dict = {num: num**2 for num in numbers if num % 2 == 0}
print(even_dict)