import unittest
from unittest.mock import patch
from main import get_user_choice, get_computer_choice, determine_winner, play_game

class TestRockPaperScissorsGame(unittest.TestCase):

	def test_get_user_choice_rock(self):
		with patch('builtins.input', return_value='1'):
			self.assertEqual(get_user_choice(), 'rock')

	def test_get_user_choice_paper(self):
		with patch('builtins.input', return_value='2'):
			self.assertEqual(get_user_choice(), 'paper')

	def test_get_user_choice_scissors(self):
		with patch('builtins.input', return_value='3'):
			self.assertEqual(get_user_choice(), 'scissors')

	def test_get_user_choice_lizard(self):
		with patch('builtins.input', return_value='4'):
			self.assertEqual(get_user_choice(), 'lizard')

	def test_get_user_choice_spock(self):
		with patch('builtins.input', return_value='5'):
			self.assertEqual(get_user_choice(), 'spock')

	def test_get_computer_choice(self):
		choices = ["rock", "paper", "scissors", "lizard", "spock"]
		computer_choice = get_computer_choice()
		self.assertIn(computer_choice, choices)

	def test_determine_winner_tie(self):
		self.assertEqual(determine_winner("rock", "rock"), "It's a tie!")

	def test_determine_winner_user_wins(self):
		self.assertEqual(determine_winner("rock", "scissors"), "You win!")

	def test_determine_winner_computer_wins(self):
		self.assertEqual(determine_winner("rock", "paper"), "You lose!")

	@patch('builtins.input', side_effect=['1'])
	@patch('builtins.print')
	def test_play_game(self, mock_print, mock_input):
		with patch('main.get_computer_choice', return_value='scissors'):
			play_game()
			mock_print.assert_called_with("You win!")

class TestRockPaperScissorsLizardSpock(unittest.TestCase):

	def test_get_user_choice_valid(self):
		for choice, expected in zip(range(1, 6), ["rock", "paper", "scissors", "lizard", "spock"]):
			with patch('builtins.input', return_value=str(choice)):
				self.assertEqual(get_user_choice(), expected)

	def test_get_user_choice_invalid_then_valid(self):
		with patch('builtins.input', side_effect=['6', '2']):
			self.assertEqual(get_user_choice(), "paper")

	def test_get_computer_choice(self):
		choices = {"rock", "paper", "scissors", "lizard", "spock"}
		computer_choices = set(get_computer_choice() for _ in range(100))
		self.assertTrue(choices.issubset(computer_choices))

	def test_determine_winner(self):
		outcomes = {
			("rock", "scissors"): "You win!",
			("paper", "rock"): "You win!",
			("scissors", "paper"): "You win!",
			("rock", "paper"): "You lose!",
			("paper", "scissors"): "You lose!",
			("scissors", "rock"): "You lose!",
			("rock", "rock"): "It's a tie!",
			("paper", "paper"): "It's a tie!",
			("scissors", "scissors"): "It's a tie!",
		}
		for (user, computer), result in outcomes.items():
			self.assertEqual(determine_winner(user, computer), result)

	@patch('main.print')
	@patch('main.get_user_choice', return_value='rock')
	@patch('main.get_computer_choice', return_value='scissors')
	def test_play_game(self, mock_get_computer_choice, mock_get_user_choice, mock_print):
		play_game()
		mock_print.assert_any_call("Computer chose: scissors")
		mock_print.assert_any_call("You win!")

if __name__ == '__main__':
	unittest.main()