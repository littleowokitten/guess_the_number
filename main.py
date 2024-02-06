import random

print("Welcome to the number guessing game!")
print("Try to guess the correct number within a specified range.")
print("You have to guess the correct number; can you get to level 5?")

# Function to play the number guessing game
def guess_the_number(level):
    # Set the range and attempts based on the chosen level
    if level not in {1, 2, 3, 4, 5}:
        print("Invalid level. Please choose a level between 1 and 4.")
        return

    if level == 1:
        low, high, attempts = 1, 5, 3
    elif level == 2:
        low, high, attempts = 1, 10, 4 
    elif level == 3:
        low, high, attempts = 1, 15, 5
    elif level == 4:
        low, high, attempts = 1, 20, 6
    elif level == 5:
        low, high, attempts = 1, 25, 7

    # Generate a random number within the specified range
    secret_number = random.randint(low, high)

    # Allow the user a certain number of attempts to guess the number
    for _attempt in range(attempts):
        try:
            # Get the user's guess
            guess = int(input(f"Guess the number (between {low} and {high}): "))
        except ValueError:
            # Handle invalid input (non-integer)
            print("Invalid input. Please enter a valid integer.")
            continue

        # Check if the guess is correct
        if guess == secret_number:
            print("Congratulations! You guessed the correct number.")
            return True  # Return True to indicate the game is won
        else:
            print("Wrong guess. Try again.")
    else:
        # If all attempts are used up, reveal the correct number
        print(f"Sorry, you've run out of attempts. The correct number was {secret_number}.")
        return False  # Return False to indicate the game is lost

# Main block
if __name__ == "__main__":
    while True:
        # Get the user's chosen level
        chosen_level = input("Choose a level (1, 2, 3, 4, or 5.): ")
        try:
            chosen_level = int(chosen_level)
        except ValueError:
            # Handle invalid input (non-integer)
            print("Invalid input. Please enter a valid integer.")
            continue

        # Play the game with the chosen level
        game_won = guess_the_number(chosen_level)

        # Ask the user if they want to play again
        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != 'yes':
          print ("see you later!")
            break

