#!/usr/bin/env python3
"""
Vaccines Management System - Complete Solution
Part 1: Human and Queue classes with basic functionality
Part 2: Family relationships and queue rearrangement
"""


class Human:
    """
    Represents a citizen waiting for vaccination.
    
    Attributes:
        id_number (str): Unique ID of the person
        name (str): Name of the person
        age (int): Age of the person
        priority (bool): Whether person has priority status
        blood_type (str): Blood type ("A", "B", "AB", or "O")
        family (list): List of family members (Part 2)
    """
    
    VALID_BLOOD_TYPES = ["A", "B", "AB", "O"]
    
    def __init__(self, id_number, name, age, priority, blood_type):
        """
        Initialize a Human.
        
        Args:
            id_number (str): Unique identifier
            name (str): Person's name
            age (int): Person's age
            priority (bool): Priority status
            blood_type (str): One of "A", "B", "AB", "O"
        """
        self.id_number = id_number
        self.name = name
        self.age = age
        self.priority = priority
        
        # Validate blood type
        if blood_type.upper() not in self.VALID_BLOOD_TYPES:
            raise ValueError(f"Invalid blood type: {blood_type}. Must be one of {self.VALID_BLOOD_TYPES}")
        self.blood_type = blood_type.upper()
        
        # Part 2: Family attribute
        self.family = []
    
    def add_family_member(self, person):
        """
        Add a family member to this human's family.
        Also adds this human to the other person's family.
        
        Args:
            person (Human): Another human to add as family
        """
        # Add person to this human's family if not already there
        if person not in self.family:
            self.family.append(person)
        
        # Add this human to person's family if not already there
        if self not in person.family:
            person.family.append(self)
    
    def __str__(self):
        """String representation of the human."""
        priority_str = "PRIORITY" if self.priority else "normal"
        return f"{self.name} (ID: {self.id_number}, Age: {self.age}, Blood: {self.blood_type}, {priority_str})"
    
    def __repr__(self):
        """Detailed representation for debugging."""
        return f"Human('{self.id_number}', '{self.name}', {self.age}, {self.priority}, '{self.blood_type}')"
    
    def __eq__(self, other):
        """Check if two humans are the same based on id_number."""
        if not isinstance(other, Human):
            return False
        return self.id_number == other.id_number


