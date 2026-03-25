#!/usr/bin/env python3
"""
FRENCH TO ENGLISH TRANSLATOR
Using googletrans module
"""

from googletrans import Translator

print("=" * 60)
print("🇫🇷 FRENCH TO ENGLISH TRANSLATOR")
print("=" * 60)

# French words to translate
french_words = ["Bonjour", "Au revoir", "Bienvenue", "A bientôt"]

# Create translator instance
translator = Translator()

# Create dictionary to store translations
translations = {}

print("\nTranslating French words...\n")

for word in french_words:
    try:
        # Translate from French (fr) to English (en)
        result = translator.translate(word, src='fr', dest='en')
        
        # Store in dictionary
        translations[word] = result.text
        
        print(f"🇫🇷 {word:<15} → 🇬🇧 {result.text}")
        
    except Exception as e:
        print(f"❌ Error translating '{word}': {e}")
        translations[word] = "Translation failed"

# Final result
print("\n" + "=" * 60)
print("📋 FINAL DICTIONARY:")
print("=" * 60)
print(translations)

# Pretty print format
print(f"\nPretty format:")
print(f" french_words = {french_words}")
print(f" translations   = {list(translations.values())}")
print(f" dictionary     = {translations}")