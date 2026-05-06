const fs = require('fs');
const path = require('path');

function readFileContent() {
  const filePath = path.join(__dirname, 'files', 'file-data.txt');

  fs.readFile(filePath, 'utf8', (err, data) => {
    if (err) {
      console.log("Error reading file:", err);
    } else {
      console.log("📄 File Content:\n", data);
    }
  });
}

module.exports = readFileContent;