# Tic-Tac-Toe Game

## Description
This is a simple command-line implementation of the classic Tic-Tac-Toe game written in Python. Two players take turns marking spaces on a 3x3 grid, aiming to get three of their marks in a row, column, or diagonal.

## Features
- Random selection of starting player
- Interactive command-line interface
- Player turn switching
- Win condition checking
- Draw condition checking

## Installation
1. Ensure you have Python 3.x installed on your system.
2. Download the `tic_tac_toe.py` file.

## Usage
1. Open a terminal or command prompt.
2. Navigate to the directory containing `tic_tac_toe.py`.
3. Run the script using Python:
   ```
   python tic_tac_toe.py
   ```
4. Follow the on-screen prompts to play the game.

## How to Play
1. The game randomly selects whether 'X' or 'O' goes first.
2. Players take turns entering a number from 1-9 to place their mark on the board.
3. The game ends when a player gets three in a row or when the board is full (resulting in a draw).

## Board Layout
The board is represented as follows:
```
1|2|3
-----
4|5|6
-----
7|8|9
```
Enter the number corresponding to the cell where you want to place your mark.

## Game Rules
- Players alternate turns.
- A player wins by getting three of their marks in a row (horizontally, vertically, or diagonally).
- If all cells are filled and no player has won, the game is a draw.

## Future Improvements
- Implement an AI opponent
- Add a graphical user interface
- Include an option to play multiple rounds
- Implement difficulty levels for AI
