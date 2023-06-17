# Checking starting and ending of string
s="Hello python"

print(s.startswith("hello"))
print(s.startswith("Hello"))
print(s.endswith("Hello"))
print(s.endswith("Hello"))
print()

# Checking what type of char is present in given string
s="Hello python"
print("isalpha ",s.isalpha())
print()

s="Hellopython"
print("isalpha ",s.isalpha())
print()

s="1Hellopython"
print("isalpha ",s.isalpha())
print()

s="1Hellopython"
print("isalnum ",s.isalnum())
print()

s="123"
print("isalnum ",s.isalnum())
print()

s="123"
print("isdigit ",s.isdigit())
print()

s="123"
print("islower ",s.islower())
print()

s="HELLO"
print("isupper ",s.isupper())
print()

s="hello"
print("isupper ",s.isupper())
print()

s="Washington"
print("istitle ",s.istitle())
print()

s="washington"
print("istitle ",s.istitle())
print()

s="     "
print("isspace ",s.isspace())
print()

s="  .   "
print("isspace ",s.isspace())
print()


# Change case
s="Hello python"
print("upper ",s.upper())
print(s)

s="Hello python"
s1=s.upper()
print(s)
print(s1)
print()
print(id(s))
print(id(s1))
print()

s="Hello Python"
print("lower",s.lower())
print(s)
print()

s="Hello Python"
print("swapcase",s.swapcase())
print(s)
print()                    
print()

s="Hello Python"
print("capitalize",s.capitalize())
print(s)
print()                    


# Find out length and count the occurrence

s="Hello Python lang"
print("length",len(s))
print()

s="Hello Python lang"
print("count",s.count("l")) 
print()

s="Hello Python lang"
print("count",s.count("l",12)) 
print()


# Replace of string
s="Hello Python is bad programming language"
print("replace",s.replace("bad","good")) 