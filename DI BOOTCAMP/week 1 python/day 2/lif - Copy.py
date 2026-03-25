# ============================================================
# PYTHON DATA STRUCTURES EXERCISES
# Topics: Sequence, List, Set, Tuple, Loops, Conditionals
# ============================================================

print("=" * 60)
print("🌟 EXERCISE 1: Favorite Numbers")
print("=" * 60)

# Create set with favorite numbers
my_fav_numbers = {7, 13, 42, 99}
print(f"My favorite numbers: {my_fav_numbers}")

# Add two new numbers
my_fav_numbers.add(21)
my_fav_numbers.add(88)
print(f"After adding 21 and 88: {my_fav_numbers}")

# Remove the last added number (88) - Note: Sets are unordered so we remove specifically
my_fav_numbers.remove(88)
print(f"After removing 88: {my_fav_numbers}")

# Create friend's favorite numbers set
friend_fav_numbers = {3, 7, 21, 50, 100}
print(f"Friend's favorite numbers: {friend_fav_numbers}")

# Concatenate using union
our_fav_numbers = my_fav_numbers.union(friend_fav_numbers)
print(f"Our combined favorite numbers: {our_fav_numbers}")


print("\n" + "=" * 60)
print("🌟 EXERCISE 2: Tuple (Immutability)")
print("=" * 60)

# Create tuple
my_tuple = (1, 2, 3, 4, 5)
print(f"Original tuple: {my_tuple}")

# Try to add to tuple (this will fail)
try:
    my_tuple.append(6)
except AttributeError as e:
    print(f"❌ Error: {e}")
    print("Tuples are immutable - they cannot be changed after creation!")

# Workaround: Convert to list, add, convert back
tuple_as_list = list(my_tuple)
tuple_as_list.append(6)
new_tuple = tuple(tuple_as_list)
print(f"New tuple created from list: {new_tuple}")


print("\n" + "=" * 60)
print("🌟 EXERCISE 3: List Manipulation")
print("=" * 60)

basket = ["Banana", "Apples", "Oranges", "Blueberries"]
print(f"Original basket: {basket}")

# Remove "Banana"
basket.remove("Banana")
print(f"After removing 'Banana': {basket}")

# Remove "Blueberries"
basket.remove("Blueberries")
print(f"After removing 'Blueberries': {basket}")

# Add "Kiwi" to end
basket.append("Kiwi")
print(f"After adding 'Kiwi' to end: {basket}")

# Add "Apples" to beginning
basket.insert(0, "Apples")
print(f"After adding 'Apples' to beginning: {basket}")

# Count "Apples"
apple_count = basket.count("Apples")
print(f"'Apples' appears {apple_count} times")

# Empty the list
basket.clear()
print(f"Final state (emptied): {basket}")


print("\n" + "=" * 60)
print("🌟 EXERCISE 4: Floats")
print("=" * 60)

print("Float vs Integer: Float has decimal points (1.5), Integer is whole number (2)")

# Generate sequence 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5 using loop
sequence = []
for i in range(1, 9):
    number = i / 2 + 1
    sequence.append(number)

print(f"Generated sequence: {sequence}")


print("\n" + "=" * 60)
print("🌟 EXERCISE 5: For Loop")
print("=" * 60)

# Print all numbers 1 to 20
print("All numbers 1-20:")
for num in range(1, 21):
    print(num, end=" ")
print()

# Print even index numbers (0, 2, 4, 6... which are numbers 1, 3, 5, 7...)
print("\nNumbers at even indices (0-based):")
numbers = list(range(1, 21))
for i in range(len(numbers)):
    if i % 2 == 0:
        print(numbers[i], end=" ")
print()


print("\n" + "=" * 60)
print("🌟 EXERCISE 6: While Loop - Name Validation")
print("=" * 60)

while True:
    name = input("Please enter your name (at least 3 letters, no digits): ")
    
    if name.isdigit():
        print("❌ Invalid! Name cannot be only digits.")
    elif len(name) < 3:
        print("❌ Invalid! Name must be at least 3 letters long.")
    else:
        print(f"✅ Thank you, {name}!")
        break


print("\n" + "=" * 60)
print("🌟 EXERCISE 7: Favorite Fruits")
print("=" * 60)

# Get favorite fruits
fruits_input = input("Enter your favorite fruits (separated by spaces): ")
favorite_fruits = fruits_input.split()
print(f"Your favorite fruits: {favorite_fruits}")

# Check specific fruit
chosen_fruit = input("Enter the name of any fruit: ")

if chosen_fruit in favorite_fruits:
    print("You chose one of your favorite fruits! Enjoy! 🍎")
else:
    print("You chose a new fruit. I hope you enjoy it! 🍓")


print("\n" + "=" * 60)
print("🌟 EXERCISE 8: Pizza Toppings")
print("=" * 60)

toppings = []
base_price = 10
topping_price = 2.50

print("Enter pizza toppings one by one (type 'quit' to finish):")

while True:
    topping = input("Enter topping (or 'quit'): ").strip().lower()
    
    if topping == 'quit':
        break
    
    toppings.append(topping)
    print(f"Adding {topping} to your pizza. 🍕")

# Calculate and display
total_cost = base_price + (len(toppings) * topping_price)
print(f"\nYour pizza toppings: {', '.join(toppings) if toppings else 'None (cheese pizza)'}")
print(f"Total cost: ${total_cost:.2f} (Base: ${base_price} + {len(toppings)} toppings at ${topping_price} each)")


print("\n" + "=" * 60)
print("🌟 EXERCISE 9: Cinemax Tickets")
print("=" * 60)

# Main ticket calculation
family_ages = []
print("Enter ages of family members (type 'done' when finished):")

while True:
    age_input = input("Enter age (or 'done'): ")
    
    if age_input.lower() == 'done':
        break
    
    try:
        age = int(age_input)
        family_ages.append(age)
    except ValueError:
        print("Please enter a valid number or 'done'.")

# Calculate total cost
total_cost = 0
for age in family_ages:
    if age < 3:
        cost = 0
        print(f"Age {age}: FREE")
    elif 3 <= age <= 12:
        cost = 10
        print(f"Age {age}: ${cost}")
    else:
        cost = 15
        print(f"Age {age}: ${cost}")
    total_cost += cost

print(f"\nTotal ticket cost: ${total_cost}")

# BONUS: Teenage movie restriction
print("\n" + "-" * 40)
print("🎬 BONUS: Restricted Movie (Ages 16-21 only)")
print("-" * 40)

group_ages = []
print("Enter ages of group members (type 'done' when finished):")

while True:
    age_input = input("Enter age (or 'done'): ")
    
    if age_input.lower() == 'done':
        break
    
    try:
        age = int(age_input)
        group_ages.append(age)
    except ValueError:
        print("Please enter a valid number.")

# Filter allowed attendees (16-21 inclusive)
allowed_attendees = [age for age in group_ages if 16 <= age <= 21]
removed_attendees = [age for age in group_ages if age not in allowed_attendees]

print(f"\nOriginal group ages: {group_ages}")
if removed_attendees:
    print(f"Removed (not allowed): {removed_attendees}")
print(f"Final attendees (ages 16-21): {allowed_attendees}")

print("\n" + "=" * 60)
print("ALL EXERCISES COMPLETED! 🎉")
print("=" * 60)