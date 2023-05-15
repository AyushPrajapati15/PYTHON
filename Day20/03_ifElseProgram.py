side1 = float(input("Enter the length of the first side: "))

side2 = float(input("Enter the length of the second side: "))

side3 = float(input("Enter the length of the third side: "))

if side1 == side2 == side3:
    print("Triangle is equilateral.")

elif side1 == side2 or side2 == side3 or side3 == side1:
    print("Triangle is isosceles.")
    
else:
    print("Triangle is scalene.")
