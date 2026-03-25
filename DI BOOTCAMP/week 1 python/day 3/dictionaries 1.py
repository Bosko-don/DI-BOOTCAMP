# ============================================================
# PYTHON DICTIONARY EXERCISES
# Topics: Dictionaries, Loops, Conditionals, Nested Structures
# ============================================================

print("=" * 60)
print("🌟 EXERCISE 1: Converting Lists into Dictionaries")
print("=" * 60)

keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]

# Method 1: Using zip() and dict()
result_dict = dict(zip(keys, values))
print(f"Using zip(): {result_dict}")

# Method 2: Using dictionary comprehension
result_dict2 = {k: v for k, v in zip(keys, values)}
print(f"Using comprehension: {result_dict2}")


print("\n" + "=" * 60)
print("🌟 EXERCISE 2: Cinemax #2")
print("=" * 60)

# Original family data
family = {"rick": 43, 'beth': 13, 'morty': 5, 'summer': 8}

total_cost = 0

print("Ticket prices for each family member:")
for name, age in family.items():
    if age < 3:
        price = 0
    elif 3 <= age <= 12:
        price = 10
    else:
        price = 15
    
    total_cost += price
    print(f"  {name.capitalize()} (age {age}): ${price}")

print(f"\nTotal cost for the family: ${total_cost}")

# BONUS: User input version
print("\n--- BONUS: Custom Family Input ---")
custom_family = {}

while True:
    name = input("Enter family member name (or 'done' to finish): ").strip().lower()
    if name == 'done':
        break
    
    try:
        age = int(input(f"Enter {name}'s age: "))
        custom_family[name] = age
    except ValueError:
        print("Please enter a valid age!")

# Calculate for custom family
if custom_family:
    custom_total = 0
    print("\nCustom family ticket prices:")
    for name, age in custom_family.items():
        if age < 3:
            price = 0
        elif 3 <= age <= 12:
            price = 10
        else:
            price = 15
        
        custom_total += price
        print(f"  {name.capitalize()} (age {age}): ${price}")
    
    print(f"\nTotal cost for custom family: ${custom_total}")


print("\n" + "=" * 60)
print("🌟 EXERCISE 3: Zara")
print("=" * 60)

# Create brand dictionary
brand = {
    "name": "Zara",
    "creation_date": 1975,
    "creator_name": "Amancio Ortega Gaona",
    "type_of_clothes": ["men", "women", "children", "home"],
    "international_competitors": ["Gap", "H&M", "Benetton"],
    "number_stores": 7000,
    "major_color": {
        "France": ["blue"],
        "Spain": ["red"],
        "US": ["pink", "green"]
    }
}

print("Original brand dictionary created")

# 1. Change number_stores to 2
brand["number_stores"] = 2
print(f"\n1. Updated number_stores: {brand['number_stores']}")

# 2. Print sentence about Zara's clients
clothes_types = ", ".join(brand["type_of_clothes"])
print(f"\n2. Zara serves clients interested in: {clothes_types}")

# 3. Add country_creation key
brand["country_creation"] = "Spain"
print(f"\n3. Added country_creation: {brand['country_creation']}")

# 4. Add Desigual to international_competitors if it exists
if "international_competitors" in brand:
    brand["international_competitors"].append("Desigual")
    print(f"\n4. Added Desigual to competitors")
    print(f"   Competitors: {brand['international_competitors']}")

# 5. Delete creation_date
del brand["creation_date"]
print(f"\n5. Deleted creation_date")

# 6. Print last international competitor
last_competitor = brand["international_competitors"][-1]
print(f"\n6. Last competitor: {last_competitor}")

# 7. Print major colors in US
us_colors = brand["major_color"]["US"]
print(f"\n7. Major colors in US: {us_colors}")

# 8. Print number of keys
num_keys = len(brand)
print(f"\n8. Number of keys: {num_keys}")

# 9. Print all keys
print(f"\n9. All keys: {list(brand.keys())}")

# BONUS: Merge with more_on_zara
print("\n--- BONUS: Merging Dictionaries ---")
more_on_zara = {
    "creation_date": 1975,
    "number_stores": 10000  # This will update the existing value
}

brand.update(more_on_zara)
print(f"Merged dictionary - creation_date: {brand.get('creation_date')}")
print(f"Merged dictionary - number_stores: {brand['number_stores']}")


print("\n" + "=" * 60)
print("🌟 EXERCISE 4: Disney Characters")
print("=" * 60)

users = ["Mickey", "Minnie", "Donald", "Ariel", "Pluto"]

# 1. Characters to indices (name: index)
char_to_index = {char: idx for idx, char in enumerate(users)}
print(f"1. Characters to indices:\n   {char_to_index}")

# 2. Indices to characters (index: name)
index_to_char = {idx: char for idx, char in enumerate(users)}
print(f"\n2. Indices to characters:\n   {index_to_char}")

# 3. Sorted alphabetically, then map to indices
sorted_users = sorted(users)
sorted_char_to_index = {char: idx for idx, char in enumerate(sorted_users)}
print(f"\n3. Sorted alphabetically to indices:\n   {sorted_char_to_index}")


print("\n" + "=" * 60)
print("ALL EXERCISES COMPLETED! 🎉")
print("=" * 60)