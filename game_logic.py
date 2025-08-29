# game_logic.py

import random
from ascii_art import STAGES

def get_random_word() -> str:
    """
    Select a random word from the predefined WORDS list.

    Returns:
        str: The randomly selected secret word.
    """
    WORDS = ["python", "git", "github", "snowman", "meltdown"]
    return WORDS[random.randint(0, len(WORDS) - 1)]


def display_game_state(mistakes: int, secret_word: str, guessed_letters: list):
    """
    Display the current state of the game, including the ASCII art
    for the snowman and the word progress.

    Args:
        mistakes (int): Number of incorrect guesses made.
        secret_word (str): The secret word the player is trying to guess.
        guessed_letters (list): List of letters guessed so far.
    """
    print("\n" + "="*30)
    print(STAGES[mistakes])
    display_word = " ".join([letter if letter in guessed_letters else "_" for letter in secret_word])
    print("Word:", display_word)
    print("="*30 + "\n")


def get_valid_guess(guessed_letters: list) -> str:
    """
    Prompt the player for a valid single alphabetical letter that
    has not been guessed before.

    Args:
        guessed_letters (list): Letters already guessed.

    Returns:
        str: Validated letter input by the player.
    """
    while True:
        guess = input("Guess a letter: ").lower()
        if not guess.isalpha() or len(guess) != 1:
            print("⚠️ Invalid input. Please enter a single letter.")
        elif guess in guessed_letters:
            print("⚠️ You already guessed that letter.")
        else:
            return guess


def play_game():
    """
    Main function to run the Snowman Meltdown game.
    Handles game loop, player input, updating game state, and replay option.
    """
    while True:
        secret_word = get_random_word()
        guessed_letters = []
        mistakes = 0
        max_mistakes = len(STAGES) - 1

        print("❄️ Welcome to Snowman Meltdown! ❄️")

        while mistakes < max_mistakes:
            display_game_state(mistakes, secret_word, guessed_letters)

            # Check for victory
            if all(letter in guessed_letters for letter in secret_word):
                print("🎉 Congratulations! You guessed the word and saved the snowman!")
                break

            # Get validated guess
            guess = get_valid_guess(guessed_letters)

            # Update game state
            if guess in secret_word:
                guessed_letters.append(guess)
                print("✅ Correct guess!")
            else:
                mistakes += 1
                print("❌ Wrong guess. The snowman is melting!")

        else:
            display_game_state(mistakes, secret_word, guessed_letters)
            print("💀 Game over! The snowman melted!")
            print(f"The word was: {secret_word}")

        # Replay option
        replay = input("\nDo you want to play again? (y/n): ").lower()
        if replay != 'y':
            print("Thanks for playing Snowman Meltdown! Goodbye!")
            break


if __name__ == "__main__":
    play_game()
