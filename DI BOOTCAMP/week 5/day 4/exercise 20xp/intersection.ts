// Base types
type Person = {
    name: string;
    age: number;
};

type Job = {
    position: string;
    department: string;
};

// Manager and Developer specific types
type Manager = Job & {
    position: "Manager";
    teamSize: number;
};

type Developer = Job & {
    position: "Developer";
    programmingLanguages: string[];
};

// Employee combines Person with either Manager or Developer
type Employee = Person & (Manager | Developer);

function describeEmployee(employee: Employee): string {
    // Type guard based on position property
    if (employee.position === "Manager") {
        // TypeScript narrows to Manager here
        return `${employee.name} is a Manager in ${employee.department} department, leading a team of ${employee.teamSize} people.`;
    } else {
        // TypeScript narrows to Developer here
        return `${employee.name} is a Developer in ${employee.department} department, skilled in ${employee.programmingLanguages.join(", ")}.`;
    }
}

// Test
const manager: Employee = {
    name: "Bob",
    age: 40,
    position: "Manager",
    department: "Engineering",
    teamSize: 10
};

const developer: Employee = {
    name: "Carol",
    age: 28,
    position: "Developer",
    department: "Engineering",
    programmingLanguages: ["TypeScript", "Python", "Go"]
};

console.log(describeEmployee(manager));    // "Bob is a Manager..."
console.log(describeEmployee(developer));  // "Carol is a Developer..."