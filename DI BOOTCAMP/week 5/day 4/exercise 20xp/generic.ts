// T constrained to have a length property
function logLength<T extends { length: number }>(item: T): void {
    console.log(`Length: ${item.length}`);
}

// Works with strings
logLength("Hello");        // Length: 5

// Works with arrays
logLength([1, 2, 3, 4]);   // Length: 4

// Works with any object with length property
logLength({ length: 10 }); // Length: 10

// Error: number doesn't have length property
// logLength(42); // ❌ Compile error