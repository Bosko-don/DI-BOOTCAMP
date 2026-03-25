# ============================================================
# PYTHON FUNCTIONS EXERCISES
# Topics: Functions, Parameters, Default Values, Random, Lists
# ============================================================

import random

print("=" * 60)
print("🌟 EXERCISE 1: What Are You Learning?")
print("=" * 60)

def display_message():
    """Display a message about what I'm learning"""
    print("I am learning about functions in Python.")

# Call the function
display_message()


print("\n" + "=" * 60)
print("🌟 EXERCISE 2: What's Your Favorite Book?")
print("=" * 60)

def favorite_book(title):
    """Display a message about favorite book"""
    print(f"One of my favorite books is {title}")

# Call the function
favorite_book("Alice in Wonderland")
favorite_book("1984")


print("\n" + "=" * 60)
print("🌟 EXERCISE 3: Some Geography")
print("=" * 60)

def describe_city(city, country="Unknown"):
    """Describe which country a city is in"""
    print(f"{city} is in {country}.")

# Call with both arguments
describe_city("Reykjavik", "Iceland")
describe_city("Tokyo", "Japan")
# Call with default country
describe_city("Paris")


print("\n" + "=" * 60)
print("🌟 EXERCISE 4: Random")
print("=" * 60)

def compare_random(user_number):
    """Compare user number with random number"""
    if not 1 <= user_number <= 100:
        print("Please enter a number between 1 and 100")
        return
    
    random_number = random.randint(1, 100)
    
    if user_number == random_number:
        print("Success! The numbers match!")
    else:
        print(f"Fail! Your number: {user_number}, Random number: {random_number}")

# Call the function
compare_random(50)
compare_random(75)


print("\n" + "=" * 60)
print("🌟 EXERCISE 5: Let's Create Some Personalized Shirts!")
print("=" * 60)

def make_shirt(size="large", text="I love Python"):
    """Create a shirt with given size and text"""
    print(f"The size of the shirt is {size} and the text is '{text}'.")

# Call with default values
make_shirt()
# Call with medium size (default text)
make_shirt("medium")
# Call with custom size and text
make_shirt("small", "Python is awesome!")
# Call with keyword arguments
make_shirt(size="XL", text="Code Master")
make_shirt(text="Hello World!", size="S")


print("\n" + "=" * 60)
print("🌟 EXERCISE 6: Magicians...")
print("=" * 60)

magician_names = ['Harry Houdini', 'David Blaine', 'Criss Angel']

def show_magicians(magicians):
    """Display all magicians in the list"""
    for magician in magicians:
        print(magician)

def make_great(magicians):
    """Add 'the Great' to each magician's name"""
    for i in range(len(magicians)):
        magicians[i] = magicians[i] + " the Great"

print("Original magicians:")
show_magicians(magician_names[:])  # Show copy to preserve original

make_great(magician_names)

print("\nModified magicians:")
show_magicians(magician_names)


print("\n" + "=" * 60)
print("🌟 EXERCISE 7: Temperature Advice")
print("=" * 60)

def get_random_temp(season=None):
    """Generate a random temperature based on season or full range"""
    if season == "winter":
        return random.uniform(-10, 10)
    elif season == "spring":
        return random.uniform(10, 20)
    elif season == "summer":
        return random.uniform(25, 40)
    elif season == "autumn" or season == "fall":
        return random.uniform(10, 25)
    else:
        # Full range if no season specified
        return random.uniform(-10, 40)

def get_season_from_month(month):
    """Determine season from month number"""
    if month in [12, 1, 2]:
        return "winter"
    elif month in [3, 4, 5]:
        return "spring"
    elif month in [6, 7, 8]:
        return "summer"
    elif month in [9, 10, 11]:
        return "autumn"
    else:
        return None

def main():
    """Main temperature advice function"""
    # Ask for month (bonus)
    try:
        month = int(input("Enter month number (1-12) or 0 for random: "))
        if 1 <= month <= 12:
            season = get_season_from_month(month)
            temp = get_random_temp(season)
            print(f"\nSeason: {season.capitalize()}")
        else:
            temp = get_random_temp()
            print("\nRandom temperature across all seasons")
    except ValueError:
        temp = get_random_temp()
        print("\nInvalid input - using random temperature")
    
    # Round to 1 decimal place for cleaner output
    temp = round(temp, 1)
    print(f"The temperature right now is {temp} degrees Celsius.")
    
    # Provide advice based on temperature
    if temp < 0:
        print("Brrr, that's freezing! Wear some extra layers today. 🧥")
    elif 0 <= temp < 16:
        print("Quite chilly! Don't forget your coat. 🧣")
    elif 16 <= temp < 24:
        print("Nice weather! Enjoy your day. ☀️")
    elif 24 <= temp < 32:
        print("A bit warm, stay hydrated. 💧")
    else:  # 32 to 40
        print("It's really hot! Stay cool. 🌴")

# Run the main function
main()


print("\n" + "=" * 60)
print("ALL EXERCISES COMPLETED! 🎉")
print("=" * 60)