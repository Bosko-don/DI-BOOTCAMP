// Demonstrates how to create overloaded functions with default parameters

// Function overload declarations
function greet(): string;
function greet(userName: string): string;

// Function implementation with default parameter
function greet(userName?: string): string {
    if (userName) {
        return `Hello, ${userName}! Welcome!`;
    } else {
        return "Hello, stranger! Welcome!";
    }
}

// Test the function
console.log(greet());           // Output: Hello, stranger! Welcome!
console.log(greet("Alice"));    // Output: Hello, Alice! Welcome!