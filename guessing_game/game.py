import random


def check_guess(target: int, guess: int) -> str:
    """Compare a guess to the target and return the result.

    This function has no randomness and no input() calls, which makes
    it fully testable on its own — same idea as checkWinner() in the
    Tic-Tac-Toe project.
    """
    if guess == target:
        return "correct"
    elif guess < target:
        return "too low"
    else:
        return "too high"


def play_game(lower: int = 1, upper: int = 100) -> None:
    """Run one full game in the console: pick a random number, then
    loop asking the player to guess until they get it right.
    """
    target = random.randint(lower, upper)
    attempts = 0

    print(f"I'm thinking of a number between {lower} and {upper}.")

    while True:
        guess_input = input("Your guess: ").strip()

        try:
            guess = int(guess_input)
        except ValueError:
            print("Please enter a whole number.")
            continue

        attempts += 1
        result = check_guess(target, guess)

        if result == "correct":
            print(f"Correct! You got it in {attempts} attempts.")
            break
        elif result == "too low":
            print("Too low — try again.")
        else:
            print("Too high — try again.")


if __name__ == "__main__":
    play_game()
