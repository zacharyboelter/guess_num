import random
import tkinter as tk
from tkinter import messagebox

def generate_random_number():
    return random.randint(1, 100)

def check_guess():
    guess = int(guess_entry.get())
    if guess < number_to_guess:
        result_label.config(text = 'Too low! Try again.')
    elif guess > number_to_guess:
        result_label.congig(text = 'Too high! Guess lower.')
    else:
        messagebox.showinfo('Thats a bingo!', f"You correctly guessed the number in {num_guesses} attempts.")
        reset_game()
    



def reset_game():
    global number_to_guess, num_guesses
    number_to_guess = generate_random_number()
    num_guesses = 0
    result_label.config(text='')