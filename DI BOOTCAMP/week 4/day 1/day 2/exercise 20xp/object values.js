const object1 = { number: 5 }; 
const object2 = object1;       // same reference
const object3 = object2;         // same reference
const object4 = { number: 5 }; // new object

object1.number = 4;

console.log(object2.number);  // 4 (same reference as object1)
console.log(object3.number);  // 4 (same reference as object1)
console.log(object4.number);  // 5 (different object, unchanged)