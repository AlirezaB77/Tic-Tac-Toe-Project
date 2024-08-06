import random

class TicTacToe:
    """A class to represent a Tic-Tac-Toe game."""

    def __init__(self):
        """Initialize the game with an empty board and a random starting player."""
        self.board = [' '] * 10  # Index 0 is ignored for easier board representation
        self.player_turn = self.get_random_player()

    def get_random_player(self):
        """Randomly choose the starting player.

        Returns:
            str: 'X' or 'O'
        """
        return random.choice(["X", "O"])

    def switch_player(self):
        """Switch the current player.

        Returns:
            str: The new current player ('X' or 'O')
        """
        self.player_turn = "X" if self.player_turn == "O" else "O"
        return self.player_turn

    def show_board(self):
        """Display the current state of the game board."""
        print(f"{self.board[1]}|{self.board[2]}|{self.board[3]}")
        print("------")
        print(f"{self.board[4]}|{self.board[5]}|{self.board[6]}")
        print("------")
        print(f"{self.board[7]}|{self.board[8]}|{self.board[9]}")

    def is_board_full(self):
        """Check if the board is completely filled.

        Returns:
            bool: True if the board is full, False otherwise
        """
        return " " not in self.board[1:]

    def fix_spot(self, player, cell):
        """Place a player's mark on the specified cell.

        Args:
            player (str): The current player ('X' or 'O')
            cell (int): The cell number to place the mark (1-9)
        """
        self.board[cell] = player

    def player_won(self, player):
        """Check if the given player has won.

        Args:
            player (str): The player to check for win ('X' or 'O')

        Returns:
            bool: True if the player has won, False otherwise
        """
        win_combinations = [
            (1, 2, 3), (4, 5, 6), (7, 8, 9),  # Rows
            (1, 4, 7), (2, 5, 8), (3, 6, 9),  # Columns
            (1, 5, 9), (3, 5, 7)  # Diagonals
        ]
        return any(self.board[c[0]] == self.board[c[1]] == self.board[c[2]] == player for c in win_combinations)

    def start(self):
        """Start and manage the game loop."""
        while True:
            print(f"\nIt's {self.player_turn}'s turn to choose\n")
            self.show_board()
            
            try:
                user_choice = int(input("Enter cell number (1-9): "))
                if user_choice not in range(1, 10):
                    raise ValueError
            except ValueError:
                print("Invalid input. Please enter a number between 1 and 9.")
                continue

            if self.board[user_choice] == " ":
                self.fix_spot(self.player_turn, user_choice)
                
                if self.player_won(self.player_turn):
                    print('')
                    self.show_board()
                    print(f"Player {self.player_turn} wins the game!")
                    break
                
                if self.is_board_full():
                    print('')
                    self.show_board()
                    print("It's a draw!")
                    break
                
                self.switch_player()
            else:
                print("That cell is already occupied. Try again.")

if __name__ == "__main__":
    game = TicTacToe()
    game.start()