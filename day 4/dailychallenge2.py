import string
import re
from collections import Counter


# ============================================
# PART I & II: TEXT CLASS
# ============================================

class Text:
    def __init__(self, text):
        self.text = text
    
    def word_frequency(self, word):
        """Count occurrences of a specific word."""
        words = self.text.lower().split()
        count = words.count(word.lower())
        return count if count > 0 else None
    
    def most_common_word(self):
        """Find the most frequently occurring word."""
        words = self.text.lower().split()
        if not words:
            return None
        
        word_counts = Counter(words)
        most_common = word_counts.most_common(1)[0]
        return most_common[0]
    
    def unique_words(self):
        """Return list of unique words."""
        words = self.text.lower().split()
        return list(set(words))
    
    @classmethod
    def from_file(cls, file_path):
        """Create Text instance from file."""
        try:
            with open(file_path, 'r') as file:
                content = file.read()
            return cls(content)
        except FileNotFoundError:
            print(f"Error: File '{file_path}' not found.")
            return None
        except Exception as e:
            print(f"Error reading file: {e}")
            return None
    
    def __str__(self):
        preview = self.text[:100] + "..." if len(self.text) > 100 else self.text
        return f"Text: {preview}"


# ============================================
# BONUS: TEXT MODIFICATION CLASS
# ============================================

class TextModification(Text):
    # Common English stop words
    STOP_WORDS = {
        'a', 'an', 'the', 'is', 'are', 'was', 'were', 'be', 'been', 'being',
        'have', 'has', 'had', 'do', 'does', 'did', 'will', 'would', 'could',
        'should', 'may', 'might', 'must', 'shall', 'can', 'need', 'dare',
        'ought', 'used', 'to', 'of', 'in', 'for', 'on', 'with', 'at', 'by',
        'from', 'as', 'into', 'through', 'during', 'before', 'after', 'above',
        'below', 'between', 'under', 'again', 'further', 'then', 'once',
        'here', 'there', 'when', 'where', 'why', 'how', 'all', 'each', 'few',
        'more', 'most', 'other', 'some', 'such', 'no', 'nor', 'not', 'only',
        'own', 'same', 'so', 'than', 'too', 'very', 'just', 'and', 'but',
        'if', 'or', 'because', 'until', 'while', 'this', 'that', 'these',
        'those', 'i', 'me', 'my', 'myself', 'we', 'our', 'ours', 'ourselves',
        'you', 'your', 'yours', 'yourself', 'yourselves', 'he', 'him', 'his',
        'himself', 'she', 'her', 'hers', 'herself', 'it', 'its', 'itself',
        'they', 'them', 'their', 'theirs', 'themselves', 'what', 'which',
        'who', 'whom', 'whose', 'whichever', 'whoever', 'whomever'
    }
    
    def remove_punctuation(self):
        """Remove all punctuation from text."""
        # Use string.punctuation for all punctuation characters
        translator = str.maketrans('', '', string.punctuation)
        clean_text = self.text.translate(translator)
        return clean_text
    
    def remove_stop_words(self):
        """Remove common stop words from text."""
        words = self.text.lower().split()
        filtered_words = [word for word in words if word not in self.STOP_WORDS]
        return ' '.join(filtered_words)
    
    def remove_special_characters(self):
        """Remove special characters using regex."""
        # Keep only alphanumeric and whitespace
        clean_text = re.sub(r'[^a-zA-Z0-9\s]', '', self.text)
        return clean_text
    
    def full_clean(self):
        """Apply all cleaning methods."""
        text = self.remove_punctuation()
        text = self.remove_special_characters()
        # Update text temporarily for stop word removal
        original = self.text
        self.text = text
        text = self.remove_stop_words()
        self.text = original
        return text


# ============================================
# DEMONSTRATION
# ============================================

