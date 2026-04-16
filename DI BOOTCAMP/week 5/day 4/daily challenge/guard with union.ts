// ============================================
// Type Definitions
// ============================================

type User = {
    type: 'user';
    name: string;
    age: number;
};

type Product = {
    type: 'product';
    id: number;
    price: number;
};

type Order = {
    type: 'order';
    orderId: string;
    amount: number;
};

type DataItem = User | Product | Order;

// ============================================
// Type Guard Functions
// ============================================

function isUser(item: DataItem): item is User {
    return item.type === 'user';
}

function isProduct(item: DataItem): item is Product {
    return item.type === 'product';
}

function isOrder(item: DataItem): item is Order {
    return item.type === 'order';
}

// ============================================
// Main Handler Function
// ============================================

function handleData(data: DataItem[]): string[] {
    const results: string[] = [];

    for (let i = 0; i < data.length; i++) {
        const item = data[i];

        if (isUser(item)) {
            results.push(`Hello, ${item.name}! You are ${item.age} years old.`);
        } else if (isProduct(item)) {
            results.push(`Product #${item.id} costs $${item.price.toFixed(2)}.`);
        } else if (isOrder(item)) {
            results.push(`Order ${item.orderId}: Total amount $${item.amount.toFixed(2)}.`);
        } else {
            // Graceful handling of unexpected cases
            console.warn(`Unknown item at index ${i}:`, item);
            results.push(`Unknown data type at position ${i}`);
        }
    }

    return results;
}

// ============================================
// Test the Function
// ============================================

const testData: DataItem[] = [
    { type: 'user', name: 'Alice', age: 30 },
    { type: 'product', id: 101, price: 29.99 },
    { type: 'order', orderId: 'ORD-2024-001', amount: 150.50 },
    { type: 'user', name: 'Bob', age: 25 },
    { type: 'product', id: 102, price: 49.99 },
    { type: 'order', orderId: 'ORD-2024-002', amount: 75.00 }
];

// Run the function
const output = handleData(testData);

// Display results
console.log("=== Results ===");
output.forEach((result, index) => {
    console.log(`${index + 1}. ${result}`);
});

// Export for module usage (optional)
export { handleData, isUser, isProduct, isOrder };
export type { User, Product, Order, DataItem };