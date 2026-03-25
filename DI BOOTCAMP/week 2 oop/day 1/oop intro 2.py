# ============================================================
# PYTHON OOP EXERCISES
# Topics: Classes, Objects, Methods, Geometry, Data Structures
# ============================================================

import random
import math

print("=" * 60)
print("🌟 EXERCISE 1: Geometry - Circle Class")
print("=" * 60)

class Circle:
    def __init__(self, radius=1.0):
        self.radius = radius
    
    def perimeter(self):
        """Calculate and return the perimeter (circumference)"""
        return 2 * math.pi * self.radius
    
    def area(self):
        """Calculate and return the area"""
        return math.pi * (self.radius ** 2)
    
    def definition(self):
        """Print the geometrical definition of a circle"""
        print("A circle is a round plane figure whose boundary (the circumference) ")
        print("consists of points equidistant from a fixed point (the center).")

# Test Circle class
circle1 = Circle(5)
print(f"Circle with radius: {circle1.radius}")
print(f"Perimeter: {circle1.perimeter():.2f}")
print(f"Area: {circle1.area():.2f}")
print()
circle1.definition()

print("\nDefault circle (radius=1):")
circle2 = Circle()
print(f"Perimeter: {circle2.perimeter():.2f}")
print(f"Area: {circle2.area():.2f}")


print("\n" + "=" * 60)
print("🌟 EXERCISE 2: Custom List Class")
print("=" * 60)

class MyList:
    def __init__(self, letters):
        self.letters = letters
    
    def reverse(self):
        """Return the reversed list"""
        return self.letters[::-1]
    
    def sorted(self):
        """Return the sorted list"""
        return sorted(self.letters)
    
    def generate_random(self):
        """Bonus: Generate list of random numbers with same length"""
        return [random.randint(1, 100) for _ in range(len(self.letters))]

# Test MyList class
my_list = MyList(['d', 'a', 'c', 'b', 'e'])
print(f"Original list: {my_list.letters}")
print(f"Reversed: {my_list.reverse()}")
print(f"Sorted: {my_list.sorted()}")
print(f"Random numbers (bonus): {my_list.generate_random()}")


print("\n" + "=" * 60)
print("🌟 EXERCISE 3: Restaurant Menu Manager")
print("=" * 60)

class MenuManager:
    def __init__(self):
        # Initialize menu with default dishes
        self.menu = [
            {"name": "Soup", "price": 10, "spice": "B", "gluten": False},
            {"name": "Hamburger", "price": 15, "spice": "A", "gluten": True},
            {"name": "Salad", "price": 18, "spice": "A", "gluten": False},
            {"name": "French Fries", "price": 5, "spice": "C", "gluten": False},
            {"name": "Beef bourguignon", "price": 25, "spice": "B", "gluten": True}
        ]
    
    def add_item(self, name, price, spice, gluten):
        """Add a new dish to the menu"""
        # Check if dish already exists
        for dish in self.menu:
            if dish["name"].lower() == name.lower():
                print(f"❌ '{name}' is already on the menu!")
                return
        
        new_dish = {
            "name": name,
            "price": price,
            "spice": spice,
            "gluten": gluten
        }
        self.menu.append(new_dish)
        print(f"✅ '{name}' added to the menu!")
    
    def update_item(self, name, price, spice, gluten):
        """Update an existing dish"""
        for dish in self.menu:
            if dish["name"].lower() == name.lower():
                dish["price"] = price
                dish["spice"] = spice
                dish["gluten"] = gluten
                print(f"✅ '{name}' updated successfully!")
                return
        
        print(f"❌ '{name}' is not on the menu. Cannot update.")
    
    def remove_item(self, name):
        """Remove a dish from the menu"""
        for i, dish in enumerate(self.menu):
            if dish["name"].lower() == name.lower():
                removed = self.menu.pop(i)
                print(f"✅ '{name}' removed from the menu!")
                print("Updated menu:")
                self.display_menu()
                return
        
        print(f"❌ '{name}' is not on the menu. Cannot remove.")
    
    def display_menu(self):
        """Display all dishes in the menu"""
        print(f"\n{'='*50}")
        print(f"{'NAME':<20} {'PRICE':<8} {'SPICE':<8} {'GLUTEN':<8}")
        print("-" * 50)
        for dish in self.menu:
            gluten_status = "Yes" if dish["gluten"] else "No"
            print(f"{dish['name']:<20} ${dish['price']:<7} {dish['spice']:<8} {gluten_status:<8}")
        print(f"{'='*50}")

# Test MenuManager
manager = MenuManager()
print("Initial menu:")
manager.display_menu()

# Add new item
manager.add_item("Pizza", 20, "C", True)

# Try to add duplicate
manager.add_item("Soup", 12, "A", False)

# Update existing item
manager.update_item("Salad", 20, "A", False)

# Try to update non-existent item
manager.update_item("Pasta", 18, "B", True)

# Remove item
manager.remove_item("French Fries")

# Try to remove non-existent item
manager.remove_item("Sushi")

print("\nFinal menu:")
manager.display_menu()


print("\n" + "=" * 60)
print("ALL EXERCISES COMPLETED! 🎉")
print("=" * 60)