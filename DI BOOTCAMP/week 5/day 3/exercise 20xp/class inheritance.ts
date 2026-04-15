// Base class
class Animal {
    public name: string;

    constructor(name: string) {
        this.name = name;
    }

    public makeSound(): string {
        return "Some generic animal sound";
    }
}

// Subclass extending Animal
class Dog extends Animal {
    constructor(name: string) {
        super(name); // Call parent constructor
    }

    // Override parent method
    public makeSound(): string {
        return "bark";
    }

    // Additional method specific to Dog
    public fetch(): string {
        return `${this.name} is fetching the ball!`;
    }
}

// Usage
const myDog = new Dog("Buddy");
console.log(myDog.makeSound()); // "bark" (overridden method)
console.log(myDog.name);        // "Buddy" (inherited property)

// Polymorphism example
const animal: Animal = new Dog("Rex");
console.log(animal.makeSound()); // "bark" (dynamic dispatch)