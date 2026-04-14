// Demonstrates how to use if...else statements to control program flow

// Function that determines if a number is positive, negative, or zero
function checkNumber(num: number): string {
    if (num > 0) {
        return "The number is positive";
    } else if (num < 0) {
        return "The number is negative";
    } else {
        return "The number is zero";
    }
}

// Test the function with different values
console.log(checkNumber(10));   // Output: The number is positive
console.log(checkNumber(-5));   // Output: The number is negative
console.log(checkNumber(0));    // Output: The number is zero