// ============================================
// JAVASCRIPT STRING METHODS EXERCISE
// Use Javascript string and array methods
// Use conditionals statement
// ============================================

// Create a sentence containing "not" and "bad"
let sentence = "The movie is not that bad, I like it";

console.log("Original sentence:", sentence);

// Find the position of "not"
let wordNot = sentence.indexOf("not");

// Find the position of "bad"
let wordBad = sentence.indexOf("bad");

console.log('Position of "not":', wordNot);
console.log('Position of "bad":', wordBad);

// Check if "bad" comes after "not" and both exist in the sentence
if (wordNot !== -1 && wordBad !== -1 && wordBad > wordNot) {
    // Replace "not...bad" with "good"
    // Extract the part before "not"
    let beforeNot = sentence.slice(0, wordNot);
    
    // Extract the part after "bad"
    // "bad" is 3 characters long, so we start after wordBad + 3
    let afterBad = sentence.slice(wordBad + 3);
    
    // Combine with "good" in the middle
    let result = beforeNot + "good" + afterBad;
    
    console.log("Result:", result);
} else {
    // "bad" doesn't come after "not" or words not found
    console.log("Result:", sentence);
}


// ============================================
// TEST WITH OTHER EXAMPLES
// ============================================

console.log("\n--- Test 1 ---");
let sentence1 = "This dinner is not that bad ! You cook well";
console.log("Original:", sentence1);

let not1 = sentence1.indexOf("not");
let bad1 = sentence1.indexOf("bad");

if (not1 !== -1 && bad1 !== -1 && bad1 > not1) {
    let result1 = sentence1.slice(0, not1) + "good" + sentence1.slice(bad1 + 3);
    console.log("Result:", result1);
} else {
    console.log("Result:", sentence1);
}

console.log("\n--- Test 2 ---");
let sentence2 = "This movie is not so bad !";
console.log("Original:", sentence2);

let not2 = sentence2.indexOf("not");
let bad2 = sentence2.indexOf("bad");

if (not2 !== -1 && bad2 !== -1 && bad2 > not2) {
    let result2 = sentence2.slice(0, not2) + "good" + sentence2.slice(bad2 + 3);
    console.log("Result:", result2);
} else {
    console.log("Result:", sentence2);
}

console.log("\n--- Test 3 ---");
let sentence3 = "This dinner is bad !";
console.log("Original:", sentence3);

let not3 = sentence3.indexOf("not");
let bad3 = sentence3.indexOf("bad");

if (not3 !== -1 && bad3 !== -1 && bad3 > not3) {
    let result3 = sentence3.slice(0, not3) + "good" + sentence3.slice(bad3 + 3);
    console.log("Result:", result3);
} else {
    console.log("Result:", sentence3);
}