# Console based hangman game.

import random
import os

# Constants
WORDS = ("python", "jumble", "easy", "difficult", "answer", "xylophone",
         "hangman", "computer", "science", "programming", "mathematics",
         "player", "condition", "reverse", "water", "board", "geeks",
         "keyboard", "laptop", "headphone", "mouse", "printer",
         "scanner", "software", "hardware", "network", "server")

HANGMAN_STAGES = (
    """
      -------
      |/    |
      |
      |
      |
      |
      |
     /|\\
    -----------
    """, """
      -------
      |/    |
      |     O
      |
      |
      |
      |
     /|\\
    -----------
    """, """
      -------
      |/    |
      |     O
      |     |
      |
      |
      |
     /|\\
    -----------
    """, """
      -------
      |/    |
      |     O
      |     |
      |     |
      |
      |
     /|\\
    -----------
    """, """
      -------
      |/    |
      |     O
      |    /|
      |     |
      |
      |
     /|\\
    -----------
    """, """
      -------
      |/    |
      |     O
      |    /|\\
      |     |
      |
      |
     /|\\
    -----------
    """, """
      -------
      |/    |
      |     O
      |    /|\\
      |     |
      |    /
      |
     /|\\
    -----------
    """, """
      -------
      |/    |
      |     O
      |    /|\\
      |     |
      |    / \\
      |
     /|\\
    -----------
""")


# Functions
def clear_screen():
    """Clears the screen."""
    os.system("cls" if os.name == "nt" else "clear")


def get_random_word():
    """Returns a random word from the WORDS tuple."""
    return random.choice(WORDS)


def splash_screen():
    """The splash screen."""
    print("""
             _   _                                               -----
            | | | | __ _ _ __   __ _ _ __ ___   __ _ _ __       |    o
            | |_| |/ _` | '_ \\ / _` | '_ ` _ \\ / _` | '_ \\      |   /|\\
            |  _  | (_| | | | | (_| | | | | | | (_| | | | |     |   / \\
            |_| |_|\\__,_|_| |_|\\__, |_| |_| |_|\\__,_|_| |_|     |
                               |___/                            v1.0
    """)
    input("Press enter to continue...")
    clear_screen()


def display(wrong, word, letters):
    """Displays current status of the game"""
    clear_screen()
    print("Hangman game. Try to guess the word. (CTRL+C to quit)")
    print(HANGMAN_STAGES[wrong])
    print(" ".join(word), end='    ')
    print("(Guessed letters: " + ", ".join(letters), ")")
    print()


def get_guess(letters):
    """Gets an input with a valid letter"""
    while True:
        guess = input("Guess a letter: ").lower()
        if len(guess) == 1 and guess.isalpha():
            # check if letter has already been guessed
            if guess in letters:
                print("You have already guessed that letter.")
            else:
                return guess
        else:
            print("Invalid guess. Please enter a single letter.")


def check_win(word):
    if "_" not in word:
        print("You win!")
        return True
    return False


def check_loss(wrong):
    if wrong == len(HANGMAN_STAGES)-1:
        print("You lose!")
        return True
    return False


def update_guess(word, guessed_word, guess):
    for i in range(len(word)):
        if word[i] == guess:
            guessed_word[i] = guess
    return guessed_word


def play_round():
    """Plays a round"""
    # Setup
    word = get_random_word()
    guessed_letters = []
    guessed_word = ["_"] * len(word)
    wrong_guesses = 0

    # game inner loop
    while True:
        display(wrong_guesses, guessed_word, guessed_letters)

        # check if player has won/lost
        if check_win(guessed_word) or check_loss(check_loss):
            break

        # make sure player enters a single letter
        guess = get_guess(guessed_letters)

        # add guess to guessed letters
        guessed_letters.append(guess)

        # check if guess is in word
        if guess in word:
            # add guess to guessed word
            guessed_word = update_guess(word, guessed_word, guess)
        else:
            # increment wrong guesses
            wrong_guesses += 1


def hangman():
    """The hangman game."""
    try:
        # game outer loop
        while True:

            play_round()

            play_again = input("Play again? (y/n): ").lower()
            if play_again != "y":
                break

        print("\nGoodbye!")

    except KeyboardInterrupt:
        print("\nGoodbye!")
        exit()


# Main
if __name__ == "__main__":
    splash_screen()
    hangman()
