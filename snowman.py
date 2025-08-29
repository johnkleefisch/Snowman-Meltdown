import random

# List of secret words
WORDS = ["python", "git", "github", "snowman", "meltdown"]

def get_random_word():
    """Selects a random word from the list."""
    return WORDS[random.randint(0, len(WORDS) - 1)]

def play_game():
    secret_word = get_random_word()
    guessed_letters = []
    max_attempts = 6
    attempts_left = max_attempts

    print("Welcome to Snowman Meltdown!")

    # Game loop
    while attempts_left > 0:
        # Show progress (e.g., _ y t h o n)
        display_word = " ".join([letter if letter in guessed_letters else "_" for letter in secret_word])
        print("\nWord:", display_word)
        print("Attempts left:", attempts_left)

        # Check victory
        if all(letter in guessed_letters for letter in secret_word):
            print("🎉 You guessed the word! The snowman is safe!")
            break

        # Get input
        guess = input("Guess a letter: ").lower()

        if not guess.isalpha() or len(guess) != 1:
            print("⚠️ Please enter only a single letter.")
            continue

        if guess in guessed_letters:
            print("⚠️ You already guessed that letter.")
            continue

        # Check guess
        if guess in secret_word:
            guessed_letters.append(guess)
            print("✅ Correct!")
        else:
            attempts_left -= 1
            print("❌ Wrong guess!")

    else:
        print("\n💀 No attempts left. The word was:", secret_word)

if __name__ == "__main__":
    play_game()
