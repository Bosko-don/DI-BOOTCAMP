// Demonstrates how to use type assertions to cast HTML elements

// Get an element from the DOM and cast it to a specific type
const inputElement = document.getElementById("myInput") as HTMLInputElement;

// Now we can safely access properties specific to HTMLInputElement
inputElement.value = "Hello, TypeScript!";

// Access and log the value
console.log("Input value:", inputElement.value);

// Another example with different element types
const buttonElement = document.getElementById("myButton") as HTMLButtonElement;
buttonElement.disabled = true;

// Note: Ensure the element exists in your HTML before running this code:
// <input id="myInput" type="text">
// <button id="myButton">Click me</button>