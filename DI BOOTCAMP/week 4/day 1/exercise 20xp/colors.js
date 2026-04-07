const colors = ["Blue", "Green", "Red", "Orange", "Violet", "Indigo", "Yellow"];

// Display colors with order
colors.forEach((color, index) => {
    console.log(`${index + 1}# choice is ${color}.`);
});

// Check if at least one element is "Violet"
if (colors.includes("Violet")) {
    console.log("Yeah");
} else {
    console.log("No...");
}