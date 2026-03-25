#!/usr/bin/env python3
"""
PYTHON MODULES & DUNDER METHODS EXERCISES
Topics: __str__, __repr__, __add__, __iadd__, Modules, datetime, faker
"""

import random
import string
from datetime import datetime, timedelta
from faker import Faker

print("=" * 60)
print("🌟 EXERCISE 1: Currencies (Dunder Methods)")
print("=" * 60)

class Currency:
    def __init__(self, currency, amount):
        self.currency = currency
        self.amount = amount
    
    def __str__(self):
        """String representation for users"""
        if self.amount == 1:
            return f"{self.amount} {self.currency}"
        return f"{self.amount} {self.currency}s"
    
    def __repr__(self):
        """Official string representation"""
        return f"'{self.__str__()}'"
    
    def __int__(self):
        """Convert to integer"""
        return self.amount
    
    def __add__(self, other):
        """Add Currency + Currency or Currency + int"""
        if isinstance(other, int):
            return Currency(self.currency, self.amount + other)
        elif isinstance(other, Currency):
            if self.currency != other.currency:
                raise TypeError(f"Cannot add between Currency type <{self.currency}> and <{other.currency}>")
            return Currency(self.currency, self.amount + other.amount)
        else:
            raise TypeError(f"Unsupported type for addition: {type(other)}")
    
    def __iadd__(self, other):
        """In-place addition (+=)"""
        if isinstance(other, int):
            self.amount += other
        elif isinstance(other, Currency):
            if self.currency != other.currency:
                raise TypeError(f"Cannot add between Currency type <{self.currency}> and <{other.currency}>")
            self.amount += other.amount
        else:
            raise TypeError(f"Unsupported type for addition: {type(other)}")
        return self

# Test Currency class
c1 = Currency('dollar', 5)
c2 = Currency('dollar', 10)
c3 = Currency('shekel', 1)
c4 = Currency('shekel', 10)

print(f"print(c1): {c1}")
print(f"int(c1): {int(c1)}")
print(f"repr(c1): {repr(c1)}")
print(f"c1 + 5: {c1 + 5}")
print(f"c1 + c2: {c1 + c2}")

c1 += 5
print(f"c1 += 5: {c1}")

c1 += c2
print(f"c1 += c2: {c1}")

# This will raise error - uncomment to test
# print(c1 + c3)


print("\n" + "=" * 60)
print("🌟 EXERCISE 2: Import (func.py simulation)")
print("=" * 60)

# Simulating func.py content here (normally in separate file)
def sum_two_numbers(a, b):
    """Sum two numbers and print result"""
    result = a + b
    print(f"{a} + {b} = {result}")
    return result

# Import and use (simulating import from func.py)
print("Calling sum_two_numbers(10, 20):")
sum_two_numbers(10, 20)


print("\n" + "=" * 60)
print("🌟 EXERCISE 3: String Module")
print("=" * 60)

def generate_random_string(length=5):
    """Generate random string of letters"""
    # Step 1 & 2: Get all letters (uppercase + lowercase)
    all_letters = string.ascii_letters  # 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    
    # Step 3: Generate random string
    result = ""
    for _ in range(length):
        result += random.choice(all_letters)
    
    return result

# Alternative using list comprehension
def generate_random_string_v2(length=5):
    return ''.join(random.choice(string.ascii_letters) for _ in range(length))

random_str = generate_random_string()
print(f"Random string (method 1): {random_str}")

random_str2 = generate_random_string_v2()
print(f"Random string (method 2): {random_str2}")


print("\n" + "=" * 60)
print("🌟 EXERCISE 4: Current Date")
print("=" * 60)

def display_current_date():
    """Display the current date"""
    current_date = datetime.now().date()
    print(f"Current date: {current_date}")
    return current_date

display_current_date()


print("\n" + "=" * 60)
print("🌟 EXERCISE 5: Time Until January 1st")
print("=" * 60)

def time_until_january_first():
    """Calculate time left until next January 1st"""
    now = datetime.now()
    
    # Determine next January 1st
    if now.month == 1 and now.day == 1:
        # Today is Jan 1st, go to next year
        next_january = datetime(now.year + 1, 1, 1)
    else:
        # Next Jan 1st is this year or next
        next_january = datetime(now.year + 1, 1, 1)
    
    time_left = next_january - now
    
    print(f"Current time: {now}")
    print(f"Next January 1st: {next_january}")
    print(f"Time left: {time_left}")
    print(f"Days: {time_left.days}")
    print(f"Seconds: {time_left.seconds}")
    
    return time_left

time_until_january_first()


print("\n" + "=" * 60)
print("🌟 EXERCISE 6: Birthday and Minutes")
print("=" * 60)

def calculate_lived_minutes(birthdate_str, date_format="%Y-%m-%d"):
    """
    Calculate how many minutes a person has lived.
    
    Args:
        birthdate_str: Birthdate as string
        date_format: Format of the date string (default: YYYY-MM-DD)
    """
    # Parse the birthdate
    birthdate = datetime.strptime(birthdate_str, date_format)
    
    # Get current time
    now = datetime.now()
    
    # Calculate difference
    time_lived = now - birthdate
    
    # Convert to minutes
    total_seconds = time_lived.total_seconds()
    total_minutes = int(total_seconds / 60)
    
    print(f"Birthdate: {birthdate.strftime('%B %d, %Y')}")
    print(f"You have lived approximately {total_minutes:,} minutes!")
    print(f"That's about {total_minutes // 525600:,} years in minutes!")
    
    return total_minutes

# Test with a sample birthdate
calculate_lived_minutes("1990-05-15")


print("\n" + "=" * 60)
print("🌟 EXERCISE 7: Faker Module")
print("=" * 60)

def generate_fake_users(num_users=5):
    """
    Generate a list of fake user dictionaries.
    
    Args:
        num_users: Number of users to generate
    """
    fake = Faker()
    users = []
    
    for _ in range(num_users):
        user = {
            "name": fake.name(),
            "address": fake.address().replace("\n", ", "),  # Make address single line
            "language_code": fake.language_code()
        }
        users.append(user)
    
    return users

# Generate and display users
fake_users = generate_fake_users(3)
print("Generated fake users:")
for i, user in enumerate(fake_users, 1):
    print(f"\nUser {i}:")
    for key, value in user.items():
        print(f"  {key}: {value}")


print("\n" + "=" * 60)
print("ALL EXERCISES COMPLETED! 🎉")
print("=" * 60)