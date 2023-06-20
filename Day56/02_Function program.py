# Calculate the Factorial of a Number
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

number = int(input("Enter a number: "))
result = factorial(number)
print("Factorial of", number, "is", result)



# Check if a Number is Prime
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

number = int(input("Enter a number: "))
if is_prime(number):
    print(number, "is prime.")
else:
    print(number, "is not prime.")


# Program 3: Reverse a String
def reverse_string(string):
    return string[::-1]

input_string = input("Enter a string: ")
reversed_string = reverse_string(input_string)
print("Reversed string:", reversed_string)

# Program 4: Calculate the Sum of Digits in a Number
def sum_of_digits(n):
    total = 0
    while n > 0:
        digit = n % 10
        total += digit
        n //= 10
    return total

number = int(input("Enter a number: "))
result = sum_of_digits(number)
print("Sum of digits in", number, "is", result)