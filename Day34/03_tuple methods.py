# Tuple Methods
# 1. Index()
t = (23, 33, 43, 33, 23, 53, 63) 
print(t.index(33))
print()

# count()
t = (23, 33, 43, 33, 23, 53, 63) 
print(t.count(33))
print()

# len()
t = (23, 33, 43, 33, 23, 53, 63) 
print(len(t))
print()


# min() and max()
t = (23, 33, 43, 33, 23, 53, 63) 
print(min(t))
print(max(t))
print()

#  cmp()
# t1=(10,11)
# t2=(10,1)
# t3=(10,1)
# print(cmp(t1, t2)) # 1
# print(cmp(t2,t1)) #-1
# print(cmp(t2, t3)) # 0y use == != >< symbol for comparison.

# sorted()
l=(12, 11, 34, 23, 21, 45, 1) 
t = sorted(l)
print(t) #[1, 11, 12, 21, 23, 34, 45]
print()

l=(12, 11, 34, 23, 21, 45, 1) 
t = sorted(l, reverse=True) 
print(t) # [45, 34, 23, 21, 12, 11, 1]
