def calculate_average(numbers):
    return sum(numbers) / len(numbers)

avg = calculate_average

# Example usage
my_list = [10, 20, 30, 40, 50]
average = avg(my_list)
print("Average:", average)

#function called convert_to_celsius that takes a temperature in Fahrenheit as input and returns the temperature in Celsius. Create an alias to_celsius for the convert_to_celsius function and use it to convert a given temperature.

def convert_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5 / 9

to_celsius = convert_to_celsius

# Example usage
temperature_fahrenheit = 75
temperature_celsius = to_celsius(temperature_fahrenheit)
print("Temperature in Celsius:", temperature_celsius)
#function called is_even that takes an integer as input and returns True if the number is even, and False otherwise. Create an alias even for the is_even function and use it to check if a given number is even.

def is_even(number):
    return number % 2 == 0

even = is_even

# Example usage
num = 10
is_even_num = even(num)
print("Is even:", is_even_num)
#function called reverse_string that takes a string as input and returns the reverse of the string. Create an alias rev_str for the reverse_string function and use it to reverse a given string.

def reverse_string(string):
    return string[::-1]

rev_str = reverse_string

# Example usage
my_string = "Hello, World!"
reversed_string = rev_str(my_string)
print("Reversed string:", reversed_string)
#function called calculate_power that takes two numbers, base and exponent, as input and returns the result of base raised to the power of exponent. Create an alias power for the calculate_power function and use it to calculate the power of a given base and exponent.
def calculate_power(base, exponent):
    return base ** exponent

power = calculate_power

# Example usage
base = 2
exponent = 3
result = power(base, exponent)
print("Result:", result)