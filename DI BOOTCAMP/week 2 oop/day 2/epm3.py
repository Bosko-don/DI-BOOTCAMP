#!/usr/bin/env python3
"""
CONWAY'S GAME OF LIFE
Topics: Inheritance, Classes, 2D Arrays, Simulation
"""

import random
import time
import os


class Cell:
    """Represents a single cell in the grid"""
    def __init__(self, alive=False):
        self.alive = alive
    
    def __str__(self):
        return "■" if self.alive else "□"


class Grid:
    """Represents the game grid"""
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.generation = 0
        # Create 2D grid of cells
        self.cells = [[Cell() for _ in range(cols)] for _ in range(rows)]
    
    def randomize(self, density=0.3):
        """Randomly populate grid with live cells"""
        for row in range(self.rows):
            for col in range(self.cols):
                self.cells[row][col].alive = random.random() < density
    
    def set_pattern(self, pattern_name):
        """Set specific initial patterns"""
        # Clear grid first
        for row in range(self.rows):
            for col in range(self.cols):
                self.cells[row][col].alive = False
        
        center_row = self.rows // 2
        center_col = self.cols // 2
        
        if pattern_name == "glider":
            # Glider pattern
            coords = [(0, 1), (1, 2), (2, 0), (2, 1), (2, 2)]
        elif pattern_name == "blinker":
            # Blinker (oscillator)
            coords = [(0, 1), (1, 1), (2, 1)]
        elif pattern_name == "block":
            # Still life (2x2 block)
            coords = [(0, 0), (0, 1), (1, 0), (1, 1)]
        elif pattern_name == "beacon":
            # Beacon
            coords = [(0, 0), (0, 1), (1, 0), (1, 1), (2, 2), (2, 3), (3, 2), (3, 3)]
        elif pattern_name == "gosper":
            # Gosper Glider Gun (simplified)
            coords = [
                (5, 1), (5, 2), (6, 1), (6, 2),
                (5, 11), (6, 11), (7, 11), (4, 12), (8, 12),
                (3, 13), (9, 13), (3, 14), (9, 14), (6, 15),
                (4, 16), (8, 16), (5, 17), (6, 17), (7, 17), (6, 18)
            ]
        else:
            return
        
        # Place pattern at center
        for dr, dc in coords:
            r = center_row + dr
            c = center_col + dc
            if 0 <= r < self.rows and 0 <= c < self.cols:
                self.cells[r][c].alive = True
    
    def count_neighbors(self, row, col):
        """Count live neighbors for a cell"""
        count = 0
        for dr in [-1, 0, 1]:
            for dc in [-1, 0, 1]:
                if dr == 0 and dc == 0:
                    continue
                nr, nc = row + dr, col + dc
                # Fixed borders - cells outside are dead
                if 0 <= nr < self.rows and 0 <= nc < self.cols:
                    if self.cells[nr][nc].alive:
                        count += 1
        return count
    
    def next_generation(self):
        """Apply Game of Life rules to create next generation"""
        # Create new grid state
        new_alive = [[False for _ in range(self.cols)] for _ in range(self.rows)]
        
        for row in range(self.rows):
            for col in range(self.cols):
                neighbors = self.count_neighbors(row, col)
                current = self.cells[row][col].alive
                
                # Apply Conway's rules
                if current:  # Live cell
                    if neighbors < 2:  # Underpopulation
                        new_alive[row][col] = False
                    elif neighbors in [2, 3]:  # Survival
                        new_alive[row][col] = True
                    else:  # Overpopulation (>3)
                        new_alive[row][col] = False
                else:  # Dead cell
                    if neighbors == 3:  # Reproduction
                        new_alive[row][col] = True
                    else:
                        new_alive[row][col] = False
        
        # Update grid
        for row in range(self.rows):
            for col in range(self.cols):
                self.cells[row][col].alive = new_alive[row][col]
        
        self.generation += 1
    
    def display(self):
        """Print the grid"""
        os.system('cls' if os.name == 'nt' else 'clear')
        print(f"=== CONWAY'S GAME OF LIFE ===  Generation: {self.generation}")
        print("=" * (self.cols * 2 + 4))
        
        for row in range(self.rows):
            line = "  "
            for col in range(self.cols):
                line += str(self.cells[row][col]) + " "
            print(line)
        
        print("=" * (self.cols * 2 + 4))
        print("Rules: ■ = Alive, □ = Dead")
        print("Press Ctrl+C to stop")
    
    def is_empty(self):
        """Check if all cells are dead"""
        for row in range(self.rows):
            for col in range(self.cols):
                if self.cells[row][col].alive:
                    return False
        return True
    
    def is_static(self):
        """Check if grid hasn't changed (simplified - would need history)"""
        # For simplicity, we check if empty
        return self.is_empty()


class GameOfLife:
    """Main game controller"""
    def __init__(self, rows=20, cols=40):
        self.grid = Grid(rows, cols)
    
    def run_random(self, generations=100, delay=0.2):
        """Run with random initial state"""
        self.grid.randomize()
        self._run_simulation(generations, delay)
    
    def run_pattern(self, pattern, generations=100, delay=0.2):
        """Run with specific pattern"""
        self.grid.set_pattern(pattern)
        self._run_simulation(generations, delay)
    
    def _run_simulation(self, max_generations, delay):
        """Run the simulation loop"""
        try:
            for _ in range(max_generations):
                self.grid.display()
                
                if self.grid.is_empty():
                    print("\nAll cells died! Game over.")
                    break
                
                time.sleep(delay)
                self.grid.next_generation()
            
            print(f"\nSimulation completed after {self.grid.generation} generations")
            
        except KeyboardInterrupt:
            print(f"\n\nStopped by user at generation {self.grid.generation}")


def main():
    """Main menu to test different initial states"""
    print("=" * 50)
    print("CONWAY'S GAME OF LIFE")
    print("=" * 50)
    print("\nChoose initial pattern:")
    print("1. Random (30% density)")
    print("2. Glider (moves diagonally)")
    print("3. Blinker (oscillator)")
    print("4. Block (still life)")
    print("5. Beacon (oscillator)")
    print("6. Gosper Glider Gun")
    print("7. Quit")
    
    choice = input("\nEnter choice (1-7): ").strip()
    
    if choice == "7" or choice == "":
        print("Goodbye!")
        return
    
    # Create game with 20x40 grid
    game = GameOfLife(rows=20, cols=40)
    
    patterns = {
        "2": "glider",
        "3": "blinker",
        "4": "block",
        "5": "beacon",
        "6": "gosper"
    }
    
    if choice == "1":
        game.run_random(generations=200, delay=0.15)
    elif choice in patterns:
        game.run_pattern(patterns[choice], generations=200, delay=0.3)
    else:
        print("Invalid choice!")


if __name__ == "__main__":
    main()