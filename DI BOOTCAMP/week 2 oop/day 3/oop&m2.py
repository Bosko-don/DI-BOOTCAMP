#!/usr/bin/env python3
"""
PYTHON MODULES EXERCISES
Topics: datetime, regex, random, string manipulation
"""

import datetime
import re
import random
import string

print("=" * 60)
print("🌟 EXERCISE 1: Upcoming Holiday")
print("=" * 60)

def upcoming_holiday():
    """Display today's date and days until next holiday"""
    today = datetime.date.today()
    print(f"Today's date: {today.strftime('%B %d, %Y')}")
    
    # Define holidays (month, day, name)
    holidays = [
        (1, 1, "New Year's Day"),
        (2, 14, "Valentine's Day"),
        (3, 17, "St. Patrick's Day"),
        (4, 1, "April Fool's Day"),
        (5, 1, "Labor Day"),
        (7, 4, "Independence Day"),
        (10, 31, "Halloween"),
        (11, 25, "Thanksgiving"),
        (12, 25, "Christmas"),
        (12, 31, "New Year's Eve")
    ]
    
    # Find next holiday
    next_holiday = None
    days_until = None
    
    for month, day, name in holidays:
        holiday_date = datetime.date(today.year, month, day)
        
        # If holiday already passed this year, check next year
        if holiday_date < today:
            holiday_date = datetime.date(today.year + 1, month, day)
        
        current_days = (holiday_date - today).days
        
        if days_until is None or current_days < days_until:
            days_until = current_days
            next_holiday = name
    
    print(f"The next holiday is {next_holiday} in {days_until} days!")

upcoming_holiday()


print("\n" + "=" * 60)
print("🌟 EXERCISE 2: How Old Are You On Jupiter?")
print("=" * 60)

def space_age(seconds):
    """Calculate age on different planets"""
    # Earth year in seconds
    earth_year = 31557600
    
    # Orbital periods relative to Earth
    planets = {
        "Earth": 1.0,
        "Mercury": 0.2408467,
        "Venus": 0.61519726,
        "Mars": 1.8808158,
        "Jupiter": 11.862615,
        "Saturn": 29.447498,
        "Uranus": 84.016846,
        "Neptune": 164.79132
    }
    
    print(f"If you are {seconds:,} seconds old:")
    
    for planet, period in planets.items():
        age = seconds / (earth_year * period)
        print(f"  On {planet:<10}: {age:.2f} years old")

# Test with example
space_age(1000000000)

# Test with user input
try:
    user_seconds = int(input("\nEnter your age in seconds: "))
    space_age(user_seconds)
except ValueError:
    print("Invalid input!")


print("\n" + "=" * 60)
print("🌟 EXERCISE 3: Regular Expression #1")
print("=" * 60)

def return_numbers(text):
    """Extract all numbers from a string using regex"""
    # Find all digits
    numbers = re.findall(r'\d', text)
    # Join them into a string
    result = ''.join(numbers)
    return result

test_string = 'k5k3q2g5z6x9bn'
print(f"Input: {test_string}")
print(f"Numbers extracted: {return_numbers(test_string)}")


print("\n" + "=" * 60)
print("🌟 EXERCISE 4: Regular Expression #2")
print("=" * 60)

def validate_full_name(name):
    """
    Validate full name:
    - Only letters and one space
    - First letter of each name capitalized
    """
    # Pattern: Word characters, space, word characters
    # ^[A-Z][a-z]+ [A-Z][a-z]+$
    pattern = r'^[A-Z][a-z]+ [A-Z][a-z]+$'
    
    if re.match(pattern, name):
        return True
    return False

# Test cases
test_names = ["John Doe", "john doe", "JohnDoe", "John  Doe", "John", "Jane Smith"]
for name in test_names:
    result = "✅ Valid" if validate_full_name(name) else "❌ Invalid"
    print(f"'{name}': {result}")

# Interactive version
user_name = input("\nEnter your full name: ")
if validate_full_name(user_name):
    print("Valid name!")
else:
    print("Invalid! Name should be 'First Last' with capital letters.")


print("\n" + "=" * 60)
print("🌟 EXERCISE 5: Python Password Generator")
print("=" * 60)

def generate_password(length):
    """Generate a secure password with required characters"""
    if length < 6 or length > 30:
        raise ValueError("Password length must be between 6 and 30")
    
    # Required character sets
    digits = string.digits
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    special = "!@#$%^&*()_+-=[]{}|;:,.<>?"
    
    # Ensure at least one of each type
    password = [
        random.choice(digits),
        random.choice(lowercase),
        random.choice(uppercase),
        random.choice(special)
    ]
    
    # Fill the rest with random choices from all characters
    all_chars = digits + lowercase + uppercase + special
    for _ in range(length - 4):
        password.append(random.choice(all_chars))
    
    # Shuffle to randomize positions
    random.shuffle(password)
    
    return ''.join(password)

def validate_password(password):
    """Test if password meets all requirements"""
    has_digit = any(c.isdigit() for c in password)
    has_lower = any(c.islower() for c in password)
    has_upper = any(c.isupper() for c in password)
    has_special = any(c in "!@#$%^&*()_+-=[]{}|;:,.<>?" for c in password)
    
    return {
        'valid': has_digit and has_lower and has_upper and has_special,
        'length': len(password),
        'has_digit': has_digit,
        'has_lower': has_lower,
        'has_upper': has_upper,
        'has_special': has_special
    }

def test_password_generator():
    """Test password generator 100 times"""
    print("Testing password generator 100 times...")
    
    passed = 0
    failed = 0
    
    for i in range(100):
        # Random length between 6 and 30
        length = random.randint(6, 30)
        password = generate_password(length)
        validation = validate_password(password)
        
        if validation['valid'] and validation['length'] == length:
            passed += 1
        else:
            failed += 1
            print(f"Test {i+1} FAILED: {validation}")
    
    print(f"\nResults: {passed} passed, {failed} failed")
    return failed == 0

# Run tests
if test_password_generator():
    print("✅ All tests passed!")

# Interactive password generator
print("\n--- Password Generator ---")
while True:
    try:
        pwd_length = int(input("Enter password length (6-30): "))
        if 6 <= pwd_length <= 30:
            break
        print("Please enter a number between 6 and 30!")
    except ValueError:
        print("Please enter a valid number!")

new_password = generate_password(pwd_length)
print(f"\n🔐 Your new password: {new_password}")
print("⚠️  IMPORTANT: Keep this password in a safe place!")


print("\n" + "=" * 60)
print("ALL EXERCISES COMPLETED! 🎉")
print("=" * 60)