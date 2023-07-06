def outer_function(num):
    def inner_function():
        return num ** 2

    return inner_function()

result = outer_function(5)
print(result)  # Output: 25
print()



def outer_function(x, y):
    def inner_function():
        return (x + y) ** 2

    return inner_function()

result = outer_function(3, 4)
print(result)  # Output: 49
print()



def outer_function(numbers):
    def inner_function():
        return sum(numbers)

    return inner_function()

result = outer_function([1, 2, 3, 4, 5])
print(result)  # Output: 15
print()



def outer_function(string):
    def inner_function():
        vowels = ['a', 'e', 'i', 'o', 'u']
        count = 0
        for char in string.lower():
            if char in vowels:
                count += 1
        return count

    return inner_function()

result = outer_function("Hello World")
print(result)  # Output: 3
print()



def outer_function(strings):
    def inner_function():
        return [string == string[::-1] for string in strings]

    return inner_function()

result = outer_function(["madam", "hello", "level", "world"])
print(result)  # Output: [True, False, True, False]
