// Create Animal class
class Animal {
    constructor(name, type, color) {
        this.name = name;
        this.type = type;
        this.color = color;
    }
}

// Create Mammal class that extends Animal
class Mammal extends Animal {
    constructor(name, type, color) {
        super(name, type, color);
    }
    
    sound(animalSound) {
        return `${animalSound} I'm a ${this.type}, named ${this.name} and I'm ${this.color}`;
    }
}

// Create farmerCow object
const farmerCow = new Mammal('Lily', 'cow', 'brown and white');

// Call the sound method
console.log(farmerCow.sound('Moooo'));
// Output: "Moooo I'm a cow, named Lily and I'm brown and white"