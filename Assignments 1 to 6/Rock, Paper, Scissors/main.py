import random

def rock_paper_scissors():
    options = ['rock', 'paper', 'scissors']
    print("Let's play Rock, Paper, Scissors!")

    user_score = 0
    computer_score = 0

    while True:
        user_choice = input("Enter rock, paper, or scissors (or 'q' to quit): ").lower()
        if user_choice == 'q':
            print("Game over!")
            print(f"Your score: {user_score}, Computer score: {computer_score}")
            break

        if user_choice not in options:
            print("Invalid choice, try again!")
            continue

        computer_choice = random.choice(options)
        print(f"Computer chose: {computer_choice}")

        if user_choice == computer_choice:
            print("It's a tie!")
        elif (user_choice == 'rock' and computer_choice == 'scissors') or \
             (user_choice == 'scissors' and computer_choice == 'paper') or \
             (user_choice == 'paper' and computer_choice == 'rock'):
            print("You win! 🎉")
            user_score += 1
        else:
            print("Computer wins!")
            computer_score += 1

# Run the game
rock_paper_scissors()
