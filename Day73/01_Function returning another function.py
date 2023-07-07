# Function returning another function

def multiply_by(n):
    def multiplier(x):
        return x * n
    return multiplier

multiplier_2 = multiply_by(2)
result = multiplier_2(5)
print(result)
print()


def get_math_operation(operation):
    if operation == 'add':
        return lambda x, y: x + y
    elif operation == 'subtract':
        return lambda x, y: x - y
    elif operation == 'multiply':
        return lambda x, y: x * y
    elif operation == 'divide':
        return lambda x, y: x / y

addition = get_math_operation('add')
result = addition(5, 3)
print(result)

multiplication = get_math_operation('multiply')
result = multiplication(4, 2)
print(result)
print()


def apply_discount(percent):
    def discount(price):
        return price - (price * percent / 100)
    return discount

ten_percent_discount = apply_discount(10)
final_price = ten_percent_discount(100)
print(final_price)
print()


def power_of(n):
    def power(x):
        return x ** n
    return power

square = power_of(2)
result = square(5)
print(result)

cube = power_of(3)
result = cube(2)
print(result)
print()


def create_incrementor(n):
    def incrementor(x):
        return x + n
    return incrementor


increment_by_3 = create_incrementor(3)
result = increment_by_3(5)
print(result)