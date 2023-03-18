import random

print("Welcome to Rock, Paper, Scissors!")
print("You will be playing against the computer.")

# Define the possible choices and the outcomes for each
choices = ["rock", "paper", "scissors"]
outcomes = {"rock": {"rock": "tie", "paper": "lose", "scissors": "win"},
            "paper": {"rock": "win", "paper": "tie", "scissors": "lose"},
            "scissors": {"rock": "lose", "paper": "win", "scissors": "tie"}}

# Keep track of the score
user_score = 0
computer_score = 0

# Run the game until the user decides to quit
while True:
    print(f"\nUser score: {user_score}, Computer score: {computer_score}")

    # Get the user's choice
    user_choice = input("\nChoose rock, paper, or scissors (or 'quit' to exit): ").lower()
    if user_choice == "quit":
        break
    elif user_choice not in choices:
        print("Invalid choice, try again.")
        continue

    # Get the computer's choice
    computer_choice = random.choice(choices)

    # Determine the outcome
    outcome = outcomes[user_choice][computer_choice]

    # Print the choices and outcome
    print(f"\nYou chose {user_choice}, computer chose {computer_choice}.")
    if outcome == "win":
        print("You win!")
        user_score += 1
    elif outcome == "lose":
        print("You lose!")
        computer_score += 1
    else:
        print("It's a tie!")
