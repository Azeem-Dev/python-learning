import tkinter as tk
from tkinter import messagebox
import random

def check_winner():
    """Check if there is a winner or a tie"""
    for user in USERS:
        # Horizontal
        if board['top-L'] == board['top-M'] == board['top-R'] == user:
            return user
        if board['mid-L'] == board['mid-M'] == board['mid-R'] == user:
            return user
        if board['low-L'] == board['low-M'] == board['low-R'] == user:
            return user

        # Vertical
        if board['top-L'] == board['mid-L'] == board['low-L'] == user:
            return user
        if board['top-M'] == board['mid-M'] == board['low-M'] == user:
            return user
        if board['top-R'] == board['mid-R'] == board['low-R'] == user:
            return user

        # Diagonal
        if board['top-L'] == board['mid-M'] == board['low-R'] == user:
            return user
        if board['top-R'] == board['mid-M'] == board['low-L'] == user:
            return user

    if all(value != ' ' for value in board.values()):
        return 'Tie'

    return None

def handle_click(position):
    global current_turn

    if board[position] != ' ':
        messagebox.showwarning("Invalid Move", "This spot is already occupied!")
        return

    board[position] = current_turn
    buttons[position].config(text=current_turn, state=tk.DISABLED)

    winner = check_winner()
    if winner:
        if winner == 'Tie':
            messagebox.showinfo("Game Over", "It's a Tie!")
        else:
            messagebox.showinfo("Game Over", f"Player {winner} wins!")
        reset_game()
    else:
        current_turn = 'O' if current_turn == 'X' else 'X'
        label_turn.config(text=f"Turn: Player {current_turn}")

def reset_game():
    global board, current_turn
    current_turn = random.choice(USERS)
    label_turn.config(text=f"Turn: Player {current_turn}")

    for key in board.keys():
        board[key] = ' '
        buttons[key].config(text=' ', state=tk.NORMAL)

# Initialize the game
USERS = ['O', 'X']
current_turn = random.choice(USERS)

board = {
    'top-L': ' ', 'top-M': ' ', 'top-R': ' ',
    'mid-L': ' ', 'mid-M': ' ', 'mid-R': ' ',
    'low-L': ' ', 'low-M': ' ', 'low-R': ' '
}

# Create the GUI
root = tk.Tk()
root.title("Tic Tac Toe")

label_turn = tk.Label(root, text=f"Turn: Player {current_turn}", font=("Arial", 14))
label_turn.grid(row=0, column=0, columnspan=3)

buttons = {}

for idx, position in enumerate(board.keys()):
    row, col = divmod(idx, 3)
    button = tk.Button(root, text=' ', font=("Arial", 20), height=2, width=5, command=lambda pos=position: handle_click(pos))
    button.grid(row=row + 1, column=col)
    buttons[position] = button

reset_button = tk.Button(root, text="Reset", font=("Arial", 12), command=reset_game)
reset_button.grid(row=4, column=0, columnspan=3)

# Start the main loop
root.mainloop()
