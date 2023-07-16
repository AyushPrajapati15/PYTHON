# largest in list
def max_min(lst):
    if len(lst) == 1:
        return lst[0], lst[0]  
    
    else:
        max_value = lst[0]
        min_value = lst[0]


        max_rest, min_rest = max_min(lst[1:])
        
        if max_rest > max_value:
            max_value = max_rest
        
        if min_rest < min_value:
            min_value = min_rest
        
        return max_value, min_value


# palindrome string
my_list = [7, 2, 9, 1, 5]
max_val, min_val = max_min(my_list)

print("Maximum element:", max_val)
print("Minimum element:", min_val)



def is_palindrome(string):
    
    if len(string) <= 1:
        return True
    
    
    if string[0] == string[-1]:
        
        return is_palindrome(string[1:-1])
    
    return False

print(is_palindrome("racecar"))  
print(is_palindrome("hello"))    
print(is_palindrome("madam"))    
