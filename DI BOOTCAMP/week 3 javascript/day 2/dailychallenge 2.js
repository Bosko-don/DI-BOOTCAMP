// ============================================
// DAILY CHALLENGE: Words in the Stars
// Creates a rectangular frame of stars around words
// ============================================

function wordsInStars() {
    
    // Step 1: Prompt the user for words separated by commas
    const input = prompt("Enter several words separated by commas:");
    
    // Check if user cancelled or entered nothing
    if (!input || input.trim() === "") {
        console.log("No words entered. Please try again!");
        return;
    }
    
    // Step 2: Split the string into an array and trim whitespace from each word
    const words = input.split(',').map(word => word.trim());
    
    // Remove any empty strings (if user typed multiple commas)
    const cleanWords = words.filter(word => word.length > 0);
    
    if (cleanWords.length === 0) {
        console.log("No valid words entered.");
        return;
    }
    
    // Step 3: Find the length of the longest word
    let maxLength = 0;
    for (let word of cleanWords) {
        if (word.length > maxLength) {
            maxLength = word.length;
        }
    }
    
    // Alternative using array method:
    // const maxLength = Math.max(...cleanWords.map(word => word.length));
    
    // Step 4: Build the frame
    
    // Create the top and bottom border of stars
    // Length = max word length + 4 (for the stars and spaces on each side: * word *)
    const border = '*'.repeat(maxLength + 4);
    
    // Array to hold all lines of the frame
    const frameLines = [];
    
    // Add top border
    frameLines.push(border);
    
    // Add each word with proper padding
    for (let word of cleanWords) {
        // Calculate spaces needed on the right side
        const spaces = ' '.repeat(maxLength - word.length);
        // Format: * word + spaces *
        const line = `* ${word}${spaces} *`;
        frameLines.push(line);
    }
    
    // Add bottom border
    frameLines.push(border);
    
    // Step 5: Display the result
    console.log("\n"); // Empty line for spacing
    console.log("=== YOUR WORDS IN A STAR FRAME ===");
    console.log("\n");
    
    // Print each line
    for (let line of frameLines) {
        console.log(line);
    }
    
    console.log("\n");
    
    // Alternative: Return as single string
    const result = frameLines.join('\n');
    return result;
}

// Run the function
wordsInStars();


// ============================================
// BONUS: More flexible version with custom border character
// ============================================

function wordsInFrame(borderChar = '*') {
    
    const input = prompt(`Enter words separated by commas (frame: ${borderChar}):`);
    
    if (!input || input.trim() === "") {
        console.log("No words entered.");
        return;
    }
    
    // Process words
    const words = input.split(',').map(w => w.trim()).filter(w => w.length > 0);
    
    if (words.length === 0) return;
    
    // Find longest word
    const maxLength = Math.max(...words.map(w => w.length));
    
    // Build frame
    const border = borderChar.repeat(maxLength + 4);
    const lines = [border];
    
    for (let word of words) {
        const padding = ' '.repeat(maxLength - word.length);
        lines.push(`${borderChar} ${word}${padding} ${borderChar}`);
    }
    
    lines.push(border);
    
    // Display
    console.log('\n' + lines.join('\n') + '\n');
    
    return lines;
}

// Example outputs you should see:
// 
// For input: "Hello, World, in, a, frame"
// 
// ***************
// * Hello       *
// * World       *
// * in          *
// * a           *
// * frame       *
// ***************
//
// For input: "JavaScript is awesome"
//
// **************
// * JavaScript *
// * is         *
// * awesome    *
// **************


// ============================================
// TEST WITHOUT PROMPT (for Node.js or console testing)
// ============================================

function testWordsInStars(testInput) {
    
    const words = testInput.split(',').map(w => w.trim()).filter(w => w.length > 0);
    const maxLength = Math.max(...words.map(w => w.length));
    
    const border = '*'.repeat(maxLength + 4);
    const lines = [border];
    
    for (let word of words) {
        const padding = ' '.repeat(maxLength - word.length);
        lines.push(`* ${word}${padding} *`);
    }
    
    lines.push(border);
    
    console.log('\n' + lines.join('\n') + '\n');
    
    return lines;
}

// Uncomment to test:
// testWordsInStars("Hello, World, in, a, frame");
// testWordsInStars("JavaScript, is, fun");
// testWordsInStars("I, love, coding");