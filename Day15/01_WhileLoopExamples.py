# Count vowel
string = input("Enter a string: ")
vowels = ['a', 'e', 'i', 'o', 'u']
count = 0
i = 0

while i < len(string):
    if string[i].lower() in vowels:
        count += 1
    i += 1

print("Number of vowels in the string is:", count)


#  program to input a string from the user and reverse the string using a while loop
string = input("Enter a string: ")
reverse_string = ""
i = len(string) - 1

while i >= 0:
    reverse_string += string[i]
    i -= 1

print("Reverse of the string is:", reverse_string)

#  program to generate a Fibonacci sequence up to a given number using a while loop.
num = int(input("Enter a positive integer: "))
a, b = 0, 1

while a <= num:
    print(a, end=' ')
    a, b = b, a + b
