def computer_guesses_number():
    print("Socho ek number 1 se 100 ke beech... main usay guess karunga!")

    low = 1
    high = 100
    attempts = 0

    while low <= high:
        guess = (low + high) // 2
        attempts += 1
        print(f"Computer guesses: {guess}")
        feedback = input("Batao: (H)igh, (L)ow, (C)orrect? ").lower()

        if feedback == 'c':
            print(f"🎉 Yay! I guessed your number {guess} in {attempts} tries.")
            break
        elif feedback == 'h':
            high = guess - 1
        elif feedback == 'l':
            low = guess + 1
        else:
            print("⛔ Invalid input. Please enter H, L, or C.")

# Run the game
computer_guesses_number()
