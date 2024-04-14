# Guessing Game Adventure: Crack the Code!

# Are you ready for a thrilling challenge? Let's dive into the exciting world of Python with this guessing game!
# Don't worry if you're new to coding; we'll guide you through each step.

# Step 1: Importing Libraries
# To make our game more dynamic, we need the help of Python's 'random' library.
# Libraries hold functions that other people have created and made available to other coders.
# This library allows us to generate random numbers, adding an element of surprise to our game.
# Usually, libraries are imported at the very top of a script.

import random

# Step 2: Welcome Message
# After importing the library(s), we'll greet you and introduce the game.
# It is often recommended to start the code with a printout indicating that it has successfully started.

print("Welcome to the Guessing Game!")

# Step 3: Random Number Generation
# We'll pick a secret number between 1 and 10 using the 'randint' function from the 'random' library.

secret_number = random.randint(1, 10)

# Step 4: Initialize Guess Count
# We'll keep track of how many attempts it takes you to guess the secret number.

guess_count = 0

# Step 5: The Guessing Loop
# Now, it's time for the real challenge! We'll loop until you guess the correct number.
# While loops repeat everything inside the loop until the condition next to while becomes False.
# In this case, "while True:" means that the loop will never end unless something within the loop causes it to.

# !!! Important Note !!!
# ALWAYS have an escape plan with loops, otherwise you can crash your computer with an infinite loop!
# In the loop below, the "break" function will allow for an exit when the game is won.
# Other strategies include a set number of loops (using for-loops) or having a timer that exits after a set time.

while True:
    # Loop Step I: Prompting for Guess
    # We'll ask you to guess the secret number using the 'input' function. 
    # Don't forget, we'll convert your input into an integer using 'int()'.
    
    guess = int(input("Guess the secret number (between 1 and 10): "))
    guess_count += 1

    # Loop Step II: Checking Guess
    # We'll compare your guess with the secret number. 
    # If you get it right, congratulations! We'll let you know how many attempts it took.
    # Otherwise, we'll encourage you to try again.
    
    # This is an if-else statement that checks if a condition is true.
    # In this case the condition is "guess == secret_number".
    # This asks if the variable "guess" is equal to the variable "secret_number"
    # If this condition is true, it will print the congratulations and break
    # If this condition is false, it will print the "sorry, try again" statement under "else:"
    if guess == secret_number:
        print("Congratulations! You guessed the secret number in", guess_count, "attempts.")

        # "break" is a command that allows you to exit the current loop (even if the loop condition is not met)
        break
    else:
        print("Sorry, that's not the secret number. Try again!")

# Keep exploring and challenging yourself. Who knows what adventures await in the world of coding?
