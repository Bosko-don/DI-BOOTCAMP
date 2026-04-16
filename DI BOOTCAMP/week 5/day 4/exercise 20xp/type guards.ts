function describeValue(value: number | string): string {
    // Type guard using typeof
    if (typeof value === "number") {
        return "This is a number";
    } else {
        // TypeScript knows this must be string
        return "This is a string";
    }
}

// Test
console.log(describeValue(42));      // "This is a number"
console.log(describeValue("hello")); // "This is a string"