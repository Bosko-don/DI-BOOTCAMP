// Base interface
interface User {
    readonly id: number;    // Cannot be changed after creation
    name: string;
    email: string;
}

// Extended interface with optional property
interface PremiumUser extends User {
    membershipLevel?: string;  // Optional (may be undefined)
    readonly joinedDate: Date; // Additional readonly property
}

// Function using the extended interface
function printUserDetails(user: PremiumUser): void {
    console.log("=== User Details ===");
    console.log(`ID: ${user.id}`);
    console.log(`Name: ${user.name}`);
    console.log(`Email: ${user.email}`);
    
    // Check optional property
    if (user.membershipLevel) {
        console.log(`Membership: ${user.membershipLevel}`);
    } else {
        console.log("Membership: Standard (no level specified)");
    }
    
    console.log(`Joined: ${user.joinedDate.toDateString()}`);
}

// Usage
const premiumUser: PremiumUser = {
    id: 1,
    name: "John Doe",
    email: "john@example.com",
    membershipLevel: "Gold",
    joinedDate: new Date("2024-01-15")
};

const basicUser: PremiumUser = {
    id: 2,
    name: "Jane Smith",
    email: "jane@example.com",
    joinedDate: new Date("2024-03-20")
    // membershipLevel is optional, so we can omit it
};

printUserDetails(premiumUser);
printUserDetails(basicUser);

// Attempting to modify readonly properties:
// premiumUser.id = 999;      // ❌ Error: readonly
// premiumUser.joinedDate = new Date(); // ❌ Error: readonly
premiumUser.name = "Johnny";  // ✅ Works: not readonly