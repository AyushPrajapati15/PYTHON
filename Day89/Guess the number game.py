# Guess the number Game

import random

rn=random.randint(1,10)

count=0

while(True):

    choice=int(input("Guess a number in between 1 - 10 \n"))
    
    print()

    count=count+1

    if choice==rn:
        print(f"Congrats! you guess the correct number in {count} times")
        print()
        break
    elif choice>rn:
        print("Sry! your gues number is greater than the number")
        print()
    else:
        print("Sry! your gues number is less than the number")
        print()

