# EXERCISE XP 

# Create a class Game that allows a user to play rock paper scissors against the computer. The class should have

import random


class Game:
    ITEMS = ("rock", "paper", "scissors")

    def get_user_item(self):
        mapping = {"r": "rock", "p": "paper", "s": "scissors"}
        while True:
            choice = input("Select (r)ock, (p)aper, or (s)cissors: ").strip().lower()
            if choice in mapping:
                return mapping[choice]
            if choice in self.ITEMS:
                return choice
            print("Invalid choice. Try again.")

    def get_computer_item(self):
        return random.choice(self.ITEMS)

    def get_game_result(self, user_item, computer_item):
        if user_item == computer_item:
            return "draw"
        wins = {
            ("rock", "scissors"),
            ("scissors", "paper"),
            ("paper", "rock"),
        }
        return "win" if (user_item, computer_item) in wins else "loss"

    def play(self):
        user_item = self.get_user_item()
        computer_item = self.get_computer_item()
        result = self.get_game_result(user_item, computer_item)

        messages = {
            "win": f"You selected {user_item}. The computer selected {computer_item}. You win!",
            "loss": f"You selected {user_item}. The computer selected {computer_item}. You lose.",
            "draw": f"You selected {user_item}. The computer selected {computer_item}. You drew!",
        }
        print(messages[result])
        return result