def demo():
    print("=" * 60)
    print("TEXT ANALYSIS DEMONSTRATION")
    print("=" * 60)
    
    # Sample text for analysis
    sample_text = """
    A good book is the best of friends, the same today and forever.
    A book is a friend that never betrays. The best friend is a good book.
    Read a good book every day. Books are friends for life.
    """
    
    print("\n--- PART I: Basic Text Analysis ---")
    print(f"Sample text:\n{sample_text[:100]}...")
    
    # Create Text instance
    text = Text(sample_text)
    
    # Test word_frequency
    word = "book"
    freq = text.word_frequency(word)
    print(f"\n1. Word Frequency of '{word}': {freq}")
    
    # Test most_common_word
    common = text.most_common_word()
    print(f"2. Most Common Word: '{common}'")
    
    # Test unique_words
    unique = text.unique_words()
    print(f"3. Unique Words ({len(unique)} total): {unique[:10]}...")
    
    # Create sample file for Part II
    print("\n--- PART II: File Analysis ---")
    filename = "sample_text.txt"
    with open(filename, "w") as f:
        f.write(sample_text)
    print(f"Created '{filename}'")
    
    # Test from_file class method
    file_text = Text.from_file(filename)
    if file_text:
        print(f"Loaded from file: {file_text}")
        print(f"Most common word from file: '{file_text.most_common_word()}'")
    
    print("\n--- BONUS: Text Modification ---")
    dirty_text = "Hello!!! This is a test... with #special @characters and stop words."
    print(f"Original: {dirty_text}")
    
    mod = TextModification(dirty_text)
    
    print(f"\n1. Remove Punctuation: {mod.remove_punctuation()}")
    print(f"2. Remove Special Chars: {mod.remove_special_characters()}")
    print(f"3. Remove Stop Words: {mod.remove_stop_words()}")
    print(f"4. Full Clean: {mod.full_clean()}")
    
    # Advanced example
    print("\n--- Advanced Example ---")
    article = """
    The quick brown fox jumps over the lazy dog. The fox was very quick!
    Programming in Python is fun. Python is easy to learn and powerful.
    """
    mod_article = TextModification(article)
    
    print(f"Original:\n{article[:100]}...")
    print(f"\nMost common word: '{mod_article.most_common_word()}'")
    print(f"Unique words count: {len(mod_article.unique_words())}")
    
    cleaned = mod_article.full_clean()
    print(f"\nAfter full cleaning:\n{cleaned[:100]}...")
    
    # Create analysis report
    print("\n--- ANALYSIS REPORT ---")
    print(f"Total words: {len(article.split())}")
    print(f"Unique words: {len(set(article.lower().split()))}")
    print(f"Most common: '{mod_article.most_common_word()}'")
    print(f"Words after cleaning: {len(cleaned.split())}")
    
    # Cleanup
    import os
    os.remove(filename)
    print(f"\nCleaned up '{filename}'")


# ============================================
# INTERACTIVE MODE
# ============================================

def interactive():
    print("\n" + "=" * 60)
    print("INTERACTIVE TEXT ANALYZER")
    print("=" * 60)
    
    choice = input("\n1. Analyze text string\n2. Analyze file\nChoice: ").strip()
    
    if choice == "1":
        user_text = input("\nEnter your text: ")
        text_obj = TextModification(user_text)
    else:
        filepath = input("Enter file path: ")
        text_obj = TextModification.from_file(filepath)
        if not text_obj:
            return
    
    while True:
        print("\n--- Menu ---")
        print("1. Word frequency")
        print("2. Most common word")
        print("3. Unique words")
        print("4. Remove punctuation")
        print("5. Remove stop words")
        print("6. Remove special characters")
        print("7. Full clean")
        print("8. Exit")
        
        action = input("\nChoice: ").strip()
        
        if action == "1":
            word = input("Enter word to count: ")
            result = text_obj.word_frequency(word)
            print(f"Frequency: {result}")
        elif action == "2":
            print(f"Most common: '{text_obj.most_common_word()}'")
        elif action == "3":
            unique = text_obj.unique_words()
            print(f"Unique words ({len(unique)}): {unique[:20]}")
        elif action == "4":
            print(f"Result: {text_obj.remove_punctuation()}")
        elif action == "5":
            print(f"Result: {text_obj.remove_stop_words()}")
        elif action == "6":
            print(f"Result: {text_obj.remove_special_characters()}")
        elif action == "7":
            print(f"Result: {text_obj.full_clean()}")
        elif action == "8":
            break


# ============================================
# MAIN
# ============================================

if __name__ == "__main__":
    demo()
    
    # Uncomment for interactive mode:
    # interactive()
    
    print("\n" + "=" * 60)
    print("DEMONSTRATION COMPLETE!")
    print("=" * 60)