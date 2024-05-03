import random  # Import the random module to generate a random number

def guessing_game():
    print("Welcome to the Guessing Game!")
    print("I’m thinking of a number between 1 and 100. Can you guess it?")

    # Generate a random number between 1 and 100
    secret_number = random.randint(1, 100)

    # Initialize variables
    attempts = 0

    while True:
        # Get user's guess
        guess = int(input("Guess: "))

        # Increment the number of attempts
        attempts += 1

        # Check if the guess is correct
        if guess == secret_number:
            print(f"Yes! You guessed correctly after {attempts} tries! Congratulations.")
            break
        elif guess < secret_number:
            print("Good try, but that’s too low. Try again.")
        else:
            print("Good try, but that’s too high. Try again.")

# Call the guessing_game function to start the game
guessing_game()
