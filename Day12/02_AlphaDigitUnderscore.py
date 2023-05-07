# Program to check whether a character is alphabet, digit, or special character

char = input("Enter any character: ")

if (char >= 'a' and char <= 'z') or (char >= 'A' and char <= 'Z'):
    print(f"{char} is an alphabet")
elif char >= '0' and char <= '9':
    print(f"{char} is a digit")
else:
    print(f"{char} is a special character")
