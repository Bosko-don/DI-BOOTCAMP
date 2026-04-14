// Demonstrates how to define object structures using type annotations

// Define the Person type annotation
interface Person {
    userName: string;  // Changed from 'name' to 'userName'
    age: number;
}

// Function that creates and returns a Person object
function createPerson(userName: string, age: number): Person {
    return {
        userName: userName,
        age: age
    };
}

// Test the function by creating a person and logging the result
const person = createPerson("Alice", 25);
console.log(person);  // Output: { userName: 'Alice', age: 25 }