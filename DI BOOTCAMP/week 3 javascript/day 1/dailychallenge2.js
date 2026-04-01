// ============================================
// DAILY CHALLENGE: STAR PATTERN
// For loops and nested for loops
// ============================================

console.log("=== METHOD 1: Using One Loop ===\n");

let pattern1 = "";
for (let i = 1; i <= 6; i++) {
    pattern1 = pattern1 + "* ";
    console.log(pattern1.trim());
}


console.log("\n=== METHOD 2: Using Nested For Loops ===\n");

for (let i = 1; i <= 6; i++) {
    let row = "";
    for (let j = 1; j <= i; j++) {
        row = row + "* ";
    }
    console.log(row.trim());
}