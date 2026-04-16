function getFirstElement(arr: (number | string)[]): string {
    const first = arr[0];
    // Type assertion: tell TypeScript to treat first element as string
    return first as string;
}

// Test with mixed arrays
const mixedArray1: (number | string)[] = ["hello", 42, 99];
const mixedArray2: (number | string)[] = [100, "world", 50];

console.log(getFirstElement(mixedArray1)); // "hello"
console.log(getFirstElement(mixedArray2)); // "100" (number converted to string representation)