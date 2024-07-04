import random

def get_user_choice():
    """Prompts the user to enter a choice: rock, paper, scissors, lizard, or spock."""
    print("Choose your option:")
    print("1. Rock")
    print("2. Paper")
    print("3. Scissors")
    print("4. Lizard")
    print("5. Spock")
    choice_map = {"1": "rock", "2": "paper", "3": "scissors", "4": "lizard", "5": "spock"}
    choice = input("Enter your choice (1-5): ").lower()
    while choice not in choice_map:
        print("Invalid choice. Please enter a number between 1 and 5.")
        choice = input("Enter your choice (1-5): ").lower()
    return choice_map[choice]

def get_computer_choice():
    """Randomly selects a choice for the computer."""
    return random.choice(["rock", "paper", "scissors", "lizard", "spock"])

def determine_winner(user_choice, computer_choice):
    """Determines the winner of the game."""
    winning_combinations = {
        "rock": ["scissors", "lizard"],
        "paper": ["rock", "spock"],
        "scissors": ["paper", "lizard"],
        "lizard": ["spock", "paper"],
        "spock": ["scissors", "rock"]
    }
    if user_choice == computer_choice:
        return "It's a tie!"
    elif computer_choice in winning_combinations[user_choice]:
        return "You win!"
    else:
        return "You lose!"

def play_game():
    """Plays a game of rock, paper, scissors, lizard, spock."""
    user_choice = get_user_choice()
    computer_choice = get_computer_choice()
    print(f"Computer chose: {computer_choice}")
    result = determine_winner(user_choice, computer_choice)
    print(result)

if __name__ == "__main__":
    play_game()