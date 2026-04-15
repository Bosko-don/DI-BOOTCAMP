class Calculator {
    // Static property
    static readonly PI: number = 3.14159;

    // Static methods - no 'this' context of instance
    static add(a: number, b: number): number {
        return a + b;
    }

    static subtract(a: number, b: number): number {
        return a - b;
    }

    static multiply(a: number, b: number): number {
        return a * b;
    }

    static divide(a: number, b: number): number {
        if (b === 0) throw new Error("Cannot divide by zero");
        return a / b;
    }
}

// Usage - NO instance needed!
console.log(Calculator.add(5, 3));        // 8
console.log(Calculator.subtract(10, 4));  // 6
console.log(Calculator.PI);                 // 3.14159

// const calc = new Calculator();          // Not needed!
// calc.add(1, 2);                         // ❌ Error: add is static