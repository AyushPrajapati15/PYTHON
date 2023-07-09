def power(b, e):
    if e == 0:
        return 1
    else:
        return b * power(b, e - 1)

base = 2
exponent = 4
result = power(base, exponent)
print(f"{base} raised to the power of {exponent} is: {result}")
print()




def reverse_string(s):
    if len(s) <= 1:
        return s
    else:
        return reverse_string(s[1:]) + s[0]

string = "Hello, World!"
result = reverse_string(string)
print(f"The reverse of '{string}' is: '{result}'")
print()




def count_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    if len(s) == 0:
        return 0
    elif s[0].lower() in vowels:
        return 1 + count_vowels(s[1:])
    else:
        return count_vowels(s[1:])

string = "Hello, World!"
result = count_vowels(string)
print(f"The number of vowels in '{string}' is: {result}")
print()




def count_down(n):
    if n <= 0:
        return
    print(n)
    count_down(n - 1)

number = 5
count_down(number)
print()



def sum_list(nums):
    if len(nums) == 0:
        return 0
    return nums[0] + sum_list(nums[1:])

my_list = [1, 2, 3, 4, 5]
result = sum_list(my_list)
print(f"The sum of the list is: {result}")
