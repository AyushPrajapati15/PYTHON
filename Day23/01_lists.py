# lists
l = [10, 20, 30, 'Alice', 'Bob', 5.5]
print(l)
print(l[3])
print(l[-4])

# Empty lists
# l=[]
# print(l)

# creation of lists Dynamically using eval() function

l = eval(input("Enter a lists"))
print(l)

#  creation of lists using list()

l = list((20, 50, 40, 60))
print(l)

#  creation of lists using range()
l = list(range(10, 21))
print(l)

# NOTE := "List can hold any complex datatype like dictionary,tuple,etc"

l = [10, {"name": "Alice"}, list((20, 30, 40))]
print(l)

#  creation of lists using split()

msg = "Welcome to python"
l = msg.split()
print(l)

msg = "He-llo- Wel-come t-o py-thon"
l = msg.split('-')
print(l)

# insertion and deletion is possible in list
l = [10, 20, 30, 40, 50]
del (l[2])
print(l)

# Accessing elements of lists :-
#  Accessing using slce operator
l = [23, 33, 43, 53, 63]
print(l[::])
print(l[2::2])