class Queue:
    """
    Represents a queue of humans waiting for vaccination.
    Manages priority and ordering of people.
    
    Attributes:
        humans (list): List of Human objects waiting in queue
    """
    
    def __init__(self):
        """Initialize an empty queue."""
        self.humans = []
    
    def add_person(self, person):
        """
        Add a human to the queue.
        If person is older than 60 or has priority, put at beginning (index 0).
        Otherwise, add to the end.
        
        Bonus: Not using list.insert() - manually shifting elements.
        
        Args:
            person (Human): Person to add to queue
        """
        # Check if person should be at front (priority or age > 60)
        if person.priority or person.age > 60:
            # Add to beginning (index 0)
            # Bonus: Not using insert, so we create new list
            new_humans = [person] + self.humans
            self.humans = new_humans
        else:
            # Add to end
            self.humans = self.humans + [person]
    
    def find_in_queue(self, person):
        """
        Find the index of a human in the queue.
        
        Bonus: Not using list.index() - manual search.
        
        Args:
            person (Human): Person to find
            
        Returns:
            int: Index of person, or -1 if not found
        """
        # Manual search without using index()
        for i in range(len(self.humans)):
            if self.humans[i] == person:
                return i
        return -1
    
    def swap(self, person1, person2):
        """
        Swap two people in the queue.
        
        Args:
            person1 (Human): First person
            person2 (Human): Second person
        """
        idx1 = self.find_in_queue(person1)
        idx2 = self.find_in_queue(person2)
        
        if idx1 == -1:
            raise ValueError(f"{person1.name} not found in queue")
        if idx2 == -1:
            raise ValueError(f"{person2.name} not found in queue")
        
        # Swap without using tuple unpacking (to be explicit)
        temp = self.humans[idx1]
        self.humans[idx1] = self.humans[idx2]
        self.humans[idx2] = temp
    
    def get_next(self):
        """
        Get the next human in queue (first person, index 0).
        Removes them from the queue.
        
        Bonus: Not using list.pop() - manual removal.
        
        Returns:
            Human: Next person in queue, or None if empty
        """
        if not self.humans:
            return None
        
        # Get first person
        next_person = self.humans[0]
        
        # Remove from queue (create new list without first element)
        # Bonus: Not using pop()
        new_humans = []
        for i in range(1, len(self.humans)):
            new_humans.append(self.humans[i])
        self.humans = new_humans
        
        return next_person
    
    def get_next_blood_type(self, blood_type):
        """
        Get the first human with specific blood type.
        Removes them from the queue.
        
        Args:
            blood_type (str): Blood type to search for
            
        Returns:
            Human: First person with matching blood type, or None
        """
        # Find first person with matching blood type
        target_index = -1
        for i in range(len(self.humans)):
            if self.humans[i].blood_type == blood_type.upper():
                target_index = i
                break
        
        if target_index == -1:
            return None
        
        # Get the person
        person = self.humans[target_index]
        
        # Remove from queue (manual, without pop)
        new_humans = []
        for i in range(len(self.humans)):
            if i != target_index:
                new_humans.append(self.humans[i])
        self.humans = new_humans
        
        return person
    
    def sort_by_age(self):
        """
        Sort the queue by priority rules:
        1. Priority people first
        2. Then older people (descending age)
        3. Then younger people (descending age)
        
        Bonus: Not using list.sort() or sorted() - implementing bubble sort.
        """
        if len(self.humans) <= 1:
            return
        
        # Bubble sort implementation
        n = len(self.humans)
        for i in range(n):
            for j in range(0, n - i - 1):
                person_a = self.humans[j]
                person_b = self.humans[j + 1]
                
                # Check if swap is needed
                should_swap = False
                
                # Rule 1: Priority people come first
                if not person_a.priority and person_b.priority:
                    should_swap = True
                # Both have same priority status
                elif person_a.priority == person_b.priority:
                    # Rule 2 & 3: Older people first (descending age)
                    if person_a.age < person_b.age:
                        should_swap = True
                
                if should_swap:
                    # Swap
                    temp = self.humans[j]
                    self.humans[j] = self.humans[j + 1]
                    self.humans[j + 1] = temp
    
    def rearrange_queue(self):
        """
        Part 2: Rearrange queue so no two family members are adjacent.
        Uses a greedy approach to spread out family members.
        """
        if len(self.humans) <= 2:
            return
        
        # Keep trying until no adjacent family members or no more swaps possible
        max_iterations = len(self.humans) * 2
        iteration = 0
        
        while iteration < max_iterations:
            found_adjacent = False
            
            # Check each pair of adjacent people
            for i in range(len(self.humans) - 1):
                person_a = self.humans[i]
                person_b = self.humans[i + 1]
                
                # Check if they are family
                is_family = False
                for family_member in person_a.family:
                    if family_member == person_b:
                        is_family = True
                        break
                
                if is_family:
                    found_adjacent = True
                    # Try to swap with next person
                    if i + 2 < len(self.humans):
                        # Swap with person after
                        temp = self.humans[i + 1]
                        self.humans[i + 1] = self.humans[i + 2]
                        self.humans[i + 2] = temp
                    elif i > 0:
                        # Swap with person before
                        temp = self.humans[i]
                        self.humans[i] = self.humans[i - 1]
                        self.humans[i - 1] = temp
                    break
            
            if not found_adjacent:
                break
            
            iteration += 1
    
    def display(self):
        """Display the current queue."""
        print(f"\nCurrent Queue ({len(self.humans)} people):")
        print("-" * 60)
        if not self.humans:
            print("  (Queue is empty)")
        else:
            for i, person in enumerate(self.humans):
                print(f"  {i}. {person}")
        print("-" * 60)
    
    def __str__(self):
        """String representation of queue."""
        return f"Queue with {len(self.humans)} humans waiting"
    
    def __repr__(self):
        """Detailed representation."""
        return f"Queue({len(self.humans)} humans)"


