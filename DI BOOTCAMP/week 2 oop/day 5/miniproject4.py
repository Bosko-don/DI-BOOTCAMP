#!/usr/bin/env python3
"""
OOP Quiz and Deck of Cards - Complete Solution
Exercise 1: OOP Theory Answers
Exercise 2: Deck of Cards Implementation
"""

import random


# ============================================================================
# EXERCISE 1: OOP THEORY ANSWERS
# ============================================================================

def display_oop_answers():
    """Display answers to Exercise 1 OOP questions."""

    answers = """
    =========================================================================
                            EXERCISE 1: OOP QUIZ ANSWERS
    =========================================================================
    
    1. WHAT IS A CLASS?
       A class is a blueprint or template for creating objects. It defines 
       the attributes (data) and methods (functions) that objects created from 
       the class will have. Think of it as a cookie cutter - the class is the 
       cutter, and objects are the cookies.
       
       Example: class Dog: defines what a Dog is (name, age, bark())
    
    2. WHAT IS AN INSTANCE?
       An instance is a specific object created from a class. When you create 
       an object using the class blueprint, that object is called an instance 
       of the class.
       
       Example: my_dog = Dog("Buddy", 3) - my_dog is an instance of Dog
    
    3. WHAT IS ENCAPSULATION?
       Encapsulation is the bundling of data (attributes) and methods that 
       operate on that data within a single unit (class), while restricting 
       direct access to some components. It hides internal implementation 
       details and exposes only what's necessary.
       
       Example: Private attributes (self.__balance) with public getter/setter
    
    4. WHAT IS ABSTRACTION?
       Abstraction is hiding complex implementation details and showing only 
       the essential features of an object. It reduces complexity by allowing 
       users to interact with high-level concepts rather than low-level details.
       
       Example: You drive a car using steering wheel, not by controlling 
                individual engine components
    
    5. WHAT IS INHERITANCE?
       Inheritance allows a new class (child/subclass) to inherit attributes 
       and methods from an existing class (parent/superclass). It promotes 
       code reuse and establishes "is-a" relationships.
       
       Example: class GoldenRetriever(Dog) inherits from Dog class
    
    6. WHAT IS MULTIPLE INHERITANCE?
       Multiple inheritance allows a class to inherit from more than one 
       parent class. The child class gets attributes and methods from all 
       parent classes.
       
       Example: class FlyingDog(Dog, Bird) inherits from both Dog and Bird
       
       Note: Python supports multiple inheritance. Some languages like Java 
       do not (they use interfaces instead).
    
    7. WHAT IS POLYMORPHISM?
       Polymorphism means "many forms." It allows objects of different classes 
       to be treated as objects of a common parent class, and the same method 
       call can behave differently based on the object's actual class.
       
       Example: speak() method works differently for Dog ("Woof") vs Cat ("Meow")
    
    8. WHAT IS METHOD RESOLUTION ORDER (MRO)?
       MRO is the order in which Python looks for a method in a class hierarchy, 
       especially important in inheritance (especially multiple inheritance). 
       It defines the sequence of classes Python searches when looking for a method.
       
       Example: In class C(A, B), MRO determines whether A or B's method is used
       
       You can view MRO using: ClassName.__mro__ or help(ClassName)
    
    =========================================================================
    """
    
    print(answers)


# ============================================================================
# EXERCISE 2: CARD CLASS
# ============================================================================

class Card:
    """
    Represents a playing card with a suit and value.
    
    Attributes:
        suit (str): Hearts, Diamonds, Clubs, or Spades
        value (str): A, 2, 3, 4, 5, 6, 7, 8, 9, 10, J, Q, or K
    """
    
    # Class-level constants for valid suits and values
    SUITS = ["Hearts", "Diamonds", "Clubs", "Spades"]
    VALUES = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
    
    def __init__(self, suit, value):
        """
        Initialize a Card with suit and value.
        
        Args:
            suit (str): The card's suit
            value (str): The card's value
        """
        if suit not in self.SUITS:
            raise ValueError(f"Invalid suit: {suit}. Must be one of {self.SUITS}")
        if value not in self.VALUES:
            raise ValueError(f"Invalid value: {value}. Must be one of {self.VALUES}")
        
        self.suit = suit
        self.value = value
    
    def __str__(self):
        """Return string representation of the card."""
        return f"{self.value} of {self.suit}"
    
    def __repr__(self):
        """Return detailed representation for debugging."""
        return f"Card('{self.suit}', '{self.value}')"
    
    def get_numeric_value(self):
        """
        Get numeric value for comparison (A=1, 2-10=face value, J=11, Q=12, K=13).
        """
        value_map = {
            "A": 1,
            "J": 11,
            "Q": 12,
            "K": 13
        }
        return value_map.get(self.value, int(self.value))
    
    def __eq__(self, other):
        """Check if two cards are equal."""
        if not isinstance(other, Card):
            return False
        return self.suit == other.suit and self.value == other.value
    
    def __lt__(self, other):
        """Compare cards for sorting."""
        if not isinstance(other, Card):
            return NotImplemented
        return self.get_numeric_value() < other.get_numeric_value()


