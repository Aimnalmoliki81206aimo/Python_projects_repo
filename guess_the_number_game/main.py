# Guess the Number Game
# This is a simple number guessing game where the user can define the range of numbers.

import random
import math

# Function to get user input and validate that it's an integer
def get_user_input():
    while True:
        try:
            lower_number = int(input("Enter the lower number: "))
            higher_number = int(input("Enter the higher number: "))
            break
        except ValueError:
            print("Invalid input! Please enter valid integer numbers.")
    return lower_number, higher_number

# Function to check if the input numbers are valid
def check_input(lower_number, higher_number, min_range_size=3):
    # Check for negative numbers
    if lower_number < 0 or higher_number < 0:
        print("Both numbers must be non-negative.")
        return False
    
    # Check if lower number is greater than or equal to higher
    if lower_number >= higher_number:
        print("The lower number must be less than the higher number.")
        return False

    # Check if the range between numbers is too small
    if (higher_number - lower_number) < min_range_size:
        print("The range is too small. Please choose a wider range.")
        return False
    return True

# Function to get a valid range or return None
def get_valid_range():
    lower_number, higher_number = get_user_input()
    if not check_input(lower_number, higher_number):
        return None
    else:
        return lower_number, higher_number
    
# Function to calculate the allowed attempts based on range size using log2
def attempts_allowed(lower_number, higher_number):
    attempts = math.ceil(math.log2(higher_number - lower_number + 1))
    return attempts

# Main game logic
def game():
    valid_range = get_valid_range()
    if not valid_range:
        print("Try again with valid inputs.\n")
        return
    lower_number, higher_number = valid_range
    secret_number = random.randint(lower_number, higher_number)
    print(f"The secret number is between {lower_number} and {higher_number}.")
    attempts = 0
    attempts_allow = attempts_allowed(lower_number, higher_number)
    print("You have", attempts_allow, "attempts to guess the number.")
    
    # Game loop for guessing
    while attempts < attempts_allow:
        try:
            guess = int(input("Enter your guess: "))
        except ValueError:
            print("Invalid input! Please enter valid integer numbers.")
            continue
        if guess < lower_number or guess > higher_number:
            print("Your guess is out of range. Please try again.")
        elif guess < secret_number:
            print("Your guess is too low.")
            attempts += 1
            print(f"You have {attempts_allow - attempts} attempts left.")
        elif guess > secret_number:
            print("Your guess is too high.")
            attempts += 1
            print(f"You have {attempts_allow - attempts} attempts left.")
        else:
            print("Congratulations! You've guessed the number:", secret_number)
            break


# Game start message
print("Welcome to the Guess the Number game!")
print("you can choose the range of numbers but you must choose integer numbers")

# Game loop to allow replay
while True:
    game()
    play_again = input("Do you want to play again? (yes/no): ").strip().lower()
    if play_again != 'yes':
        print("Thank you for playing! Goodbye!")
        break
