// ============================================
// JAVASCRIPT EXERCISES
// Variables, Conditionals, Loops, Functions
// ============================================

// ============================================
// EXERCISE 1: Checking the BMI
// ============================================

console.log("=== Exercise 1: Checking the BMI ===");

// Create two person objects with BMI calculation method
let person1 = {
    fullName: "John Doe",
    mass: 75,      // kg
    height: 1.75,  // meters
    calcBMI: function() {
        return this.mass / (this.height * this.height);
    }
};

let person2 = {
    fullName: "Jane Smith",
    mass: 68,      // kg
    height: 1.68,  // meters
    calcBMI: function() {
        return this.mass / (this.height * this.height);
    }
};

// Function to compare BMIs and display the result
function compareBMI(personA, personB) {
    let bmiA = personA.calcBMI();
    let bmiB = personB.calcBMI();
    
    console.log(`${personA.fullName}'s BMI: ${bmiA.toFixed(2)}`);
    console.log(`${personB.fullName}'s BMI: ${bmiB.toFixed(2)}`);
    
    if (bmiA > bmiB) {
        console.log(`${personA.fullName} has the largest BMI.`);
    } else if (bmiB > bmiA) {
        console.log(`${personB.fullName} has the largest BMI.`);
    } else {
        console.log("Both have the same BMI.");
    }
}

// Call the comparison function
compareBMI(person1, person2);


// ============================================
// EXERCISE 2: Grade Average
// ============================================

console.log("\n=== Exercise 2: Grade Average ===");

// Part 1 & 2: Calculate average
function findAvg(gradesList) {
    let sum = 0;
    
    for (let i = 0; i < gradesList.length; i++) {
        sum = sum + gradesList[i];
    }
    
    let average = sum / gradesList.length;
    return average;
}

// Part 3 & 4: Check pass/fail status
function checkResult(average) {
    console.log(`Your average is: ${average.toFixed(2)}`);
    
    if (average > 65) {
        console.log("Congratulations! You passed the course.");
    } else {
        console.log("You failed and must repeat the course.");
    }
}

// Bonus: Main function that calls the other two
function evaluateGrades(gradesList) {
    let avg = findAvg(gradesList);
    checkResult(avg);
}

// Test with different grade arrays
let grades1 = [80, 90, 75, 88, 92];  // Above 65
let grades2 = [50, 60, 55, 45, 70];  // Below 65

console.log("\n--- Student 1 ---");
evaluateGrades(grades1);

console.log("\n--- Student 2 ---");
evaluateGrades(grades2);