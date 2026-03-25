# ============================================================
# OLD MACDONALD'S FARM
# Topics: Classes, Dictionaries, String Formatting, Methods
# ============================================================

class Farm:
    def __init__(self, farm_name):
        """Initialize farm with name and empty animals dictionary"""
        self.name = farm_name
        self.animals = {}
    
    def add_animal(self, animal_type, count=1):
        """Add animal(s) to the farm"""
        if animal_type in self.animals:
            self.animals[animal_type] += count
        else:
            self.animals[animal_type] = count
    
    def add_animals(self, **kwargs):
        """Bonus: Add multiple animals using **kwargs"""
        for animal_type, count in kwargs.items():
            self.add_animal(animal_type, count)
    
    def get_info(self):
        """Return formatted string with farm info"""
        info = f"{self.name}'s farm\n\n"
        
        for animal, count in self.animals.items():
            info += f"{animal} : {count}\n"
        
        info += "\n    E-I-E-I-0!"
        return info
    
    def get_animal_types(self):
        """Return sorted list of animal types"""
        return sorted(self.animals.keys())
    
    def get_short_info(self):
        """Return short description of farm with pluralized animals"""
        animal_types = self.get_animal_types()
        
        if not animal_types:
            return f"{self.name}'s farm has no animals."
        
        # Pluralize animal names (add 's' if count > 1)
        pluralized = []
        for animal in animal_types:
            if self.animals[animal] > 1:
                pluralized.append(animal + "s")
            else:
                pluralized.append(animal)
        
        # Format the list with commas and 'and'
        if len(pluralized) == 1:
            animals_str = pluralized[0]
        elif len(pluralized) == 2:
            animals_str = f"{pluralized[0]} and {pluralized[1]}"
        else:
            animals_str = ", ".join(pluralized[:-1]) + f" and {pluralized[-1]}"
        
        return f"{self.name}'s farm has {animals_str}."


# ============================================================
# TESTING THE CODE
# ============================================================

print("=" * 60)
print("🚜 OLD MACDONALD'S FARM - TESTING")
print("=" * 60)

# Test basic functionality
print("\n--- Basic Test ---")
macdonald = Farm("McDonald")
macdonald.add_animal('cow', 5)
macdonald.add_animal('sheep')
macdonald.add_animal('sheep')
macdonald.add_animal('goat', 12)
print(macdonald.get_info())

# Test get_animal_types (bonus)
print("\n--- Animal Types (Sorted) ---")
print(f"Animal types: {macdonald.get_animal_types()}")

# Test get_short_info (bonus)
print("\n--- Short Info ---")
print(macdonald.get_short_info())

# Test **kwargs (bonus)
print("\n--- Adding Multiple Animals with **kwargs ---")
new_farm = Farm("Green Acres")
new_farm.add_animals(cow=5, sheep=2, goat=12, chicken=20)
print(new_farm.get_info())
print(new_farm.get_short_info())

# Test with single animal (no plural)
print("\n--- Single Animal Test ---")
small_farm = Farm("Tiny Farm")
small_farm.add_animal('horse', 1)
print(small_farm.get_short_info())

print("\n" + "=" * 60)
print("TESTING COMPLETED! 🎉")
print("=" * 60)