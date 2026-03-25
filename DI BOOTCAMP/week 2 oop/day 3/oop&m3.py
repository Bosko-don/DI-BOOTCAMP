#!/usr/bin/env python3
"""
DUNDER METHODS & CLASSES EXERCISES
Topics: SOLID Principles, Quantum Physics Simulation, Temperature Conversion
"""

import random
from abc import ABC, abstractmethod

print("=" * 60)
print("🌟 EXERCISE 1: Temperature (SOLID Design)")
print("=" * 60)


# SOLID Design: Base class with abstract method, each class handles its own conversion
class Temperature(ABC):
    """Abstract base class for temperature scales"""
    
    def __init__(self, value):
        self.value = value
    
    @abstractmethod
    def to_celsius(self):
        """Convert to Celsius - base reference point"""
        pass
    
    @abstractmethod
    def to_kelvin(self):
        """Convert to Kelvin"""
        pass
    
    @abstractmethod
    def to_fahrenheit(self):
        """Convert to Fahrenheit"""
        pass
    
    def __repr__(self):
        return f"{self.__class__.__name__}({self.value})"
    
    def __str__(self):
        symbol = {'Celsius': '°C', 'Kelvin': 'K', 'Fahrenheit': '°F'}[self.__class__.__name__]
        return f"{self.value}{symbol}"
    
    def __eq__(self, other):
        """Compare two temperatures regardless of scale"""
        if not isinstance(other, Temperature):
            return False
        return self.to_celsius().value == other.to_celsius().value


class Celsius(Temperature):
    """Celsius temperature scale"""
    
    def to_celsius(self):
        return Celsius(self.value)
    
    def to_kelvin(self):
        return Kelvin(self.value + 273.15)
    
    def to_fahrenheit(self):
        return Fahrenheit((self.value * 9/5) + 32)


class Kelvin(Temperature):
    """Kelvin temperature scale"""
    
    def to_celsius(self):
        return Celsius(self.value - 273.15)
    
    def to_kelvin(self):
        return Kelvin(self.value)
    
    def to_fahrenheit(self):
        return Fahrenheit((self.value - 273.15) * 9/5 + 32)


class Fahrenheit(Temperature):
    """Fahrenheit temperature scale"""
    
    def to_celsius(self):
        return Celsius((self.value - 32) * 5/9)
    
    def to_kelvin(self):
        return Kelvin((self.value - 32) * 5/9 + 273.15)
    
    def to_fahrenheit(self):
        return Fahrenheit(self.value)


# Test Temperature conversions
print("\nTemperature Conversions:")
c = Celsius(25)
print(f"Starting: {c}")
print(f"  to Kelvin: {c.to_kelvin()}")
print(f"  to Fahrenheit: {c.to_fahrenheit()}")

f = Fahrenheit(98.6)
print(f"\nStarting: {f}")
print(f"  to Celsius: {f.to_celsius()}")
print(f"  to Kelvin: {f.to_kelvin()}")

k = Kelvin(0)
print(f"\nStarting: {k}")
print(f"  to Celsius: {k.to_celsius()}")
print(f"  to Fahrenheit: {k.to_fahrenheit()}")

# Test equality
print(f"\n25°C == 77°F ? {Celsius(25) == Fahrenheit(77)}")
print(f"0°C == 273.15K ? {Celsius(0) == Kelvin(273.15)}")


print("\n" + "=" * 60)
print("🌟 EXERCISE 2: Quantum Realm")
print("=" * 60)


class QuantumParticle:
    """Quantum particle with position, momentum, spin and entanglement"""
    
    _entangled_pairs = {}  # Class-level tracking of entangled pairs
    
    def __init__(self, x=None, y=None, p=None):
        # Initial values (can be None for random generation)
        self._initial_x = x
        self._initial_y = y
        self._initial_p = p
        
        # Current values (affected by measurements/disturbances)
        self._x = x
        self._y = y
        self._p = p
        
        # Spin state
        self._spin = None
        
        # Entanglement partner
        self.entangled_with = None
        
        # Particle ID for tracking
        self.id = id(self)
    
    def _disturbance(self):
        """Quantum disturbance - changes position and momentum randomly"""
        self._x = random.randint(1, 10000)
        self._y = random.random()  # Random float 0-1
        print("🔮 Quantum Interferences!!")
    
    def position(self):
        """Measure position - causes disturbance"""
        self._disturbance()
        return self._x
    
    def momentum(self):
        """Measure momentum - causes disturbance"""
        self._disturbance()
        return self._y
    
    def spin(self):
        """Measure spin - returns 1/2 or -1/2"""
        # Check if entangled - if partner was measured, we get opposite
        if self.entangled_with and self.entangled_with._spin is not None:
            self._spin = -self.entangled_with._spin
            print("🎆 Spooky Action at a Distance !!")
        else:
            # Random spin if not entangled or partner not measured
            self._spin = random.choice([0.5, -0.5])
        
        return self._spin
    
    def entangle(self, other):
        """Entangle this particle with another QuantumParticle"""
        if not isinstance(other, QuantumParticle):
            raise TypeError("Can only entangle with another QuantumParticle!")
        
        if self == other:
            raise ValueError("Cannot entangle a particle with itself!")
        
        self.entangled_with = other
        other.entangled_with = self
        
        # Track in class-level registry
        QuantumParticle._entangled_pairs[self.id] = other.id
        QuantumParticle._entangled_pairs[other.id] = self.id
        
        print(f"🌌 Particle {self.id} is now in quantum entanglement with Particle {other.id}")
        return self
    
    def __repr__(self):
        return (f"QuantumParticle(id={self.id}, x={self._x}, y={self._y}, "
                f"spin={self._spin}, entangled={self.entangled_with is not None})")
    
    def __str__(self):
        status = "entangled" if self.entangled_with else "single"
        return f"🔬 Quantum Particle #{self.id[:6] if isinstance(self.id, str) else self.id} [{status}]"


# Test Quantum Particle
print("\n--- Single Particle Tests ---")
p1 = QuantumParticle(x=1, p=5.0)
print(f"Created: {p1}")

print(f"\nPosition measurement: {p1.position()}")
print(f"Momentum measurement: {p1.momentum()}")
print(f"Spin measurement: {p1.spin()}")
print(f"After measurements: {p1}")

print("\n--- Entanglement Tests ---")
# Create two particles
particle1 = QuantumParticle(x=100, p=2.5)
particle2 = QuantumParticle(x=200, p=3.5)

print(f"Particle 1: {particle1}")
print(f"Particle 2: {particle2}")

# Entangle them
particle1.entangle(particle2)

# Measure spin of first - should affect second
print(f"\nMeasuring spin of particle 1: {particle1.spin()}")
print(f"Particle 1 spin: {particle1._spin}")
print(f"Particle 2 spin (should be opposite): {particle2._spin}")

# Test error handling
print("\n--- Error Handling ---")
try:
    particle1.entangle("not a particle")
except TypeError as e:
    print(f"✅ Caught expected error: {e}")

# Create new entangled pair with random properties
print("\n--- New Entangled Pair ---")
p3 = QuantumParticle()
p4 = QuantumParticle()
p3.entangle(p4)

# Measure position (causes disturbance)
print(f"\nP3 position: {p3.position()}")
print(f"P3 after disturbance: {p3}")

# Check if p4 was affected by entanglement (spin only, not position/momentum)
print(f"\nP4 spin (should trigger spooky action): {p4.spin()}")


print("\n" + "=" * 60)
print("ALL EXERCISES COMPLETED! 🎉")
print("=" * 60)