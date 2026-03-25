# ============================================================
# HANGMAN GAME IN PYTHON
# Topics: Conditionals, Loops, Functions, Modules, Strings
# ============================================================

import random

def display_hangman(tries):
    """Return the hangman ASCII art based on remaining tries"""
    stages = [
        # Final state: head, body, both arms, both legs
        """
           --------
           |      |
           |      O
           |     \\|/
           |      |
           |     / \\
           -
        """,
        # Head, body, both arms, one leg
        """
           --------
           |      |
           |      O
           |     \\|/
           |      |
           |     / 
           -
        """,
        # Head, body, both arms
        """
           --------
           |      |
           |      O
           |     \\|/
           |      |
           |      
           -
        """,
        # Head, body, one arm
        """
           --------
           |      |
           |      O
           |     \\|
           |      |
           |     
           -
        """,
        # Head and body
        """
           --------
           |      |
           |      O
           |      |
           |      |
           |     
           -
        """,
        # Head
        """
           --------
           |      |
           |      O
           |    
           |      
           |     
           -
        """,
        # Empty
        """
           --------
           |      |
           |      
           |    
           |      
           |     
           -
        """
    ]
    return stages[tries]

def play_hangman():
    """Main game function"""
    # Word list
    wordslist = ['correction', 'childish', 'beach', 'python', 'assertive', 
                 'interference', 'complete', 'share', 'credit card', 'rush', 'south']
    
    # Select random word
    word = random.choice(wordslist)
    
    # Game state
    word_letters = set(word.replace(" ", "").lower())  # Unique letters to guess
    guessed_letters = set()  # Letters already guessed
    tries = 6  # Number of wrong guesses allowed
    
    print("=" * 50)
    print("🎮 WELCOME TO HANGMAN! 🎮")
    print("=" * 50)
    print("Guess the word letter by letter.")
    print("You have 6 tries before the hangman is complete!")
    print(f"The word has {len(word.replace(' ', ''))} letters.\n")
    
    while tries > 0 and len(word_letters) > 0:
        # Display current hangman state
        print(display_hangman(tries))
        
        # Show guessed letters
        if guessed_letters:
            print(f"Letters guessed: {', '.join(sorted(guessed_letters))}")
        
        # Display current word progress
        word_display = ""
        for char in word:
            if char == " ":
                word_display += "  "
            elif char.lower() in guessed_letters:
                word_display += char + " "
            else:
                word_display += "_ "
        print(f"\nWord: {word_display}")
        
        # Get player guess
        guess = input("\nGuess a letter: ").strip().lower()
        
        # Validate input
        if len(guess) != 1 or not guess.isalpha():
            print("❌ Please enter a single letter!")
            continue
        
        # Check if already guessed
        if guess in guessed_letters:
            print(f"⚠️ You already guessed '{guess}'! Try another letter.")
            continue
        
        # Add to guessed letters
        guessed_letters.add(guess)
        
        # Check if in word
        if guess in word_letters:
            word_letters.remove(guess)
            print(f"✅ Good guess! '{guess}' is in the word.")
        else:
            tries -= 1
            print(f"❌ Wrong guess! '{guess}' is not in the word.")
            print(f"Tries remaining: {tries}")
    
    # Game over
    print(display_hangman(tries))
    print("=" * 50)
    
    if len(word_letters) == 0:
        print("🎉 CONGRATULATIONS! You guessed the word! 🎉")
    else:
        print("💀 GAME OVER! The hangman is complete! 💀")
        print(f"The word was: '{word}'")
    
    print("=" * 50)
    
    # Play again
    play_again = input("\nPlay again? (y/n): ").strip().lower()
    if play_again == 'y':
        play_hangman()
    else:
        print("Thanks for playing! Goodbye! 👋")

# Start the game
if __name__ == "__main__":
    play_hangman()