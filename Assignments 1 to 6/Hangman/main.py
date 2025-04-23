import random

def hangman():
    words = ['python', 'developer', 'streamlit', 'hangman', 'programming']
    word = random.choice(words)
    guessed_letters = []
    tries = 6

    print("Welcome to Hangman!")
    
    while tries > 0:
        display_word = ''
        for letter in word:
            if letter in guessed_letters:
                display_word += letter + ' '
            else:
                display_word += '_ '
        
        print("\nWord:", display_word.strip())
        print(f"You have {tries} tries left.")
        
        guess = input("Guess a letter: ").lower()

        if guess in guessed_letters:
            print("You already guessed that letter.")
            continue

        if guess in word:
            print("Good guess!")
            guessed_letters.append(guess)
        else:
            print("Wrong guess.")
            tries -= 1
            guessed_letters.append(guess)

        if all(letter in guessed_letters for letter in word):
            print(f"\nCongratulations! You guessed the word: {word}")
            break

    else:
        print(f"\nYou ran out of tries. The word was: {word}")

# Run the game
hangman()
