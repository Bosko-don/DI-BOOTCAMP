class Employee {
    // Private: only accessible within this class
    private name: string;
    private salary: number;
    
    // Public: accessible from anywhere
    public position: string;
    
    // Protected: accessible within class and subclasses
    protected department: string;

    constructor(name: string, salary: number, position: string, department: string) {
        this.name = name;
        this.salary = salary;
        this.position = position;
        this.department = department;
    }

    // Public method to access private data
    public getEmployeeInfo(): string {
        return `Name: ${this.name}, Position: ${this.position}`;
    }

    // Private method example
    private calculateBonus(): number {
        return this.salary * 0.1;
    }

    // Protected method example
    protected getDepartment(): string {
        return this.department;
    }
}

// Usage
const emp = new Employee("Alice", 50000, "Developer", "IT");
console.log(emp.getEmployeeInfo()); // ✅ Works: "Name: Alice, Position: Developer"
console.log(emp.position);          // ✅ Works: public property
// console.log(emp.name);            // ❌ Error: private property
// console.log(emp.department);      // ❌ Error: protected property