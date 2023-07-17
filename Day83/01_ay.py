# Calculator program
def shape_calculator():
    def calculate_rectangle(length, width):
        area = length * width
        perimeter = 2 * (length + width)
        return area, perimeter

    def calculate_square(side):
        area = side * side
        perimeter = 4 * side
        return area, perimeter

    def calculate_circle(radius):
        import math
        area = math.pi * radius * radius
        circumference = 2 * math.pi * radius
        return area, circumference

    def menu():
        while True:
            print("\n--- Shape Calculator ---")
            print("1. Calculate Rectangle")
            print("2. Calculate Square")
            print("3. Calculate Circle")
            print("4. Exit")

            choice = input("Enter your choice: ")

            if choice == "1":
                length = float(input("Enter length: "))
                width = float(input("Enter width: "))
                area, perimeter = calculate_rectangle(length, width)
                print(f"Rectangle: Area = {area}, Perimeter = {perimeter}")
            elif choice == "2":
                side = float(input("Enter side length: "))
                area, perimeter = calculate_square(side)
                print(f"Square: Area = {area}, Perimeter = {perimeter}")
            elif choice == "3":
                radius = float(input("Enter radius: "))
                area, circumference = calculate_circle(radius)
                print(f"Circle: Area = {area}, Circumference = {circumference}")
            elif choice == "4":
                print("Exiting the program.")
                break
            else:
                print("Invalid choice. Please try again.")

    menu()


shape_calculator()
