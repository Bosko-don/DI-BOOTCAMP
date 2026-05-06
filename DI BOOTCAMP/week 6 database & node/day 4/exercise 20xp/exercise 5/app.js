const _ = require('lodash');
const math = require('./math');

const numbers = [1, 2, 3, 4];

console.log("Sum:", _.sum(numbers));
console.log("Add:", math.add(5, 3));
console.log("Multiply:", math.multiply(4, 2));