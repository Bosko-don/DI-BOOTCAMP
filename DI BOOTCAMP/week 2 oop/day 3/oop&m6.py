#!/usr/bin/env python3
"""
HARDER DAILY CHALLENGE
Sort list of tuples using lambda function
Priority: Name > Age > Score
"""

print("=" * 60)
print("📋 STUDENT DATA SORTER (Using Lambda)")
print("=" * 60)

# Collect 5 entries from user
students = []

print("\nEnter 5 student records (Name, Age, Score):")
for i in range(5):
    print(f"\n--- Entry {i + 1} ---")
    name = input("Name: ").strip()
    age = int(input("Age: ").strip())
    score = int(input("Score: ").strip())
    
    # Store as tuple (name, age, score)
    students.append((name, age, score))

print(f"\n{'='*60}")
print("Original list:")
print(students)

# Sort using lambda: Priority Name > Age > Score
# Lambda returns a tuple (name, age, score) for comparison
sorted_students = sorted(students, key=lambda x: (x[0], x[1], x[2]))

print(f"\nSorted list (Name > Age > Score):")
print(sorted_students)

# Alternative: Using list.sort() method (modifies original list)
students.sort(key=lambda x: (x[0], x[1], x[2]))
print(f"\nUsing .sort() method:")
print(students)