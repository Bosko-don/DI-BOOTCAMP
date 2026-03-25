# ============================================================
# PYTHON CHALLENGES
# Topics: Basics, Loops, Lists, Strings, Input/Output
# ============================================================

print("=" * 60)
print("🎯 CHALLENGE 1: Multiples of a Number")
print("=" * 60)

# Get user inputs
try:
    number = int(input("Enter a number: "))
    length = int(input("Enter the length of the list: "))
    
    # Generate multiples using list comprehension
    multiples = [number * i for i in range(1, length + 1)]
    
    print(f"\nMultiples of {number} (length {length}):")
    print(multiples)
    
except ValueError:
    print("❌ Please enter valid integers!")


print("\n" + "=" * 60)
print("🎯 CHALLENGE 2: Remove Consecutive Duplicate Letters")
print("=" * 60)

# Get user string
user_word = input("Enter a word: ")

# Remove consecutive duplicates
if len(user_word) == 0:
    result = ""
else:
    result = user_word[0]  # Start with first character
    
    for i in range(1, len(user_word)):
        # Only add character if it's different from the previous one
        if user_word[i] != user_word[i - 1]:
            result += user_word[i]

print(f"\nOriginal: '{user_word}'")
print(f"Cleaned:  '{result}'")


print("\n" + "=" * 60)
print("ALL CHALLENGES COMPLETED! 🎉")
print("=" * 60)