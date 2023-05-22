password = input("Set a password ")
attempts = 3

while attempts > 0:
    user_input = input("Enter the password: ")
    
    if user_input == password:
        print("Access granted!")
        break
    
    attempts -= 1
    if attempts > 0:
        print("Incorrect password. Try again.")
    else:
        print("Access denied.")
else:
    print("Access denied.")
