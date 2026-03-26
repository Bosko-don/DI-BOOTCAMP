import json
import random


# ============================================
# EXERCISE 1: RANDOM SENTENCE GENERATOR
# ============================================

def get_words_from_file(file_path):
    """Read words from a file and return as a list."""
    try:
        with open(file_path, "r") as file:
            content = file.read()
            words = content.split()
            return words
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        return []
    except Exception as e:
        print(f"Error reading file: {e}")
        return []


def get_random_sentence(length, file_path="words.txt"):
    """Generate a random sentence of specified length."""
    words = get_words_from_file(file_path)
    
    if not words:
        return "Error: Could not load words."
    
    # Select random words
    selected_words = [random.choice(words) for _ in range(length)]
    
    # Create sentence (lowercase, join with spaces)
    sentence = " ".join(selected_words).lower()
    
    # Capitalize first letter and add period
    sentence = sentence[0].upper() + sentence[1:] + "."
    
    return sentence


def main_exercise1():
    """Main function for Exercise 1."""
    print("=" * 50)
    print("RANDOM SENTENCE GENERATOR")
    print("=" * 50)
    print("This program generates a random sentence from a word list.")
    print("Sentence length must be between 2 and 20 words.\n")
    
    # Get user input
    try:
        length = input("Enter sentence length (2-20): ").strip()
        length = int(length)
        
        # Validate input
        if length < 2 or length > 20:
            print("Error: Length must be between 2 and 20.")
            return
        
        # Generate and print sentence
        sentence = get_random_sentence(length)
        print(f"\nGenerated sentence: {sentence}")
        
    except ValueError:
        print("Error: Please enter a valid integer.")
    except Exception as e:
        print(f"An error occurred: {e}")


# ============================================
# EXERCISE 2: WORKING WITH JSON
# ============================================

def main_exercise2():
    """Main function for Exercise 2."""
    print("\n" + "=" * 50)
    print("WORKING WITH JSON")
    print("=" * 50)
    
    # Sample JSON string
    sampleJson = """{ 
       "company":{ 
          "employee":{ 
             "name":"emma",
             "payable":{ 
                "salary":7000,
                "bonus":800
             }
          }
       }
    }"""
    
    # Step 1: Load JSON string
    data = json.loads(sampleJson)
    print("JSON loaded successfully.")
    
    # Step 2: Access nested "salary" key
    salary = data["company"]["employee"]["payable"]["salary"]
    print(f"Employee salary: ${salary}")
    
    # Step 3: Add "birth_date" key
    data["company"]["employee"]["birth_date"] = "1995-03-15"
    print("Added birth_date: 1995-03-15")
    
    # Step 4: Save to file
    with open("employee_data.json", "w") as file:
        json.dump(data, file, indent=4)
    
    print("Modified JSON saved to 'employee_data.json'")
    
    # Display the result
    print("\n--- Final JSON ---")
    print(json.dumps(data, indent=4))


# ============================================
# CREATE SAMPLE WORDS FILE (if needed)
# ============================================

def create_sample_words_file():
    """Create a sample words.txt file if it doesn't exist."""
    sample_words = """apple banana cherry date elderberry fig grape honeydew 
kiwi lemon mango nectarine orange papaya quince raspberry strawberry 
tangerine watermelon apricot blueberry coconut dragonfruit grapefruit 
avocado blackcurrant cranberry durian elderberry feijoa guava"""
    
    try:
        with open("words.txt", "x") as file:
            file.write(sample_words)
            print("Created sample 'words.txt' file.")
    except FileExistsError:
        pass  # File already exists


# ============================================
# MAIN PROGRAM
# ============================================

if __name__ == "__main__":
    # Create sample words file if needed
    create_sample_words_file()
    
    # Run Exercise 1
    main_exercise1()
    
    # Run Exercise 2
    main_exercise2()
    
    print("\n" + "=" * 50)
    print("ALL EXERCISES COMPLETED!")
    print("=" * 50)