from flask import Flask, request, jsonify
import random

app = Flask(__name__)

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

@app.route('/game', methods=['POST'])
def play_game_api():
    data = request.json
    user_choice = data.get('choice')
    if user_choice not in ["rock", "paper", "scissors", "lizard", "spock"]:
        return jsonify({"error": "Invalid choice"}), 400
    computer_choice = get_computer_choice()
    result = determine_winner(user_choice, computer_choice)
    return jsonify({
        "user_choice": user_choice,
        "computer_choice": computer_choice,
        "result": result
    }), 200

if __name__ == "__main__":
    app.run(debug=True)