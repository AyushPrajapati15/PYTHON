# Rock paper scissor game
import random

def get_user_choice():
    user_choice = input("Enter your choice (Rock/Paper/Scissors): ").lower()
    while user_choice not in ['rock', 'paper', 'scissors']:
        print("Invalid choice. Please try again.")
        user_choice = input("Enter your choice (Rock/Paper/Scissors): ").lower()
    return user_choice


def get_computer_choice():
    return random.choice(['rock', 'paper', 'scissors'])


def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif user_choice == 'rock':
        return "You win!" if computer_choice == 'scissors' else "Computer wins!"
    elif user_choice == 'paper':
        return "You win!" if computer_choice == 'rock' else "Computer wins!"
    elif user_choice == 'scissors':
        return "You win!" if computer_choice == 'paper' else "Computer wins!"

def play_again():
    return input("Do you want to play again? (yes/no): ").lower() == 'yes'

def main():
    print("Welcome to Rock, Paper, Scissors!")

    while True:
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()

        print(f"Your choice: {user_choice}")
        print(f"Computer's choice: {computer_choice}")

        result = determine_winner(user_choice, computer_choice)
        print(result)

        if not play_again():
            break

if __name__ == "__main__":
    main()
