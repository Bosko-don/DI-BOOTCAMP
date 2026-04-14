/**
 * Validates if a value's type matches one of the allowed types
 * @param value - The value to check
 * @param allowedTypes - Array of allowed type names as strings
 * @returns boolean - true if value's type is in allowedTypes, false otherwise
 */
function validateUnionType(value: any, allowedTypes: string[]): boolean {
    const actualType: string = typeof value;
    
    for (let i = 0; i < allowedTypes.length; i++) {
        if (actualType === allowedTypes[i]) {
            return true;
        }
    }
    
    return false;
}

// ============================================
// DEMONSTRATION
// ============================================

console.log("=== Union Type Validator Demo ===\n");

// Test 1: Validating a string
const personName: string = "Alice";
const isValidName = validateUnionType(personName, ['string', 'number']);
console.log(`Value: "${personName}" (type: ${typeof personName})`);
console.log(`Allowed types: ['string', 'number']`);
console.log(`Result: ${isValidName}`); // true
console.log("");

// Test 2: Validating a number against multiple types
const personAge: number = 25;
const isValidAge = validateUnionType(personAge, ['string', 'boolean', 'object']);
console.log(`Value: ${personAge} (type: ${typeof personAge})`);
console.log(`Allowed types: ['string', 'boolean', 'object']`);
console.log(`Result: ${isValidAge}`); // false
console.log("");

// Test 3: Validating a boolean
const isActiveUser: boolean = true;
const isValidStatus = validateUnionType(isActiveUser, ['boolean', 'string']);
console.log(`Value: ${isActiveUser} (type: ${typeof isActiveUser})`);
console.log(`Allowed types: ['boolean', 'string']`);
console.log(`Result: ${isValidStatus}`); // true
console.log("");

// Test 4: Validating an object
const personProfile = { name: "Bob", age: 30 };
const isValidProfile = validateUnionType(personProfile, ['object', 'null']);
console.log(`Value: ${JSON.stringify(personProfile)} (type: ${typeof personProfile})`);
console.log(`Allowed types: ['object', 'null']`);
console.log(`Result: ${isValidProfile}`); // true
console.log("");

// Test 5: Validating null
const emptyValue: null = null;
const isValidNull = validateUnionType(emptyValue, ['object', 'undefined']);
console.log(`Value: ${emptyValue} (type: ${typeof emptyValue})`);
console.log(`Allowed types: ['object', 'undefined']`);
console.log(`Result: ${isValidNull}`); // true
console.log("");

// Test 6: Validating undefined
const notAssigned: undefined = undefined;
const isValidUndefined = validateUnionType(notAssigned, ['string', 'number']);
console.log(`Value: ${notAssigned} (type: ${typeof notAssigned})`);
console.log(`Allowed types: ['string', 'number']`);
console.log(`Result: ${isValidUndefined}`); // false
console.log("");

// Test 7: Practical use case
function processFormInput(input: any): string {
    const allowedTypes = ['string', 'number'];
    
    if (validateUnionType(input, allowedTypes)) {
        return `✅ Valid input: ${input} (type: ${typeof input})`;
    } else {
        return `❌ Invalid input! Expected: ${allowedTypes.join(', ')}, got: ${typeof input}`;
    }
}

console.log("=== Form Validation ===");
console.log(processFormInput("Hello World"));
console.log(processFormInput(42));
console.log(processFormInput(true));