import random

# ============================================================
# PYTHON STRING MANIPULATION EXERCISE
# Topics: User Input, Conditionals, Loops, String Operations
# ============================================================

print("=" * 50)
print("STRING VALIDATOR & BUILDER")
print("=" * 50)

# Step 1: Ask for User Input
user_string = input("\nEnter a string (exactly 10 characters): ")

# Step 2: Check the Length of the String
string_length = len(user_string)

if string_length < 10:
    print("\n❌ String not long enough.")
    
elif string_length > 10:
    print("\n❌ String too long.")
    
else:
    # Step 3: Perfect string - Print First and Last Characters
    print("\n✅ Perfect string!")
    print(f"First character: '{user_string[0]}'")
    print(f"Last character: '{user_string[-1]}'")
    
    # Step 4: Build the String Character by Character
    print("\n📈 Building string character by character:")
    print("-" * 30)
    
    built_string = ""
    for i, char in enumerate(user_string):
        built_string += char
        print(f"Step {i + 1}: {built_string}")
    
    print("-" * 30)
    print(f"Final result: {built_string}")
    
    # Step 5: Bonus - Jumble the String
    print("\n🎲 BONUS: Jumbled version:")
    char_list = list(user_string)           # Convert string to list
    random.shuffle(char_list)               # Shuffle the list
    jumbled_string = "".join(char_list)     # Join back to string
    print(f"Jumbled: {jumbled_string}")

print("\n" + "=" * 50)
print("Program completed!")
print("=" * 50)