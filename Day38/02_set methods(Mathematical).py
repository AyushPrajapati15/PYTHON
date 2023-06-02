# Union()
a={10,20,30,40,50}
b={11,22,33,44,10,20}
print(a.union(b))
print(a|b)
print()


# intersection()
a={10,20,30,40,50}
b={11,22,33,44,10,20}
print(a.intersection(b))
print(a&b)
print()


# difference()
a={10,20,30,40,50}
b={11,22,33,44,10,20}
print(a.difference(b))
print(a-b)
print()


# symmetric_difference()
a={10,20,30,40,50}
b={11,22,33,44,10,20}
print(a.symmetric_difference(b))
print(a^b)
print()


# subset()
a={1,2,3,4,5,6,7,8,9,}
b={5,6,7}
print(b.issubset(a))
print(a.issubset(b))
print()


# superset
a={1,2,3,4,5,6,7,8,9,}
b={5,6,7}
print(a.issuperset(b))
print(b.issuperset(a))
print()


# disjoint()
a={1,2,3,4,5,6,7,8,9}
b={11,22,33}
print(a.isdisjoint(b))
a={1,2,3,4,5,6,7,8,9}
b={11,22,33,1}
print(a.isdisjoint(b))
