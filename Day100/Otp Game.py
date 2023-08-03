# OTP verification process
import random

def generate_otp():
    return str(random.randint(1000, 9999))

def otp_verification_game():
    print()
    print("Welcome to Math Quiz with OTP Verification!")
    otp = generate_otp()
    attempts = 3

    print("An OTP has been sent to your registered email.")
    print("Hey! aayushprajapati@gmail.com your one time password is given below please donot share it with anyone:- ",otp)
    print("You have 3 attempts to enter the correct OTP.")

    while attempts > 0:
        user_input = input("Enter the OTP: ")

        if user_input == otp:
            print("OTP is correct. Access granted!\n")

            num1 = random.randint(1, 20)
            num2 = random.randint(1, 20)
            correct_answer = num1 ** num2

            print(f"What is the result of {num1} ** {num2}?")
            user_answer = int(input("Your answer: "))

            if user_answer == correct_answer:
                print("Correct! You are a math whiz!")
            else:
                print(f"Oops! Incorrect. The correct answer is {correct_answer}.")

            break
        else:
            attempts -= 1
            if attempts > 0:
                print(f"Wrong OTP. You have {attempts} attempts left.")
            else:
                print("Sorry, you've run out of attempts. Access denied.")

otp_verification_game()
