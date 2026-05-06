const fs = require('fs');

fs.readdir('.', (err, files) => {
  if (err) {
    console.log("Error reading directory:", err);
  } else {
    console.log("Files:");
    files.forEach(file => console.log(file));
  }
});