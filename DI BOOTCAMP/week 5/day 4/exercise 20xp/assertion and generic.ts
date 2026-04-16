// Generic with constraint: T must have toString() method
function formatInput<T extends { toString(): string }>(input: T): string {
    // Type assertion: ensure TypeScript treats it as string
    const strValue = input.toString() as string;
    
    // Format the string
    return `Formatted: [${strValue.toUpperCase()}]`;
}

// Test with different types that have toString()
console.log(formatInput(42));                    // "Formatted: [42]"
console.log(formatInput(true));                  // "Formatted: [TRUE]"
console.log(formatInput("hello"));               // "Formatted: [HELLO]"
console.log(formatInput([1, 2, 3]));             // "Formatted: [1,2,3]"
console.log(formatInput(new Date("2024-01-01"))); // "Formatted: [MON JAN 01 2024...]"

// Custom object with toString()
class Person {
    constructor(public name: string) {}
    toString(): string {
        return `Person: ${this.name}`;
    }
}

console.log(formatInput(new Person("Alice")));   // "Formatted: [PERSON: ALICE]"