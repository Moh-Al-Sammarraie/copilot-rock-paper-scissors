import unittest
from main_rest import app

class TestGameAPI(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()
        self.client.testing = True

    def test_valid_choices(self):
        for choice in ["rock", "paper", "scissors", "lizard", "spock"]:
            response = self.client.post('/game', json={"choice": choice})
            data = response.get_json()
            self.assertEqual(response.status_code, 200)
            self.assertIn("user_choice", data)
            self.assertIn("computer_choice", data)
            self.assertIn("result", data)
            self.assertIn(data["user_choice"], ["rock", "paper", "scissors", "lizard", "spock"])
            self.assertIn(data["computer_choice"], ["rock", "paper", "scissors", "lizard", "spock"])

    def test_invalid_choice(self):
        response = self.client.post('/game', json={"choice": "invalid"})
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.get_json(), {"error": "Invalid choice"})

if __name__ == '__main__':
    unittest.main()