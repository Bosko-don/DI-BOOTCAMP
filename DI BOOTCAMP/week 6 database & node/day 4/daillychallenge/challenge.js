const greet = require('./greeting');
const showMessage = require('./colorful-message');
const readFileContent = require('./read-file');

// 1. Greeting
const message = greet("Samuel");
console.log(message);

// 2. Colorful Message
showMessage();

// 3. Read File
readFileContent();