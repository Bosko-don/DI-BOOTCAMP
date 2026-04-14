// Demonstrates how to use tuple types and return multiple values from a function

// Function that returns a tuple with name, age, and greeting message
function getDetails(userName: string, age: number): [string, number, string] {
    const greeting = `Hello, ${userName}! You are ${age} years old.`;
    return [userName, age, greeting];
}

// Call the function and log the tuple
const details = getDetails("Alice", 25);

// Expected output: ['Alice', 25, 'Hello, Alice! You are 25 years old.']
console.log(details);