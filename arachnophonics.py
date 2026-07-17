import random

def play_game():
    # 1. Setup our word bank and game variables
    words = ["pixel", "render", "compile", "module", "iterate", "python"]
    secret_word = random.choice(words)
    
    correct_guesses = []
    incorrect_guesses = []
    max_tries = 6
    
    print("==================================")
    print("    Welcome to ArachnoPhonics!    ")
    print("==================================")
    
    # 2. Main game loop
    while len(incorrect_guesses) < max_tries:
        # Build the visual display (e.g., _ _ t _ o n)
        display_word = ""
        for letter in secret_word:
            if letter in correct_guesses:
                display_word += letter + " "
            else:
                display_word += "_ "
        
        print(f"\nWord to guess: {display_word}")
        print(f"Incorrect guesses ({len(incorrect_guesses)}/{max_tries}): {incorrect_guesses}")
        
        # Check if the player won
        if "_" not in display_word:
            print("\n🎉 You won! You uncovered the word!")
            return
            
        # Get player input
        guess = input("Guess a letter: ").lower().strip()
        
        # Validate input
        if len(guess) != 1 or not guess.isalpha():
            print("❌ Please enter exactly one letter.")
            continue
            
        if guess in correct_guesses or guess in incorrect_guesses:
            print("⚠️ You already guessed that letter!")
            continue
            
        # Process the guess
        if guess in secret_word:
            print("✅ Correct!")
            correct_guesses.append(guess)
        else:
            print("❌ Wrong! The spider gets closer...")
            incorrect_guesses.append(guess)
            
    # 3. Game over condition if the loop finishes
    print(f"\n💥 Game Over! The spider caught you. The word was: {secret_word}")

# Start the game
play_game()