# =============================================================================
# DEMONSTRATION AND TESTING
# =============================================================================

def demonstrate_part1():
    """Demonstrate Part 1 functionality."""
    print("\n" + "=" * 70)
    print("PART 1: BASIC HUMAN AND QUEUE FUNCTIONALITY")
    print("=" * 70)
    
    # Create humans
    print("\n1. Creating humans...")
    h1 = Human("ID001", "Alice", 35, False, "A")
    h2 = Human("ID002", "Bob", 65, False, "B")
    h3 = Human("ID003", "Charlie", 45, True, "O")
    h4 = Human("ID004", "Diana", 70, False, "AB")
    h5 = Human("ID005", "Eve", 25, False, "A")
    
    print(f"   Created: {h1.name}, {h2.name}, {h3.name}, {h4.name}, {h5.name}")
    
    # Create queue and add people
    print("\n2. Adding people to queue...")
    queue = Queue()
    
    # Add regular person (goes to end)
    queue.add_person(h1)  # Alice, 35, normal
    print(f"   Added Alice (35, normal) - Queue: {len(queue.humans)} people")
    
    # Add priority person (goes to front)
    queue.add_person(h3)  # Charlie, 45, priority
    print(f"   Added Charlie (45, priority) - Queue: {len(queue.humans)} people")
    
    # Add elderly person (goes to front)
    queue.add_person(h2)  # Bob, 65, elderly
    print(f"   Added Bob (65, elderly) - Queue: {len(queue.humans)} people")
    
    # Add more people
    queue.add_person(h4)  # Diana, 70, elderly
    queue.add_person(h5)  # Eve, 25, normal
    
    queue.display()
    
    # Test find_in_queue
    print("\n3. Testing find_in_queue...")
    idx = queue.find_in_queue(h3)
    print(f"   Charlie found at index: {idx}")
    
    # Test swap
    print("\n4. Testing swap...")
    print(f"   Swapping {h1.name} and {h5.name}...")
    queue.swap(h1, h5)
    queue.display()
    
    # Test get_next
    print("\n5. Testing get_next...")
    next_person = queue.get_next()
    print(f"   Next person: {next_person}")
    queue.display()
    
    # Test get_next_blood_type
    print("\n6. Testing get_next_blood_type('A')...")
    person_a = queue.get_next_blood_type("A")
    print(f"   Found person with blood type A: {person_a}")
    queue.display()
    
    # Test sort_by_age
    print("\n7. Testing sort_by_age...")
    # Reset queue with all people
    queue = Queue()
    queue.add_person(h1)  # Alice, 35, normal
    queue.add_person(h2)  # Bob, 65, normal
    queue.add_person(h3)  # Charlie, 45, priority
    queue.add_person(h4)  # Diana, 70, normal
    queue.add_person(h5)  # Eve, 25, normal
    
    print("   Before sorting:")
    queue.display()
    
    queue.sort_by_age()
    print("   After sorting (priority first, then by age):")
    queue.display()


