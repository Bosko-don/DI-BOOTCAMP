// Variable of type any
let someValue: any = "Hello, TypeScript!";

// Cast to string using 'as' syntax
let strLength: number = (someValue as string).length;

// Or using angle-bracket syntax (not recommended in JSX)
// let strLength: number = (<string>someValue).length;

console.log(strLength); // 18

// Using the cast value as string
console.log((someValue as string).toUpperCase()); // "HELLO, TYPESCRIPT!"