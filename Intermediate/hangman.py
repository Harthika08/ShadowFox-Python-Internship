import random
words = {
    "PYTHON": "A popular programming language",
    "JAVA": "A programming language named after coffee",
    "COMPUTER": "An electronic device used for processing data",
    "PROGRAMMING": "The process of writing instructions for a computer",
    "INTERNET": "A global network connecting computers"
}
hangman_stages = [
    """
     +---+
     |   |
         |
         |
         |
    =========
    """,
    """
     +---+
     |   |
     O   |
         |
         |
    =========
    """,
    """
     +---+
     |   |
     O   |
     |   |
         |
    =========
    """,
    """
     +---+
     |   |
     O   |
    /|   |
         |
    =========
    """,
    """
     +---+
     |   |
     O   |
    /|\\  |
         |
    =========
    """,
    """
     +---+
     |   |
     O   |
    /|\\  |
    /    |
    =========
    """,
    """
     +---+
     |   |
     O   |
    /|\\  |
    / \\  |
    =========
    """
]
def display_word(secret_word,guessed_letters):
    display = ""
    
    for letter in secret_word:
        if letter in guessed_letters:
            display += letter + " "
        else:
            display += "_ "
    print("\nword:",display)

def play_game():
    secret_word = random.choice(list(words.keys()))
    guessed_letters = []
    wrong_guesses = 0
    max_attempts = 6
    
    print("\n-----HANGMAN GAME-----")
    print("Guess the hidden word one letter at a time")
    print("Enter '?' if you need a hint")
    
    print("\nHint:",words[secret_word])
    while wrong_guesses < max_attempts:
        print(hangman_stages[wrong_guesses])
        display_word(secret_word,guessed_letters)
        
        print("Wrong attempts remaining:",max_attempts - wrong_guesses)
        
        guess = input("\nEnter a letter or ?:").strip().upper()
        
        if guess == "?":
            print("Hint:",words[secret_word])
            continue
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter only one alphabet letter.")
            continue

        # Check repeated guesses
        if guess in guessed_letters:
            print("You already guessed that letter!")
            continue

        guessed_letters.append(guess)

        # Correct guess
        if guess in secret_word:
            print("Correct guess!")
        else:
            print("Wrong guess!")
            wrong_guesses += 1

        # Check win condition
        if all(letter in guessed_letters for letter in secret_word):
            print("\nCongratulations! You guessed the word:", secret_word)
            return

    # Player loses
    print(hangman_stages[wrong_guesses])
    print("\nGame Over!")
    print("The correct word was:", secret_word)


# Main program: replay option
while True:

    play_game()

    choice = input("\nDo you want to play again? (yes/no): ").strip().lower()

    if choice != "yes":
        print("\nThank you for playing Hangman!")
        break
    