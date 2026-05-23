# EXERCISE XP

# Create a class Game that allows a user to play rock paper scissors against the computer. The class should have


from Game import Game


def get_user_menu_choice():
    print("\nMenu:")
    print("(g) Play a new game")
    print("(x) Show scores and exit")
    choice = input(": ").strip().lower()
    if choice in ("g", "x"):
        return choice
    print("Invalid choice.")
    return None


def print_results(results):
    print("\nGame Results:")
    print(f"  You won {results.get('win', 0)} times")
    print(f"  You lost {results.get('loss', 0)} times")
    print(f"  You drew {results.get('draw', 0)} times")
    print("\nThank you for playing!")


def main():
    results = {"win": 0, "loss": 0, "draw": 0}

    while True:
        choice = get_user_menu_choice()
        if choice == "g":
            game = Game()
            result = game.play()
            results[result] += 1
        elif choice == "x":
            print_results(results)
            break


if __name__ == "__main__":
    main()




# EXERCISE XP GOLD

def display_board(board):
    print()
    for i in range(3):
        row = " | ".join(board[i * 3:(i + 1) * 3])
        print(f" {row}")
        if i < 2:
            print("---+---+---")
    print()


def player_input(board, player):
    while True:
        try:
            pos = int(input(f"Player {player}, choose a position (1-9): "))
        except ValueError:
            print("Please enter a number.")
            continue
        if pos < 1 or pos > 9:
            print("Position must be between 1 and 9.")
            continue
        if board[pos - 1] in ("X", "O"):
            print("Position already taken.")
            continue
        board[pos - 1] = player
        return


def check_win(board, player):
    wins = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8),   # rows
        (0, 3, 6), (1, 4, 7), (2, 5, 8),   # columns
        (0, 4, 8), (2, 4, 6),              # diagonals
    ]
    return any(board[a] == board[b] == board[c] == player for a, b, c in wins)


def is_full(board):
    return all(cell in ("X", "O") for cell in board)


def play():
    board = [str(i + 1) for i in range(9)]
    players = ("X", "O")
    turn = 0

    print("Welcome to Tic Tac Toe!")
    print("Positions are numbered 1-9 (left to right, top to bottom).")

    while True:
        display_board(board)
        player = players[turn % 2]
        player_input(board, player)

        if check_win(board, player):
            display_board(board)
            print(f"Player {player} wins!")
            return
        if is_full(board):
            display_board(board)
            print("It's a tie!")
            return

        turn += 1


if __name__ == "__main__":
    play()