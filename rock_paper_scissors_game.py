# ROCK-PAPER-SCISSORS GAME

import random

def determine_result(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "Both chose the same. It's a tie!"
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
        (user_choice == 'scissors' and computer_choice == 'paper') or \
        (user_choice == 'paper' and computer_choice == 'rock'):
        return "You win!"
    else:
        return "You lose!"

def main():
    user_score = 0
    computer_score = 0
    tied_score = 0

    print("      Welcome to Rock-Paper-Scissors!")
    print("Choose between: 'Rock', 'Paper', or 'Scissors'.")
    
    while True:
        user_choice = input("Enter your choice: ").lower()

        if user_choice not in ['rock', 'paper', 'scissors']:
            print("Invalid choice. Please choose again.\n")
            continue

        computer_choice = random.choice(['rock', 'paper', 'scissors'])

        print("\nYou chose: " + user_choice)
        print("Computer chose: " + computer_choice)

        result = determine_result(user_choice, computer_choice)
        print(result)

        if result == "You win!":
            user_score += 1
        elif result == "You lose!":
            computer_score += 1
        elif result == "Both chose the same. It's a tie!":
            tied_score += 1
        else:
            continue

        print("\nScores - You: " + str(user_score), ", Computer: " + str(computer_score), ", Tied score: " + str(tied_score))            

        while True :
            play_again = input("\nDo you want to play again? (yes/no): ").lower()
            if play_again == 'no':
                print("Thank you for playing Rock-Paper-Scissors!\n")
                exit()
            elif play_again == 'yes':
                print("\nLet's play again!")
                break
            else:
                print("Invalid Input. Please enter 'Yes' or 'No'. ")           

if __name__ == "__main__":
    main()