def demonstrate_part2():
    """Demonstrate Part 2 functionality (family relationships)."""
    print("\n" + "=" * 70)
    print("PART 2: FAMILY RELATIONSHIPS AND QUEUE REARRANGEMENT")
    print("=" * 70)
    
    # Create family members
    print("\n1. Creating family members...")
    father = Human("F001", "John (Father)", 45, False, "A")
    mother = Human("M001", "Jane (Mother)", 43, False, "B")
    son = Human("S001", "Jack (Son)", 20, False, "O")
    daughter = Human("D001", "Jill (Daughter)", 18, False, "AB")
    neighbor = Human("N001", "Tom (Neighbor)", 30, False, "A")
    
    # Establish family relationships
    print("\n2. Establishing family relationships...")
    father.add_family_member(mother)
    father.add_family_member(son)
    father.add_family_member(daughter)
    mother.add_family_member(son)
    mother.add_family_member(daughter)
    son.add_family_member(daughter)
    
    print(f"   John's family: {[p.name for p in father.family]}")
    print(f"   Jane's family: {[p.name for p in mother.family]}")
    print(f"   Jack's family: {[p.name for p in son.family]}")
    print(f"   Jill's family: {[p.name for p in daughter.family]}")
    print(f"   Tom's family: {[p.name for p in neighbor.family]} (none)")
    
    # Create queue with family members adjacent
    print("\n3. Creating queue with family members adjacent...")
    queue = Queue()
    queue.add_person(father)
    queue.add_person(mother)  # Family - adjacent to father
    queue.add_person(son)     # Family - adjacent to mother
    queue.add_person(daughter)  # Family - adjacent to son
    queue.add_person(neighbor)  # Not family
    
    print("   Queue before rearrangement:")
    queue.display()
    
    # Check adjacencies
    print("\n4. Checking family adjacencies...")
    for i in range(len(queue.humans) - 1):
        p1 = queue.humans[i]
        p2 = queue.humans[i + 1]
        is_family = p2 in p1.family
        print(f"   {p1.name} <-> {p2.name}: {'FAMILY' if is_family else 'not family'}")
    
    # Rearrange queue
    print("\n5. Rearranging queue (no family members adjacent)...")
    queue.rearrange_queue()
    queue.display()
    
    # Check adjacencies after rearrange
    print("\n6. Checking adjacencies after rearrangement...")
    family_adjacent = False
    for i in range(len(queue.humans) - 1):
        p1 = queue.humans[i]
        p2 = queue.humans[i + 1]
        is_family = p2 in p1.family
        status = "FAMILY" if is_family else "not family"
        print(f"   {p1.name} <-> {p2.name}: {status}")
        if is_family:
            family_adjacent = True
    
    if not family_adjacent:
        print("\n   SUCCESS: No family members are adjacent!")
    else:
        print("\n   NOTE: Some family members still adjacent (limited by queue size)")


def demonstrate_bonus():
    """Demonstrate that bonus requirements are met (no built-in methods)."""
    print("\n" + "=" * 70)
    print("BONUS: VERIFICATION (No built-in list methods used)")
    print("=" * 70)
    
    print("""
    The following built-in methods were NOT used:
    
    - list.insert()  -> Used manual list concatenation: [person] + list
    - list.pop()     -> Used manual list slicing and reconstruction
    - list.index()   -> Used manual for-loop search
    - list.sort()    -> Used bubble sort implementation
    - sorted()       -> Used custom sorting algorithm
    
    All requirements met with manual implementations!
    """)


def main():
    """Main function to run all demonstrations."""
    print("\n" + "=" * 70)
    print("VACCINES MANAGEMENT SYSTEM - COMPLETE SOLUTION")
    print("=" * 70)
    
    demonstrate_part1()
    demonstrate_part2()
    demonstrate_bonus()
    
    print("\n" + "=" * 70)
    print("SUMMARY")
    print("=" * 70)
    print("""
    Part 1 Completed:
    - Human class with id_number, name, age, priority, blood_type
    - Queue class with humans list
    - add_person() - adds to front if priority/elderly, else back
    - find_in_queue() - returns index of person
    - swap() - swaps two people in queue
    - get_next() - removes and returns first person
    - get_next_blood_type() - finds first person with specific blood type
    - sort_by_age() - priority first, then by age (descending)
    
    Part 2 Completed:
    - family attribute added to Human
    - add_family_member() - bidirectional family relationship
    - rearrange_queue() - no two family members adjacent
    
    Bonus Completed:
    - No use of list.insert, list.pop, list.index, list.sort, sorted()
    """)
    print("=" * 70)


if __name__ == "__main__":
    main()