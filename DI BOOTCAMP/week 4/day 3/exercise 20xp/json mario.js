const marioGame = {
  detail: "An amazing game!",
  characters: {
    mario: {
      description: "Small and jumpy. Likes princesses.",
      height: 10,
      weight: 3,
      speed: 12,
    },
    bowser: {
      description: "Big and green, Hates princesses.",
      height: 16,
      weight: 6,
      speed: 4,
    },
    princessPeach: {
      description: "Beautiful princess.",
      height: 12,
      weight: 2,
      speed: 2,
    }
  },
};

// Convert to JSON (nested objects become nested JSON)
const jsonString = JSON.stringify(marioGame);
console.log(jsonString);

// Pretty print with indentation
const prettyJSON = JSON.stringify(marioGame, null, 2);
console.log(prettyJSON);

// For debugger breakpoint
debugger;