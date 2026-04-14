// Demonstrates how to use union types to allow multiple types for a variable

// Declare a variable that can be either a string or a number
let id: string | number;

// Assign different types to the variable
id = "abc123";  // string value
console.log("ID (string):", id);

id = 456;       // number value
console.log("ID (number):", id);