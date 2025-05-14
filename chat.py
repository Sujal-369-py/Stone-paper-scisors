import tkinter as tk
from random import choice

choices = ['Rock', 'Paper', 'Scissors']

def computer_choice():
    return choice(choices)

def check_winner(user, comp):
    if user == comp:
        return "It's a Tie!"
    elif (user == 'Rock' and comp == 'Scissors') or \
         (user == 'Paper' and comp == 'Rock') or \
         (user == 'Scissors' and comp == 'Paper'):
        return f"You Win! Computer chose {comp}"
    else:
        return f"You Lose! Computer chose {comp}"

def on_user_choice(user_choice):
    comp = computer_choice()
    result = check_winner(user_choice, comp)
    result_label.config(text=result)

def reset():
    result_label.config(text="Choose your move:")

# GUI Setup
root = tk.Tk()
root.title("Rock Paper Scissors")
root.geometry("300x250")
root.resizable(False, False)

tk.Label(root, text="Rock Paper Scissors", font=("Arial", 20, "bold")).pack(pady=10)
tk.Label(root, text="Your Move:", font=("Arial", 12)).pack()

button_frame = tk.Frame(root)
button_frame.pack(pady=10)

for move in choices:
    tk.Button(button_frame, text=move, width=10, command=lambda m=move: on_user_choice(m)).pack(side=tk.LEFT, padx=5)

result_label = tk.Label(root, text="Choose your move:", font=("Arial", 12), fg="blue")
result_label.pack(pady=20)

tk.Button(root, text="Play Again", command=reset).pack()

root.mainloop()
