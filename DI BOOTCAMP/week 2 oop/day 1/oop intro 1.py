# ============================================================
# PYTHON OOP EXERCISES
# Topics: Classes, Objects, Methods, Attributes, Inheritance
# ============================================================

print("=" * 60)
print("🌟 EXERCISE 1: Cats")
print("=" * 60)

class Cat:
    def __init__(self, cat_name, cat_age):
        self.name = cat_name
        self.age = cat_age

# Step 1: Create cat objects
cat1 = Cat("Whiskers", 3)
cat2 = Cat("Mittens", 7)
cat3 = Cat("Shadow", 5)

# Step 2: Create function to find oldest cat
def find_oldest_cat(*cats):
    oldest = cats[0]
    for cat in cats:
        if cat.age > oldest.age:
            oldest = cat
    return oldest

# Step 3: Print oldest cat's details
oldest = find_oldest_cat(cat1, cat2, cat3)
print(f"The oldest cat is {oldest.name}, and is {oldest.age} years old.")


print("\n" + "=" * 60)
print("🌟 EXERCISE 2: Dogs")
print("=" * 60)

class Dog:
    def __init__(self, name, height):
        self.name = name
        self.height = height
    
    def bark(self):
        print(f"{self.name} goes woof!")
    
    def jump(self):
        print(f"{self.name} jumps {self.height * 2} cm high!")

# Create dog objects
davids_dog = Dog("Rex", 50)
sarahs_dog = Dog("Teacup", 20)

# Print details and call methods
print(f"David's dog: {davids_dog.name}, {davids_dog.height} cm")
davids_dog.bark()
davids_dog.jump()

print(f"\nSarah's dog: {sarahs_dog.name}, {sarahs_dog.height} cm")
sarahs_dog.bark()
sarahs_dog.jump()

# Compare dog sizes
if davids_dog.height > sarahs_dog.height:
    print(f"\n{davids_dog.name} is bigger!")
else:
    print(f"\n{sarahs_dog.name} is bigger!")


print("\n" + "=" * 60)
print("🌟 EXERCISE 3: Who's the Song Producer?")
print("=" * 60)

class Song:
    def __init__(self, lyrics):
        self.lyrics = lyrics
    
    def sing_me_a_song(self):
        for line in self.lyrics:
            print(line)

# Create song object
stairway = Song(["There's a lady who's sure", 
                 "all that glitters is gold", 
                 "and she's buying a stairway to heaven"])

stairway.sing_me_a_song()


print("\n" + "=" * 60)
print("🌟 EXERCISE 4: Afternoon at the Zoo")
print("=" * 60)

class Zoo:
    def __init__(self, zoo_name):
        self.name = zoo_name
        self.animals = []
        self.grouped_animals = {}
    
    def add_animal(self, *new_animals):
        """Add one or more animals to the zoo"""
        for animal in new_animals:
            if animal not in self.animals:
                self.animals.append(animal)
                print(f"Added {animal}")
            else:
                print(f"{animal} is already in the zoo!")
    
    def get_animals(self):
        """Print all animals in the zoo"""
        print(f"\nAnimals in {self.name}:")
        if self.animals:
            for animal in self.animals:
                print(f"  - {animal}")
        else:
            print("  (No animals yet)")
    
    def sell_animal(self, animal_sold):
        """Remove an animal from the zoo"""
        if animal_sold in self.animals:
            self.animals.remove(animal_sold)
            print(f"Sold {animal_sold}")
        else:
            print(f"{animal_sold} is not in the zoo!")
    
    def sort_animals(self):
        """Sort animals and group by first letter"""
        self.animals.sort()
        self.grouped_animals = {}
        
        for animal in self.animals:
            first_letter = animal[0].upper()
            if first_letter not in self.grouped_animals:
                self.grouped_animals[first_letter] = []
            self.grouped_animals[first_letter].append(animal)
        
        return self.grouped_animals
    
    def get_groups(self):
        """Print grouped animals"""
        if not self.grouped_animals:
            self.sort_animals()
        
        print(f"\nAnimal groups in {self.name}:")
        for letter, animals in sorted(self.grouped_animals.items()):
            print(f"  {letter}: {animals}")

# Create zoo and test methods
brooklyn_safari = Zoo("Brooklyn Safari")

# Add animals using *args (bonus)
brooklyn_safari.add_animal("Giraffe", "Bear", "Baboon", "Cat", "Cougar", "Lion", "Zebra")

# Display animals
brooklyn_safari.get_animals()

# Sell an animal
brooklyn_safari.sell_animal("Bear")
brooklyn_safari.get_animals()

# Sort and group
brooklyn_safari.sort_animals()
brooklyn_safari.get_groups()

# Try to add duplicate
brooklyn_safari.add_animal("Lion")


print("\n" + "=" * 60)
print("ALL EXERCISES COMPLETED! 🎉")
print("=" * 60)