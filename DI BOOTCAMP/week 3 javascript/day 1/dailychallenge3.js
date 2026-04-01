// ============================================
// DAILY CHALLENGE GOLD: Bubble Sort
// Array methods, loops, nested for loops
// ============================================

const numbers = [5, 0, 9, 1, 7, 4, 2, 6, 3, 8];

console.log("=== PART 1: Convert Array to String ===\n");

// Using .toString() method
let stringWithCommas = numbers.toString();
console.log("Using .toString():", stringWithCommas);

// Using .join() with different separators
console.log("\nUsing .join(\"+\"):", numbers.join("+"));
console.log("Using .join(\" \"):", numbers.join(" "));
console.log("Using .join(\"\"):", numbers.join(""));
console.log("Using .join(\"-\"):", numbers.join("-"));
console.log("Using .join(\" | \"):", numbers.join(" | "));


console.log("\n=== PART 2: Bubble Sort (Descending Order) ===\n");

// Create a copy of the array to sort (so we don't modify original for demonstration)
let arr = [5, 0, 9, 1, 7, 4, 2, 6, 3, 8];
console.log("Original array:", arr);

// BUBBLE SORT ALGORITHM
// We use nested for loops to compare adjacent elements
// Outer loop: controls how many times we pass through the array
// Inner loop: compares adjacent elements and swaps if needed

// Outer loop - we need to make multiple passes through the array
// We go through the array arr.length times to ensure everything is sorted
for (let i = 0; i < arr.length; i++) {
    
    // Inner loop - compare adjacent elements
    // We go from start to end, but we can subtract i because
    // after each pass, the largest element "bubbles up" to the end
    for (let j = 0; j < arr.length - 1 - i; j++) {
        
        // Compare current element with next element
        // For DESCENDING order: we want larger numbers first
        // So if current element is SMALLER than next, we swap
        if (arr[j] < arr[j + 1]) {
            
            // SWAP using temporary variable
            // Store current value temporarily
            let temp = arr[j];
            // Put next value in current position
            arr[j] = arr[j + 1];
            // Put temp value (original current) in next position
            arr[j + 1] = temp;
            
            // Log the swap for understanding
            console.log(`Swapped ${arr[j + 1]} and ${arr[j]}: [${arr.join(", ")}]`);
        }
    }
    
    // Log progress after each full pass
    console.log(`After pass ${i + 1}: [${arr.join(", ")}]`);
}

console.log("\n=== FINAL SORTED ARRAY (Descending) ===");
console.log(arr);

// Verification
console.log("\nExpected: [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]");
console.log("Got:     [" + arr.join(", ") + "]");