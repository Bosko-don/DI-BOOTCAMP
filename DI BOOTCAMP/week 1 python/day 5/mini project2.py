# ============================================================
# PYTHON CHALLENGES
# Topics: String Manipulation, Lists, Sorting, Functions
# ============================================================

print("=" * 60)
print("🎯 CHALLENGE 1: Sorting")
print("=" * 60)

def sort_words():
    """Sort comma-separated words alphabetically"""
    # Step 1: Get input
    user_input = input("Enter words separated by commas: ")
    
    # Step 2: Split the string into a list
    words = user_input.split(",")
    
    # Step 3: Sort the list
    words.sort()
    
    # Step 4: Join back into comma-separated string
    result = ",".join(words)
    
    # Step 5: Print result
    print(f"Sorted: {result}")

# Run challenge 1
sort_words()


print("\n" + "=" * 60)
print("🎯 CHALLENGE 2: Longest Word")
print("=" * 60)

def longest_word(sentence):
    """
    Find and return the longest word in a sentence.
    Punctuation is considered part of the word.
    """
    # Step 2: Split sentence into words
    words = sentence.split()
    
    # Step 3: Initialize variables
    longest = ""
    
    # Step 4 & 5: Iterate and compare
    for word in words:
        if len(word) > len(longest):
            longest = word
    
    # Step 6: Return result
    return longest

# Test cases
test_sentences = [
    "Margaret's toy is a pretty doll.",
    "A thing of beauty is a joy forever.",
    "Forgetfulness is by all means powerless!"
]

print("Test results:")
for sentence in test_sentences:
    result = longest_word(sentence)
    print(f"  '{sentence}'")
    print(f"    → Longest word: '{result}' (length: {len(result)})\n")

# Interactive version
user_sentence = input("Enter your own sentence: ")
user_result = longest_word(user_sentence)
print(f"Longest word: '{user_result}'")


print("\n" + "=" * 60)
print("ALL CHALLENGES COMPLETED! 🎉")
print("=" * 60)