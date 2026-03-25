#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
PYTHON OOP EXERCISES
Topics: Inheritance, Polymorphism, Class Methods, super()
"""

import random

def main():
    """Main function to run all exercises"""
    
    # ============================================================
    # EXERCISE 1: Pets
    # ============================================================
    print("=" * 60)
    print("EXERCISE 1: Pets")
    print("=" * 60)

    class Pets:
        def __init__(self, animals):
            self.animals = animals

        def walk(self):
            for animal in self.animals:
                result = animal.walk()
                print(result)

    class Cat:
        is_lazy = True

        def __init__(self, name, age):
            self.name = name
            self.age = age

        def walk(self):
            return f'{self.name} is just walking around'

    class Bengal(Cat):
        def sing(self, sounds):
            return f'{sounds}'

    class Chartreux(Cat):
        def sing(self, sounds):
            return f'{sounds}'

    class Siamese(Cat):
        pass

    # Create and test
    bengal_cat = Bengal("Leo", 3)
    chartreux_cat = Chartreux("Luna", 5)
    siamese_cat = Siamese("Milo", 2)

    all_cats = [bengal_cat, chartreux_cat, siamese_cat]
    sara_pets = Pets(all_cats)

    print("Taking all cats for a walk:")
    sara_pets.walk()


    # ============================================================
    # EXERCISE 2: Dogs
    # ============================================================
    print("\n" + "=" * 60)
    print("EXERCISE 2: Dogs")
    print("=" * 60)

    class Dog:
        def __init__(self, name, age, weight):
            self.name = name
            self.age = age
            self.weight = weight
        
        def bark(self):
            return f"{self.name} is barking"
        
        def run_speed(self):
            return self.weight / self.age * 10
        
        def fight(self, other_dog):
            my_power = self.run_speed() * self.weight
            other_power = other_dog.run_speed() * other_dog.weight
            
            if my_power > other_power:
                return f"{self.name} won the fight against {other_dog.name}!"
            elif other_power > my_power:
                return f"{other_dog.name} won the fight against {self.name}!"
            else:
                return f"It's a tie!"

    dog1 = Dog("Rex", 5, 30)
    dog2 = Dog("Buddy", 3, 25)
    dog3 = Dog("Max", 7, 20)

    print(f"{dog1.name} says: {dog1.bark()}")
    print(f"{dog1.name}'s run speed: {dog1.run_speed():.2f}")
    print(f"{dog2.name}'s run speed: {dog2.run_speed():.2f}")
    print(dog1.fight(dog2))
    print(dog2.fight(dog3))


    # ============================================================
    # EXERCISE 3: Dogs Domesticated
    # ============================================================
    print("\n" + "=" * 60)
    print("EXERCISE 3: Dogs Domesticated")
    print("=" * 60)

    class PetDog(Dog):
        def __init__(self, name, age, weight):
            super().__init__(name, age, weight)
            self.trained = False
        
        def train(self):
            bark_result = self.bark()
            print(bark_result)
            self.trained = True
        
        def play(self, *args):
            dog_names = [self.name]
            for dog in args:
                dog_names.append(dog.name)
            names_str = ", ".join(dog_names)
            print(f"{names_str} all play together")
        
        def do_a_trick(self):
            if self.trained:
                tricks = ["does a barrel roll", "stands on his back legs", 
                         "shakes your hand", "plays dead"]
                trick = random.choice(tricks)
                print(f"{self.name} {trick}")
            else:
                print(f"{self.name} is not trained yet!")

    my_dog = PetDog("Fido", 2, 10)
    my_dog.train()

    friend_dog1 = PetDog("Buddy", 3, 15)
    friend_dog2 = PetDog("Max", 4, 12)

    my_dog.play(friend_dog1, friend_dog2)
    my_dog.do_a_trick()

    untrained = PetDog("Rex", 5, 20)
    untrained.do_a_trick()


    # ============================================================
    # EXERCISE 4: Family and Person Classes
    # ============================================================
    print("\n" + "=" * 60)
    print("EXERCISE 4: Family and Person Classes")
    print("=" * 60)

    class Person:
        def __init__(self, first_name, age):
            self.first_name = first_name
            self.age = age
            self.last_name = ""
        
        def is_18(self):
            return self.age >= 18

    class Family:
        def __init__(self, last_name):
            self.last_name = last_name
            self.members = []
            self.parents = {"father": "", "mother": ""}
        
        def set_parents(self, father_name, mother_name):
            self.parents["father"] = father_name
            self.parents["mother"] = mother_name
        
        def born(self, first_name, age):
            new_person = Person(first_name, age)
            new_person.last_name = self.last_name
            self.members.append(new_person)
            print(f"Welcome {first_name} {self.last_name} to the family!")
        
        def check_majority(self, first_name):
            found = False
            for member in self.members:
                if member.first_name == first_name:
                    found = True
                    if member.is_18():
                        father = self.parents["father"]
                        mother = self.parents["mother"]
                        print(f"You are over 18, your parents {mother} and {father} accept that you will go out with your friends")
                    else:
                        print("Sorry, you are not allowed to go out with your friends.")
                    break
            
            if not found:
                print(f"{first_name} is not in this family.")
        
        def family_presentation(self):
            print(f"\nThe {self.last_name} Family")
            print("-" * 30)
            for member in self.members:
                print(f"  {member.first_name} {member.last_name}, {member.age} years old")

    # Test Family
    smith_family = Family("Smith")
    smith_family.set_parents("John", "Jane")

    smith_family.born("Tom", 20)
    smith_family.born("Lisa", 15)
    smith_family.born("Baby", 1)

    smith_family.family_presentation()

    print()
    smith_family.check_majority("Tom")
    smith_family.check_majority("Lisa")


    # ============================================================
    # COMPLETION
    # ============================================================
    print("\n" + "=" * 60)
    print("ALL EXERCISES COMPLETED!")
    print("=" * 60)


# Run the main function
if __name__ == "__main__":
    main()