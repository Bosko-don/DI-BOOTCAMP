// EXERCISE 1
let people = ["Greg", "Mary", "Devon", "James"];
people.shift();
people[people.indexOf("James")] = "Jason";
people.push("YourName");
console.log("Mary's index:", people.indexOf("Mary"));
let peopleCopy = people.slice(1, 3);
console.log("Index of 'Foo':", people.indexOf("Foo"));
let last = people[people.length - 1];
console.log("Last element:", last);

console.log("\n--- All people ---");
for (let i = 0; i < people.length; i++) console.log(people[i]);

console.log("\n--- Until Devon ---");
for (let i = 0; i < people.length; i++) {
    console.log(people[i]);
    if (people[i] === "Devon") break;
}

// EXERCISE 2
console.log("\n=== EXERCISE 2 ===");
let colors = ["Blue", "Red", "Green", "Purple", "Orange"];
for (let i = 0; i < colors.length; i++) {
    let suffix = i === 0 ? "st" : i === 1 ? "nd" : i === 2 ? "rd" : "th";
    console.log(`My ${i + 1}${suffix} choice is ${colors[i]}`);
}

// EXERCISE 3 - FIXED FOR NODE.JS
console.log("\n=== EXERCISE 3 ===");
// Simulated input (replace 5 with any number < 10 to test the loop)
let number = 5; 
console.log("Starting number:", number);
while (number < 10) {
    number++; // Simulating user entering new number
    console.log("Number is < 10, increasing to:", number);
}
console.log("Final number:", number);

// EXERCISE 4
console.log("\n=== EXERCISE 4 ===");
const building = {
    numberOfFloors: 4,
    numberOfAptByFloor: { firstFloor: 3, secondFloor: 4, thirdFloor: 9, fourthFloor: 2 },
    nameOfTenants: ["Sarah", "Dan", "David"],
    numberOfRoomsAndRent: { sarah: [3, 990], dan: [4, 1000], david: [1, 500] }
};
console.log("Floors:", building.numberOfFloors);
console.log("Apts on floors 1 & 3:", building.numberOfAptByFloor.firstFloor + building.numberOfAptByFloor.thirdFloor);
console.log("Second tenant:", building.nameOfTenants[1], "Rooms:", building.numberOfRoomsAndRent.dan[0]);

let sarahRent = building.numberOfRoomsAndRent.sarah[1];
let davidRent = building.numberOfRoomsAndRent.david[1];
let danRent = building.numberOfRoomsAndRent.dan[1];
console.log(`Sarah: $${sarahRent} + David: $${davidRent} = $${sarahRent + davidRent}`);
if (sarahRent + davidRent > danRent) {
    building.numberOfRoomsAndRent.dan[1] = 1200;
    console.log("Dan's rent increased to $1200");
}

// EXERCISE 5
console.log("\n=== EXERCISE 5 ===");
const family = { father: "John", mother: "Jane", son: "Jimmy", daughter: "Jenny" };
console.log("Keys:");
for (let key in family) console.log(" ", key);
console.log("Values:");
for (let key in family) console.log(" ", family[key]);

// EXERCISE 6
console.log("\n=== EXERCISE 6 ===");
const details = { my: 'name', is: 'Rudolf', the: 'reindeer' };
let sentence = "";
for (let key in details) sentence += key + " " + details[key] + " ";
console.log(sentence.trim());

// EXERCISE 7
console.log("\n=== EXERCISE 7 ===");
const names = ["Jack", "Philip", "Sarah", "Amanda", "Bernard", "Kyle"];
let firstLetters = names.map(n => n[0]).sort().join("");
console.log("Secret society:", firstLetters);

console.log("\n=== ALL DONE! ===");