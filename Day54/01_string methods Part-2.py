# list methods part 2
# Splitting of string
# split()

s = 'Alice  doe'
print(s.split())
print()

s = 'Alice  doe'
print(s.split('a'))
print()

s = 'Alice  doe'
print(s.split('u'))
print()

s = 'Alice doe'
print(s.split('u'))
print()

dob = '15-1-2001'
print(dob.split('-'))
print()


dob = '15-1-2001'
print(dob.split('*'))
print()

# Joining of string
# join()
l = ['Alice', 'Bob', 'Jack', 'Mary']
s = '+'.join(l)
print(s)
print()


l = ['Alice', 'Bob', 'Jack', 'Mary']
s = '*'.join(l)
print(s)
print()


l = ['Alice', 'Bob', 'Jack', 'Mary']
s = ''.join(l)
print(s)
print()


l = ['Alice', 'Bob', 'Jack', 'Mary']
s = ' '.join(l)
print(s)
print()


l = ('Alice', 'Bob', 'Jack', 'Mary')
s = '.'.join(l)
print(s)
print()


# removing space from the string
# rstrip()
s = 'Alice       '
print(len(s))
print(len(s.rstrip()))
print()


#lstrip()
s = '       Alice       '
print(len(s))
print(len(s.rstrip()))
print()


# strip()
s = '       Alice       '
print(len(s))
print(len(s.strip()))
print()


# fill char
# zfill()
s = 'Alice'
print(s.zfill(15))
print()


s = 'Alice'
print(s.zfill(50))
print()


s = 'Alice'
print(s.zfill(9))
print()


# rjust()
s = 'hello'
print(s.rjust(10))
print()


s = 'Alice'
print(s.rjust(50))
print()


s = 'Alice'
print(s.rjust(10, '*'))
print()


# ljust()
s = 'Alice'
print(s.ljust(10, '*'))
print()


# center()
s = 'Alice'
print(s.center(20))
print()


s = 'Alice'
print(s.center(20, '*'))
print()


s = 'Alice'
print(s.center(21, '*'))
print()


# others
# min()
s = 'Alice'
print(min(s))
print()

s = 'Alice'
print(max(s))
print()


s = 'Alice'
print(sorted(s))
print()


s = 'Alice'
print(sorted(s,reverse=True))
print()


# isidentifier()
s = '123abc'
print(s.isidentifier())
print()


s = 'abc123'
print(s.isidentifier())
print()


s = 'True'
print(s.isidentifier())
print()


s = '***abc'
print(s.isidentifier())
print()

s = 'Alice'
for i in enumerate(s):
    print(i)
print()


s = 'Alice'
for i, j in enumerate(s):
    print(i, j)
    print()