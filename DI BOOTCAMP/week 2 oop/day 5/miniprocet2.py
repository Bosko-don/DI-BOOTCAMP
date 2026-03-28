#!/usr/bin/env python3
"""
Rock Paper Scissors - Complete Single File Solution
Combines Game class and User Interface
"""

import random


class Game:
    """
    Game class containing all game logic for Rock Paper Scissors.
    """

    def __init__(self):
        """Initialize the Game."""
        self.choices = ["rock", "paper", "scissors"]

    def get_user_item(self):
        """
        Ask the user to select an item (rock/paper/scissors).
        Validates input and returns the user's choice.
        """
        while True:
            user_input = input("\nSelect an item (rock/paper/scissors): ").strip().lower()

            if user_input in self.choices:
                return user_input
            else:
                print("Invalid choice! Please type 'rock', 'paper', or 'scissors'.")

    def get_computer_item(self):
        """
        Randomly select an item (rock/paper/scissors).
        Returns the computer's choice.
        """
        return random.choice(self.choices)

    def get_game_result(self, user_item, computer_item):
        """
        Determine the result of the game based on the rules.
        Returns "win", "draw", or "loss".
        """
        if user_item == computer_item:
            return "draw"

        # Winning combinations for user
        win_conditions = {
            "rock": "scissors",
            "paper": "rock",
            "scissors": "paper"
        }

        if win_conditions[user_item] == computer_item:
            return "win"
        else:
            return "loss"

    def play(self):
        """
        Play a single game.
        Gets user and computer choices, determines result, prints outcome.
        Returns the result ("win", "draw", or "loss").
        """
        # Get choices
        user_item = self.get_user_item()
        computer_item = self.get_computer_item()

        # Determine result
        result = self.get_game_result(user_item, computer_item)

        # Print outcome
        print(f"\nYou chose: {user_item.upper()}")
        print(f"Computer chose: {computer_item.upper()}")

        if result == "win":
            print("Result: YOU WIN!")
        elif result == "draw":
            print("Result: DRAW!")
        else:
            print("Result: YOU LOSE!")

        return result


def get_user_menu_choice():
    """
    Display menu options and get user's choice.
    Validates input and returns the choice.
    """
    print("\n" + "=" * 40)
    print("MENU")
    print("=" * 40)
    print("(g) Play a new game")
    print("(x) Show scores and exit")
    print("=" * 40)

    while True:
        choice = input("Enter your choice (g/x): ").strip().lower()

        if choice in ["g", "x"]:
            return choice
        else:
            print("Invalid choice! Please enter 'g' to play or 'x' to exit.")


def print_results(results):
    """
    Print the game results in a user-friendly format.
    Thanks the user for playing.
    """
    print("\n" + "=" * 40)
    print("GAME SUMMARY")
    print("=" * 40)
    print(f"Wins:   {results.get('win', 0)}")
    print(f"Losses: {results.get('loss', 0)}")
    print(f"Draws:  {results.get('draw', 0)}")
    print(f"Total games played: {sum(results.values())}")
    print("=" * 40)

    # Calculate win rate
    total = sum(results.values())
    if total > 0:
        win_rate = (results.get('win', 0) / total) * 100
        print(f"Win rate: {win_rate:.1f}%")

    print("\nThank you for playing Rock Paper Scissors!")
    print("=" * 40)


def main():
    """
    Main function - runs the Rock Paper Scissors game.
    """
    print("=" * 50)
    print("    ROCK PAPER SCISSORS")
    print("=" * 50)
    print("Play against the computer!")
    print("=" * 50)

    # Initialize results dictionary
    results = {"win": 0, "loss": 0, "draw": 0}

    # Main game loop
    while True:
        choice = get_user_menu_choice()

        if choice == "g":
            # Play a new game
            game = Game()
            result = game.play()

            # Store result
            results[result] += 1

            print(f"\nCurrent score - Wins: {results['win']}, Losses: {results['loss']}, Draws: {results['draw']}")

        elif choice == "x":
            # Show results and exit
            print_results(results)
            break


if __name__ == "__main__":
    main()