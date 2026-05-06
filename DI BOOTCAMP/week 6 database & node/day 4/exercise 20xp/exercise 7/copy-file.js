const fs = require('fs');

fs.readFile('source.txt', 'utf8', (err, data) => {
  if (err) {
    console.log("Error reading file:", err);
    return;
  }

  fs.writeFile('destination.txt', data, (err) => {
    if (err) {
      console.log("Error writing file:", err);
    } else {
      console.log("File copied successfully");
    }
  });
});