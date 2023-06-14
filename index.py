import random
import tkinter as tkinter
from tkinter import messagebox

def generate_random_number():
    return random.randint(1, 100)

def check_guess():
    guess = int(guess_entry.get())
    if guess < number_to_guess:
        result_label.config(text='Too low! Try again.')



def reset_game():
    global number_to_guess, num_guesses
    number_to_guess = generate_random_number()
    num_guesses = 0