# ============================================================================
# EXERCISE 2: DECK CLASS (Does NOT inherit from Card)
# ============================================================================

class Deck:
    """
    Represents a deck of 52 playing cards.
    
    The Deck class does NOT inherit from Card (as per requirements).
    Instead, it contains Card objects in a list.
    
    Attributes:
        cards (list): List of Card objects in the deck
    """
    
    def __init__(self):
        """
        Initialize a new deck with all 52 cards.
        Creates cards in order: Hearts A-K, Diamonds A-K, Clubs A-K, Spades A-K
        """
        self.cards = []
        self._create_deck()
    
    def _create_deck(self):
        """
        Create all 52 cards and add them to the deck.
        Private method (encapsulation).
        """
        self.cards = []
        for suit in Card.SUITS:
            for value in Card.VALUES:
                self.cards.append(Card(suit, value))
    
    def shuffle(self):
        """
        Shuffle the deck randomly.
        
        First checks that all 52 cards are present, then rearranges them randomly.
        """
        # Verify deck is complete (52 cards, all unique)
        if len(self.cards) != 52:
            print(f"Warning: Deck has {len(self.cards)} cards. Recreating deck...")
            self._create_deck()
        
        # Check for duplicates (optional validation)
        unique_cards = set((card.suit, card.value) for card in self.cards)
        if len(unique_cards) != 52:
            print("Warning: Duplicate cards found. Recreating deck...")
            self._create_deck()
        
        # Shuffle the deck in place
        random.shuffle(self.cards)
        print("Deck shuffled successfully!")
    
    def deal(self):
        """
        Deal a single card from the top of the deck.
        
        Returns:
            Card: The dealt card
            
        Raises:
            ValueError: If the deck is empty
        """
        if not self.cards:
            raise ValueError("Cannot deal from an empty deck!")
        
        # Remove and return the top card (last card in list for efficiency)
        return self.cards.pop()
    
    def deal_hand(self, num_cards):
        """
        Deal multiple cards at once.
        
        Args:
            num_cards (int): Number of cards to deal
            
        Returns:
            list: List of dealt Card objects
        """
        if num_cards > len(self.cards):
            raise ValueError(f"Cannot deal {num_cards} cards. Only {len(self.cards)} remaining.")
        
        hand = []
        for _ in range(num_cards):
            hand.append(self.deal())
        return hand
    
    def reset(self):
        """
        Reset the deck to a new, unshuffled state with all 52 cards.
        """
        self._create_deck()
        print("Deck reset to original state (unshuffled).")
    
    def count(self):
        """Return the number of cards remaining in the deck."""
        return len(self.cards)
    
    def is_empty(self):
        """Check if the deck is empty."""
        return len(self.cards) == 0
    
    def peek(self, num_cards=1):
        """
        Look at the top card(s) without removing them.
        
        Args:
            num_cards (int): Number of cards to peek at
            
        Returns:
            Card or list: Single card or list of cards
        """
        if num_cards == 1:
            return self.cards[-1] if self.cards else None
        return self.cards[-num_cards:] if len(self.cards) >= num_cards else self.cards[:]
    
    def __str__(self):
        """Return string representation of the deck."""
        return f"Deck of {len(self.cards)} cards"
    
    def __repr__(self):
        """Return detailed representation for debugging."""
        return f"Deck(cards={len(self.cards)})"
    
    def display(self):
        """Display all cards in the deck (for debugging)."""
        print(f"\nCurrent deck ({len(self.cards)} cards):")
        for i, card in enumerate(self.cards, 1):
            print(f"  {i:2d}. {card}")


# ============================================================================
# DEMONSTRATION AND TESTING
# ============================================================================

def demonstrate_card_class():
    """Demonstrate the Card class functionality."""
    print("\n" + "=" * 70)
    print("CARD CLASS DEMONSTRATION")
    print("=" * 70)
    
    # Create individual cards
    card1 = Card("Hearts", "A")
    card2 = Card("Spades", "K")
    card3 = Card("Diamonds", "10")
    
    print(f"\nCreated cards:")
    print(f"  Card 1: {card1}")
    print(f"  Card 2: {card2}")
    print(f"  Card 3: {card3}")
    
    print(f"\nCard details:")
    print(f"  {card1} has numeric value: {card1.get_numeric_value()}")
    print(f"  {card2} has numeric value: {card2.get_numeric_value()}")
    print(f"  {card3} has numeric value: {card3.get_numeric_value()}")
    
    print(f"\nComparison:")
    print(f"  {card1} == {card1}: {card1 == card1}")
    print(f"  {card1} < {card2}: {card1 < card2}")
    print(f"  {card3} > {card1}: {card3 > card1}")
    
    # Show representation
    print(f"\nRepresentation (repr): {repr(card1)}")


