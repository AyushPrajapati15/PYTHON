# Sum Of Digits using class

class SumOfDigits:
    def __init__(self, number):
        self.number = number

    def get_digits(self):
        return [int(digit) for digit in str(self.number)]

    def calculate_sum(self):
        digits = self.get_digits()
        return sum(digits)



number = 12345
sum_of_digits_obj = SumOfDigits(number)
result = sum_of_digits_obj.calculate_sum()
print(f"The sum of digits of {number} is: {result}")
