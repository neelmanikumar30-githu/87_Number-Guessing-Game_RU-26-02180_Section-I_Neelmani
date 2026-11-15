import random


def get_valid_guess(attempts_left):
    """
    Get and validate a guess from the user.
    Invalid inputs (non-numbers or out of range) do not consume an attempt.
    """
    while True:
        user_input = input("Enter your guess (1-100): ").strip()

        if not user_input.lstrip("-").isdigit():
            print("Invalid input. Enter a whole number.")
            continue

        guess = int(user_input)

        if guess < 1 or guess > 100:
            print("Out of range. Enter a number between 1 and 100.")
            print(f"Attempts left: {attempts_left} (no attempt lost)")
            continue

        return guess


def play_game():
    """
    Play one round of the Number Guessing Game.
    Returns the number of attempts used.
    """
    secret = random.randint(1, 100)

    max_attempts = 5
    attempts_used = 0

    print("\n Number Guessing Game ")
    print("I have selected a number between 1 and 100.")
    print(f"You have {max_attempts} attempts to guess it.\n")

    while attempts_used < max_attempts:
        attempts_left_before = max_attempts - attempts_used
        guess = get_valid_guess(attempts_left_before)
        attempts_used += 1
        attempts_left = max_attempts - attempts_used

        if guess == secret:
            print(f"Congratulations! You guessed it in {attempts_used} attempt{'s' if attempts_used != 1 else ''}.")
            return attempts_used

        if guess < secret:
            print(f"Too low! Attempts left: {attempts_left}")
        else:
            print(f"Too high! Attempts left: {attempts_left}")

    print(f"Game Over! The number was {secret}.")
    return attempts_used


def main():
    """Main loop that allows the player to play multiple rounds."""
    while True:
        attempts = play_game()
        print(f"\nAttempts used: {attempts}")
        choice = input("Play again? (y/n): ").strip().lower()
        if choice != "y":
            print("Thanks for playing! Goodbye.")
            break


if __name__ == "__main__":
    main()         
