# Palindrome nmber using class
class Palindrome:
    def __init__(self, number):
        self.number = number

    def is_palindrome(self):
        num_str = str(self.number)
        reversed_num_str = num_str[::-1]
        return num_str == reversed_num_str


number = 121
palindrome_obj = Palindrome(number)
if palindrome_obj.is_palindrome():
    print(f"{number} is a palindrome number.")
else:
    print(f"{number} is not a palindrome number.")
