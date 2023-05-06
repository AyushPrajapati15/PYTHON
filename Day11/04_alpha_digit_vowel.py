# Program to check whether a character is uppercase or lowercase alphabet

char = input("Enter a character: ")


if char.isalpha():
    if char.islower():
        print(char, "is a lowercase alphabet")
    else:
        print(char, "is an uppercase alphabet")
else:
    print(char, "is not an alphabet")
