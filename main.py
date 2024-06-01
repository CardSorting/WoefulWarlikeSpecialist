import random

def hangman():
    words = ['python', 'java', 'kotlin', 'javascript']
    word = random.choice(words)
    guessed_word = ['_'] * len(word)
    attempts = 6
    guessed_letters = set()

    print("Welcome to Hangman!")
    print(" ".join(guessed_word))

    while attempts > 0 and ''.join(guessed_word) != word:
        guess = input("Guess a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
            continue

        if guess in guessed_letters:
            print("You have already guessed that letter.")
            continue

        guessed_letters.add(guess)

        if guess in word:
            for i, letter in enumerate(word):
                if letter == guess:
                    guessed_word[i] = guess
            print("Good guess!")
        else:
            attempts -= 1
            print(f"Wrong guess! You have {attempts} attempts left.")

        print(" ".join(guessed_word))

    if ''.join(guessed_word) == word:
        print("Congratulations, you won!")
    else:
        print(f"Sorry, you lost. The word was '{word}'.")

if __name__ == "__main__":
    hangman()