def demonstrate_deck_class():
    """Demonstrate the Deck class functionality."""
    print("\n" + "=" * 70)
    print("DECK CLASS DEMONSTRATION")
    print("=" * 70)
    
    # Create a new deck
    deck = Deck()
    print(f"\n1. Created new deck:")
    print(f"   {deck}")
    print(f"   Cards remaining: {deck.count()}")
    
    # Show first few cards (unshuffled)
    print(f"\n2. Top 5 cards (unshuffled):")
    top_cards = deck.peek(5)
    for card in top_cards:
        print(f"   {card}")
    
    # Shuffle the deck
    print(f"\n3. Shuffling deck...")
    deck.shuffle()
    
    # Show first few cards after shuffle
    print(f"\n4. Top 5 cards (after shuffle):")
    top_cards = deck.peek(5)
    for card in top_cards:
        print(f"   {card}")
    
    # Deal a single card
    print(f"\n5. Dealing single card...")
    dealt_card = deck.deal()
    print(f"   Dealt: {dealt_card}")
    print(f"   Cards remaining: {deck.count()}")
    
    # Deal a hand of 5 cards
    print(f"\n6. Dealing hand of 5 cards...")
    hand = deck.deal_hand(5)
    print(f"   Hand dealt:")
    for card in hand:
        print(f"     {card}")
    print(f"   Cards remaining: {deck.count()}")
    
    # Deal multiple hands
    print(f"\n7. Dealing 3 hands of 5 cards each...")
    for i in range(3):
        hand = deck.deal_hand(5)
        print(f"   Hand {i+1}: {[str(c) for c in hand]}")
    print(f"   Cards remaining: {deck.count()}")
    
    # Test empty deck handling
    print(f"\n8. Testing empty deck handling...")
    cards_remaining = deck.count()
    print(f"   Dealing all {cards_remaining} remaining cards...")
    try:
        while not deck.is_empty():
            deck.deal()
        print(f"   All cards dealt. Deck empty: {deck.is_empty()}")
        
        # Try to deal from empty deck
        print(f"   Attempting to deal from empty deck...")
        deck.deal()
    except ValueError as e:
        print(f"   Caught expected error: {e}")
    
    # Reset deck
    print(f"\n9. Resetting deck...")
    deck.reset()
    print(f"   {deck}")
    print(f"   Cards remaining: {deck.count()}")


def demonstrate_game_scenario():
    """Demonstrate a realistic card game scenario."""
    print("\n" + "=" * 70)
    print("CARD GAME SCENARIO: Poker Hand")
    print("=" * 70)
    
    deck = Deck()
    deck.shuffle()
    
    print("\nDealing 2-player poker game:")
    print("-" * 40)
    
    # Deal 2 cards to each player
    player1_hand = deck.deal_hand(2)
    player2_hand = deck.deal_hand(2)
    
    print(f"Player 1 hand: {[str(c) for c in player1_hand]}")
    print(f"Player 2 hand: {[str(c) for c in player2_hand]}")
    
    # Deal community cards (5 cards)
    print("\nDealing 5 community cards:")
    community_cards = deck.deal_hand(5)
    for i, card in enumerate(community_cards, 1):
        print(f"  Card {i}: {card}")
    
    print(f"\nCards remaining in deck: {deck.count()}")


def main():
    """Main function to run all demonstrations."""
    print("\n" + "=" * 70)
    print("OOP QUIZ AND DECK OF CARDS - COMPLETE SOLUTION")
    print("=" * 70)
    
    # Display Exercise 1 answers
    display_oop_answers()
    
    # Demonstrate Exercise 2
    demonstrate_card_class()
    demonstrate_deck_class()
    demonstrate_game_scenario()
    
    # Final summary
    print("\n" + "=" * 70)
    print("SUMMARY")
    print("=" * 70)
    print("""
    Exercise 1: All 8 OOP concepts explained with examples.
    
    Exercise 2: Deck of Cards implemented with:
               - Card class (suit + value)
               - Deck class (NO inheritance from Card)
               - shuffle() method (verifies 52 cards, then randomizes)
               - deal() method (removes and returns top card)
               - Additional features: deal_hand(), reset(), count(), etc.
    
    All requirements met!
    """)
    print("=" * 70)


if __name__ == "__main__":
    main()