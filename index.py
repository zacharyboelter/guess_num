import random
import pygame
from pygame.locals import *

# Initialize Pygame
pygame.init()

# Set up the game window
window_width, window_height = 400, 300
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Guess the Number")

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Generate a random number between 1 and 100
number_to_guess = random.randint(1, 100)

# Font setup
font = pygame.font.SysFont(None, 32)

def draw_text(text, x, y, color=WHITE):
    surface = font.render(text, True, color)
    window.blit(surface, (x, y))

# Game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False

        if event.type == KEYDOWN:
            if event.key == K_RETURN:
                guess = guess_text.strip()

                try:
                    guess = int(guess)

                    if guess < number_to_guess:
                        result = "Too low!"
                    elif guess > number_to_guess:
                        result = "Too high!"
                    else:
                        result = "Congratulations! You guessed the number!"
                        running = False

                except ValueError:
                    result = "Invalid input. Please enter a valid number."

    # Clear the window
    window.fill(BLACK)

    # Draw text and input field
    draw_text("Guess a number between 1 and 100:", 50, 50)
    draw_text("Your guess:", 50, 100)
    guess_text = pygame.draw.rect(window, WHITE, (150, 100, 100, 32), 2)

    # Display the result
    draw_text(result, 50, 150)

    # Update the display
    pygame.display.flip()

# Quit the game
pygame.quit()
