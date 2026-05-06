const fs = require('fs');

function readFile(fileName) {
  fs.readFile(fileName, 'utf8', (err, data) => {
    if (err) {
      console.log("Error reading file:", err);
    } else {
      console.log("File content:", data);
    }
  });
}

function writeFile(fileName, content) {
  fs.writeFile(fileName, content, (err) => {
    if (err) {
      console.log("Error writing file:", err);
    } else {
      console.log("File written successfully");
    }
  });
}

module.exports = { readFile, writeFile };