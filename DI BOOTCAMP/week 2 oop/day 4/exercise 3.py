import json
import re
import random


# ============================================
# EXERCISE 1: RESTAURANT MENU MANAGER - REGEX
# ============================================

class ValentineMenuManager:
    def __init__(self, filename="restaurant_menu.json"):
        self.filename = filename
        self.load_menu()
    
    def load_menu(self):
        try:
            with open(self.filename, "r") as file:
                self.menu = json.load(file)
        except FileNotFoundError:
            self.menu = {"items": [], "valentine_specials": []}
    
    def save_menu(self):
        with open(self.filename, "w") as file:
            json.dump(self.menu, file, indent=4)
    
    def validate_item_name(self, name):
        """Validate name: starts with V, each word capitalized except connectors, at least 2 'e', no numbers"""
        # Check starts with capital V
        if not name.startswith("V"):
            return False, "Name must start with capital 'V'"
        
        # Check no numbers
        if re.search(r'\d', name):
            return False, "Name cannot contain numbers"
        
        # Check at least 2 'e' (case insensitive)
        if len(re.findall(r'e', name, re.IGNORECASE)) < 2:
            return False, "Name must contain at least 2 'e'"
        
        # Check word capitalization (connector words in lowercase)
        words = name.split()
        connectors = ["of", "the", "and", "with", "in", "on", "at", "to", "for"]
        
        for i, word in enumerate(words):
            if i == 0:  # First word must start with V (already checked)
                if not re.match(r'^V[a-z]+$', word):
                    return False, "First word must be capitalized properly (e.g., 'Vegetable')"
            else:
                # Connector words lowercase, others capitalized
                clean_word = word.strip("-")
                if clean_word.lower() in connectors:
                    if not clean_word.islower():
                        return False, f"Connector word '{clean_word}' must be lowercase"
                else:
                    if not re.match(r'^[A-Z][a-z]+(-[A-Za-z]+)?$', word):
                        return False, f"Word '{word}' must be capitalized"
        
        return True, "Valid"
    
    def validate_price(self, price):
        """Validate price pattern: XX,14"""
        pattern = r'^\d{2},14$'
        if re.match(pattern, price):
            return True
        return False
    
    def add_valentine_item(self, name, price):
        is_valid_name, msg = self.validate_item_name(name)
        if not is_valid_name:
            return False, f"Invalid name: {msg}"
        
        if not self.validate_price(price):
            return False, "Invalid price. Must match pattern: XX,14 (e.g., 25,14)"
        
        # Convert price format for storage
        price_float = float(price.replace(",", "."))
        
        item = {"name": name, "price": price_float}
        self.menu["valentine_specials"].append(item)
        self.save_menu()
        return True, "Item added successfully!"
    
    def display_heart(self):
        """Display a heart made of stars"""
        heart = """
        **   **
      ******* *******
    *******************
     *****************
       *************
         *********
           *****
             ***
              *
        """
        print(heart)
    
    def show_menu(self):
        self.display_heart()
        print("\n=== VALENTINE'S DAY SPECIALS ===")
        if not self.menu["valentine_specials"]:
            print("No specials yet!")
        else:
            for item in self.menu["valentine_specials"]:
                print(f"❤️  {item['name']} - ${item['price']}")


def run_exercise1():
    print("=" * 60)
    print("EXERCISE 1: VALENTINE'S DAY MENU MANAGER")
    print("=" * 60)
    
    manager = ValentineMenuManager()
    
    while True:
        print("\n1. Add Valentine Item")
        print("2. Show Menu")
        print("3. Exit")
        
        choice = input("\nChoose (1-3): ").strip()
        
        if choice == "1":
            print("\nRules:")
            print("- Name starts with 'V', each word capitalized (connectors lowercase)")
            print("- At least 2 'e' in name, no numbers")
            print("- Price format: XX,14 (e.g., 25,14)")
            
            name = input("\nEnter item name: ").strip()
            price = input("Enter price (XX,14): ").strip()
            
            success, msg = manager.add_valentine_item(name, price)
            print(f"\n{'✓' if success else '✗'} {msg}")
            
        elif choice == "2":
            manager.show_menu()
            
        elif choice == "3":
            print("Goodbye!")
            break


# ============================================
# EXERCISE 2: DUNGEONS & DRAGONS
# ============================================

class Character:
    ATTRIBUTES = ["Strength", "Dexterity", "Constitution", 
                  "Intelligence", "Wisdom", "Charisma"]
    
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.stats = self.generate_stats()
    
    def roll_stat(self):
        """Roll 4d6, drop lowest, sum rest"""
        rolls = [random.randint(1, 6) for _ in range(4)]
        rolls.sort(reverse=True)
        return sum(rolls[:3])  # Sum top 3
    
    def generate_stats(self):
        """Generate all 6 stats"""
        return {attr: self.roll_stat() for attr in self.ATTRIBUTES}
    
    def get_modifier(self, stat_value):
        """Calculate ability modifier"""
        return (stat_value - 10) // 2
    
    def to_dict(self):
        return {
            "name": self.name,
            "age": self.age,
            "stats": self.stats
        }
    
    def __str__(self):
        lines = [
            f"Character: {self.name}",
            f"Age: {self.age}",
            "-" * 30,
            "STATS:",
        ]
        for attr, value in self.stats.items():
            mod = self.get_modifier(value)
            mod_str = f"+{mod}" if mod >= 0 else str(mod)
            lines.append(f"  {attr:12}: {value:2} (Modifier: {mod_str})")
        return "\n".join(lines)


class Game:
    def __init__(self):
        self.characters = []
    
    def create_characters(self):
        num_players = int(input("How many players? "))
        
        for i in range(num_players):
            print(f"\n--- Player {i+1} ---")
            name = input("Character name: ").strip()
            age = input("Character age: ").strip()
            
            char = Character(name, age)
            self.characters.append(char)
            print(f"\n{char}\n")
    
    def export_txt(self, filename="characters.txt"):
        with open(filename, "w") as file:
            file.write("=" * 50 + "\n")
            file.write("   DUNGEONS & DRAGONS - CHARACTER SHEETS\n")
            file.write("=" * 50 + "\n\n")
            
            for char in self.characters:
                file.write(str(char))
                file.write("\n\n" + "=" * 50 + "\n\n")
        
        print(f"✓ Exported to {filename}")
    
    def export_json(self, filename="characters.json"):
        data = [char.to_dict() for char in self.characters]
        
        with open(filename, "w") as file:
            json.dump(data, file, indent=4)
        
        print(f"✓ Exported to {filename}")


def run_exercise2():
    print("\n" + "=" * 60)
    print("EXERCISE 2: DUNGEONS & DRAGONS CHARACTER GENERATOR")
    print("=" * 60)
    
    game = Game()
    game.create_characters()
    
    print("\n--- Exporting Characters ---")
    game.export_txt()
    game.export_json()


# ============================================
# MAIN PROGRAM
# ============================================

if __name__ == "__main__":
    run_exercise1()
    run_exercise2()
    
    print("\n" + "=" * 60)
    print("ALL EXERCISES COMPLETED!")
    print("=" * 60)