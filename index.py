import random
import tkinter as tk
from tkinter import ttk, messagebox

style = ttk.Style()

style.configure("TLabel", font=("Arial", 14))
style.configure("TButton", font=("Arial", 12))
style.configure("TEntry", font=("Arial", 12))

def generate_random_number():
    return random.randint(1, 100)

def check_guess():
    guess = int(guess_entry.get())
    if guess < number_to_guess:
        result_label.config(text = "Too low! Try again.")
    elif guess > number_to_guess:
        result_label.congig(text = "Too high! Guess lower.")
    else:
        messagebox.showinfo("Thats a bingo!", f"You correctly guessed the number in {num_guesses} attempts.")
        reset_game()
    
    guess_entry.delete(0, tk.END)
    guess_entry.focus()



def reset_game():
    global number_to_guess, num_guesses
    number_to_guess = generate_random_number()
    num_guesses = 0
    result_label.config(text="")
    guess_entry.delete(0, tk.END)
    guess_entry.focus()


window= tk.Tk()
window.title("Guess the Number")

number_to_guess = generate_random_number()
num_guesses = 0

instruction_label = tk.Label(window, text="Guess a number between 1 and 100:")
instruction_label.pack()

guess_entry = tk.Entry(window)
guess_entry.pack()
guess_entry.focus()

check_button = tk.Button(window, text="Check", command=check_guess)
check_button.pack()

result_label = tk.Label(window, text="")
result_label.pack()

reset_game()

window.mainloop()