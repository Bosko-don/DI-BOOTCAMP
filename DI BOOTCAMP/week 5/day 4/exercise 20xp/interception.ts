// Define individual types
type Person = {
    name: string;
    age: number;
};

type Address = {
    street: string;
    city: string;
};

// Intersection type combines both
type PersonWithAddress = Person & Address;

// Create variable with properties from both types
const personWithAddress: PersonWithAddress = {
    name: "Alice",
    age: 30,
    street: "123 Main St",
    city: "New York"
};

console.log(personWithAddress);
// { name: 'Alice', age: 30, street: '123 Main St', city: 'New York' }