import random

def generate_random_number():
    return random.randint(1, 100)

def get_player_guess():
    while True:
        try:
            guess = int(input("Enter your guess (between 1 and 100): "))
            return guess
        except ValueError:
            print("Invalid input. Please enter a number.")

def play_game():
    number_to_guess = generate_random_number()
    num_guesses = 0

    print("Welcome to Guess the Number!")
    print("I'm thinking of a number between 1 and 100.")

    while True:
        guess = get_player_guess()
        num_guesses += 1

        if guess < number_to_guess:
            print("Too low! Try again.")
        elif guess > number_to_guess:
            print("Too high! Try again.")
        else:
            print(f"Congratulations! You guessed the number in {num_guesses} tries.")
            break

        play_again = input("Do you want to play again? (yes/no): ")
        if play_again.lower() != "yes":
            print("Thank you for playing!")
            break

play_game()