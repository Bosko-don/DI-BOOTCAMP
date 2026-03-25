#!/usr/bin/env python3
"""
CIRCLE CLASS WITH DUNDER METHODS
Topics: OOP, Property Decorators, Magic Methods
"""

import math


class Circle:
    """A circle class with radius/diameter properties and dunder methods"""
    
    def __init__(self, radius=None, diameter=None):
        """Initialize circle with radius OR diameter"""
        if radius is not None and diameter is not None:
            raise ValueError("Specify radius OR diameter, not both!")
        
        if radius is not None:
            if radius < 0:
                raise ValueError("Radius cannot be negative!")
            self._radius = radius
        
        elif diameter is not None:
            if diameter < 0:
                raise ValueError("Diameter cannot be negative!")
            self._radius = diameter / 2
        
        else:
            raise ValueError("Must specify radius or diameter!")
    
    # Property decorator for radius
    @property
    def radius(self):
        """Get radius"""
        return self._radius
    
    @radius.setter
    def radius(self, value):
        """Set radius"""
        if value < 0:
            raise ValueError("Radius cannot be negative!")
        self._radius = value
    
    # Property decorator for diameter
    @property
    def diameter(self):
        """Get diameter (2 * radius)"""
        return self._radius * 2
    
    @diameter.setter
    def diameter(self, value):
        """Set diameter (updates radius)"""
        if value < 0:
            raise ValueError("Diameter cannot be negative!")
        self._radius = value / 2
    
    # Compute area
    def area(self):
        """Calculate circle area: πr²"""
        return math.pi * (self._radius ** 2)
    
    # Dunder methods
    
    def __str__(self):
        """User-friendly string representation"""
        return f"Circle(radius={self._radius:.2f}, diameter={self.diameter:.2f}, area={self.area():.2f})"
    
    def __repr__(self):
        """Official representation for debugging"""
        return f"Circle(radius={self._radius})"
    
    def __add__(self, other):
        """Add two circles: new circle with combined radius"""
        if not isinstance(other, Circle):
            raise TypeError("Can only add Circle to Circle!")
        new_radius = self._radius + other._radius
        return Circle(radius=new_radius)
    
    def __gt__(self, other):
        """Compare: is this circle bigger than other?"""
        if not isinstance(other, Circle):
            raise TypeError("Can only compare Circle to Circle!")
        return self._radius > other._radius
    
    def __eq__(self, other):
        """Compare: are circles equal?"""
        if not isinstance(other, Circle):
            return False
        return self._radius == other._radius
    
    def __lt__(self, other):
        """Compare: is this circle smaller than other? (for sorting)"""
        if not isinstance(other, Circle):
            raise TypeError("Can only compare Circle to Circle!")
        return self._radius < other._radius
    
    def __le__(self, other):
        """Less than or equal"""
        return self < other or self == other
    
    def __ge__(self, other):
        """Greater than or equal"""
        return self > other or self == other
    
    def __len__(self):
        """Return circumference as 'length'"""
        return int(2 * math.pi * self._radius)


# ============================================================
# TESTING THE CIRCLE CLASS
# ============================================================

def main():
    print("=" * 60)
    print("🎯 CIRCLE CLASS TESTS")
    print("=" * 60)
    
    # Test 1: Create circles with radius
    print("\n--- Creating Circles ---")
    c1 = Circle(radius=5)
    print(f"Circle 1 (radius=5): {c1}")
    print(f"  Area: {c1.area():.2f}")
    print(f"  Diameter: {c1.diameter}")
    
    # Test 2: Create circle with diameter
    c2 = Circle(diameter=20)  # radius = 10
    print(f"\nCircle 2 (diameter=20): {c2}")
    
    # Test 3: Property decorators
    print("\n--- Property Tests ---")
    c1.diameter = 30  # Should set radius to 15
    print(f"After setting diameter=30: {c1}")
    
    c1.radius = 8
    print(f"After setting radius=8: {c1}")
    
    # Test 4: Add circles
    print("\n--- Adding Circles ---")
    c3 = Circle(radius=3)
    c4 = Circle(radius=4)
    c5 = c3 + c4
    print(f"{c3} + {c4} = {c5}")
    
    # Test 5: Comparisons
    print("\n--- Comparisons ---")
    a = Circle(radius=5)
    b = Circle(radius=10)
    c = Circle(radius=5)
    
    print(f"Circle a: {a}")
    print(f"Circle b: {b}")
    print(f"Circle c: {c}")
    
    print(f"\na > b? {a > b}")  # False
    print(f"b > a? {b > a}")    # True
    print(f"a == c? {a == c}")  # True
    print(f"a == b? {a == b}")  # False
    
    # Test 6: Sorting circles
    print("\n--- Sorting Circles ---")
    circles = [
        Circle(radius=3),
        Circle(radius=10),
        Circle(radius=1),
        Circle(radius=7),
        Circle(radius=5)
    ]
    
    print("Unsorted circles:")
    for c in circles:
        print(f"  {c}")
    
    circles.sort()  # Uses __lt__
    
    print("\nSorted circles (smallest to largest):")
    for c in circles:
        print(f"  {c}")
    
    # Test 7: Circumference (len)
    print("\n--- Circumference ---")
    c = Circle(radius=5)
    print(f"Circle with radius 5 has circumference ≈ {len(c)}")
    
    # Test 8: Error handling
    print("\n--- Error Handling ---")
    try:
        bad = Circle(radius=-5)
    except ValueError as e:
        print(f"✅ Caught error: {e}")
    
    try:
        bad = Circle()  # No radius or diameter
    except ValueError as e:
        print(f"✅ Caught error: {e}")


# ============================================================
# BONUS: TURTLE VISUALIZATION
# ============================================================

def bonus_turtle_visualization():
    """Draw circles using turtle graphics"""
    try:
        import turtle
        
        print("\n" + "=" * 60)
        print("🐢 BONUS: TURTLE VISUALIZATION")
        print("=" * 60)
        
        # Create sorted circles
        circles = [
            Circle(radius=20),
            Circle(radius=50),
            Circle(radius=30),
            Circle(radius=80),
            Circle(radius=40)
        ]
        circles.sort()
        
        # Setup turtle
        screen = turtle.Screen()
        screen.title("Sorted Circles Visualization")
        screen.setup(width=800, height=600)
        
        t = turtle.Turtle()
        t.speed(0)  # Fastest
        
        # Draw circles side by side
        x_position = -300
        
        for i, circle in enumerate(circles):
            t.penup()
            t.goto(x_position, -circle.radius)  # Center the circle
            t.pendown()
            
            # Color based on size
            colors = ["red", "orange", "yellow", "green", "blue"]
            t.pencolor(colors[i % len(colors)])
            t.fillcolor(colors[i % len(colors)])
            
            t.begin_fill()
            t.circle(circle.radius)
            t.end_fill()
            
            # Label
            t.penup()
            t.goto(x_position, -circle.radius - 30)
            t.write(f"r={circle.radius}", align="center", font=("Arial", 10, "bold"))
            
            x_position += circle.radius * 2 + 20  # Move to next position
        
        t.hideturtle()
        print("Close the turtle window to continue...")
        screen.mainloop()
        
    except ImportError:
        print("\n⚠️ Turtle not installed. Run: pip install PythonTurtle")
        print("Skipping visualization.")


if __name__ == "__main__":
    main()
    
    # Ask about bonus
    response = input("\nRun turtle visualization? (y/n): ").strip().lower()
    if response == 'y':
        bonus_turtle_visualization()
    
    print("\n" + "=" * 60)
    print("ALL TESTS COMPLETED! 🎉")
    print("=" * 60)