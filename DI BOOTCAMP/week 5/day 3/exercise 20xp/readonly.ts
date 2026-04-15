class Product {
    // readonly: can only be set in constructor or at declaration
    readonly id: number;
    public name: string;
    public price: number;

    constructor(id: number, name: string, price: number) {
        this.id = id;  // ✅ Can set here
        this.name = name;
        this.price = price;
    }

    public getProductInfo(): string {
        return `Product: ${this.name}, Price: $${this.price}`;
    }
}

// Usage
const laptop = new Product(101, "MacBook Pro", 1999);
console.log(laptop.getProductInfo()); // "Product: MacBook Pro, Price: $1999"
console.log(laptop.id);               // ✅ Can read: 101

// Attempt to modify readonly property
// laptop.id = 102;                   // ❌ Error: Cannot assign to 'id' because it is a read-only property