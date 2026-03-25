# ============================================================
# PYTHON FUNDAMENTALS EXERCISES
# Topics: Print Statements, Variables, Math, Comparison Operators, If Statements, User Input
# ============================================================

# ============================================================
# Exercise 1: Hello World
# Instructions: Print "Hello world" four times using one line of code
# ============================================================
print("Hello world\n" * 4)


# ============================================================
# Exercise 2: Some Math
# Instructions: Calculate (99^3)*8 (99 to the power of 3, times 8)
# ============================================================
result = (99 ** 3) * 8
print(f"\nExercise 2: (99^3)*8 = {result}")


# ============================================================
# Exercise 3: What is the output?
# Instructions: Predict the output, comment your guess, then run to compare
# ============================================================
print("\nExercise 3: Comparison Operators")

print(f"5 < 3: {5 < 3}")           # My guess: False (5 is not less than 3)
print(f"3 == 3: {3 == 3}")         # My guess: True (3 equals 3)
print(f"3 == '3': {3 == '3'}")     # My guess: False (integer vs string)
# print(f"'3' > 3: {'3' > 3}")     # My guess: TypeError (can't compare string and int)
print(f"'Hello' == 'hello': {'Hello' == 'hello'}")  # My guess: False (case sensitive)


# ============================================================
# Exercise 4: Your computer brand
# Instructions: Create computer_brand variable and print sentence
# ============================================================
computer_brand = "Dell"  # Change this to your computer brand
print(f"\nExercise 4: I have a {computer_brand} computer.")


# ============================================================
# Exercise 5: Your information
# Instructions: Create variables and print interesting sentence
# ============================================================
name = "Alex"
age = 25
shoe_size = 42
info = f"My name is {name}, I am {age} years old, and I wear size {shoe_size} shoes. Fun fact: I've had the same shoe size since I was 16!"
print(f"\nExercise 5: {info}")


# ============================================================
# Exercise 6: A & B
# Instructions: Create two number variables, print "Hello World" if a > b
# ============================================================
a = 10
b = 5
print(f"\nExercise 6: a = {a}, b = {b}")
if a > b:
    print("Hello World")


# ============================================================
# Exercise 7: Odd or Even
# Instructions: Ask user for number, determine if odd or even
# ============================================================
print("\nExercise 7: Odd or Even Checker")
try:
    user_number = int(input("Enter a number: "))
    if user_number % 2 == 0:
        print(f"{user_number} is even!")
    else:
        print(f"{user_number} is odd!")
except ValueError:
    print("Please enter a valid number!")


# ============================================================
# Exercise 8: What's your name?
# Instructions: Ask user for name, compare with your name, print funny message
# ============================================================
print("\nExercise 8: Name Comparison")
my_name = "Alex"  # Change this to your name
user_name = input("What's your name? ")

if user_name.lower() == my_name.lower():
    print(f"Wow! {user_name}? That's my name too! We must be twins separated at birth! 👯")
else:
    print(f"{user_name}? That's a... unique name. I guess someone had to have it. 🤷")


# ============================================================
# Exercise 9: Tall enough to ride a roller coaster
# Instructions: Ask for height in cm, check if over 145cm
# ============================================================
print("\nExercise 9: Roller Coaster Height Check")
try:
    height = int(input("Enter your height in centimeters: "))
    if height > 145:
        print("🎢 Congratulations! You are tall enough to ride the roller coaster! Enjoy the thrill!")
    else:
        print("🌱 Sorry, you need to grow a bit more before you can ride. Eat your vegetables and try again next year!")
except ValueError:
    print("Please enter a valid number for your height!")