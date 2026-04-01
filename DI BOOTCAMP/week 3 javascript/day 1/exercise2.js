// ============================================
// JAVASCRIPT BASICS EXERCISES
// Variables, Conditionals, Loops, Objects
// ============================================

// ============================================
// EXERCISE 1: Divisible by Three
// ============================================

let numbers = [123, 8409, 100053, 333333333, 7];

console.log("=== Exercise 1: Divisible by Three ===");

for (let i = 0; i < numbers.length; i++) {
    let isDivisible = numbers[i] % 3 === 0;
    console.log(isDivisible);
}


// ============================================
// EXERCISE 2: Attendance
// ============================================

let guestList = {
    randy: "Germany",
    karla: "France",
    wendy: "Japan",
    norman: "England",
    sam: "Argentina"
};

console.log("\n=== Exercise 2: Attendance ===");

let studentName = prompt("What is your name?").toLowerCase();

if (studentName in guestList) {
    console.log(`Hi! I'm ${studentName}, and I'm from ${guestList[studentName]}.`);
} else {
    console.log("Hi! I'm a guest.");
}


// ============================================
// EXERCISE 3: Playing with Numbers
// ============================================

let age = [20, 5, 12, 43, 98, 55];

console.log("\n=== Exercise 3: Playing with Numbers ===");

// 1. Sum of all numbers
let sum = 0;
for (let i = 0; i < age.length; i++) {
    sum = sum + age[i];
}
console.log("Sum of all ages:", sum);

// 2. Highest age
let highest = age[0];
for (let i = 1; i < age.length; i++) {
    if (age[i] > highest) {
        highest = age[i];
    }
}
console.log("Highest age:", highest);