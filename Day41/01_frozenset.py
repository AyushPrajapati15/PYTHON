# Frozenset is immutable in nature so we cant use add(), remove() kind of methods why because these will modify frozenset.

# ceatin frozen set from set
s={11,22,33,44,55}
fs=frozenset(s)
print(fs)
print(type(fs))
print()

# ceatin frozen set from list
l=[10,20,30,40,50]
fs=frozenset(l)
print(fs)
print(type(fs))
print()

fs=frozenset(range(10))
print(fs)
print()

# fs=frozenset(range(10))
# fs.add(222)   not posssible in frezenset
# fs.remove(5)

# applying other normal methods which will not modify frozenset
fs1=frozenset([23,33,43,53,63])
fs2=frozenset([11,22,33,44,53])
fs3=frozenset([23,45])
fs3=frozenset([23,45])
fs5=frozenset([99,100])
fs4= fs1.copy()
print(fs4)
print()
print(fs1.union(fs2))
print()
print(fs1.intersection(fs2))
print()
print(fs1.difference(fs2))
print()
print(fs1.symmetric_difference(fs2))
print()
print(fs3.issubset(fs1))
print()
print(fs1.issuperset(fs3))
print()
print(fs5.isdisjoint(fs3))
print()
