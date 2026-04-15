// ============================================================
// STEP 1: Define the Book Interface
// ============================================================

interface Book {
    title: string;           // Book title
    author: string;          // Author name
    isbn: string;            // Unique identifier
    publishedYear: number;   // Year of publication
    genre?: string;          // Optional genre property
}

// ============================================================
// STEP 2: Create the Base Library Class
// ============================================================

class Library {
    // Private property: only accessible within this class
    private books: Book[];

    constructor() {
        this.books = []; // Initialize empty array
    }

    // Public method: add a new book to the library
    public addBook(book: Book): void {
        // Check if book with same ISBN already exists
        const exists = this.books.some(b => b.isbn === book.isbn);
        if (exists) {
            console.log(`⚠️ Book with ISBN ${book.isbn} already exists!`);
            return;
        }
        
        this.books.push(book);
        console.log(`✅ Added: "${book.title}" by ${book.author}`);
    }

    // Public method: get book details by ISBN
    public getBookDetails(isbn: string): Book | undefined {
        const book = this.books.find(b => b.isbn === isbn);
        
        if (!book) {
            console.log(`❌ No book found with ISBN: ${isbn}`);
            return undefined;
        }
        
        return book;
    }

    // Protected method: allow subclasses to access books array
    protected getAllBooks(): Book[] {
        return [...this.books]; // Return copy to prevent direct modification
    }

    // Protected method: get count of books
    protected getBookCount(): number {
        return this.books.length;
    }
}

// ============================================================
// STEP 3: Create DigitalLibrary (Extends Library)
// ============================================================

class DigitalLibrary extends Library {
    // Readonly property: can only be set in constructor
    readonly website: string;

    constructor(website: string) {
        super(); // Call parent constructor
        this.website = website;
    }

    // Public method: return list of all book titles
    public listBooks(): string[] {
        const books = this.getAllBooks(); // Use protected method from parent
        return books.map(book => book.title);
    }

    // Public method: get library info
    public getLibraryInfo(): string {
        return `Digital Library Website: ${this.website} | Total Books: ${this.getBookCount()}`;
    }

    // Public method: search books by author
    public findBooksByAuthor(author: string): Book[] {
        const books = this.getAllBooks();
        return books.filter(book => 
            book.author.toLowerCase().includes(author.toLowerCase())
        );
    }

    // Public method: display formatted book list
    public displayCatalog(): void {
        const books = this.getAllBooks();
        
        console.log("\n📖 === LIBRARY CATALOG ===");
        console.log(`Website: ${this.website}\n`);
        
        if (books.length === 0) {
            console.log("No books in the library.");
            return;
        }

        books.forEach((book, index) => {
            console.log(`${index + 1}. "${book.title}"`);
            console.log(`   Author: ${book.author}`);
            console.log(`   ISBN: ${book.isbn}`);
            console.log(`   Year: ${book.publishedYear}`);
            if (book.genre) {
                console.log(`   Genre: ${book.genre}`);
            }
            console.log(""); // Empty line for readability
        });
    }
}

// ============================================================
// STEP 4: Usage and Testing
// ============================================================

// Create instance of DigitalLibrary
const myLibrary = new DigitalLibrary("https://digitallibrary.example.com");

// Add books to the library
console.log("🚀 Adding books to the digital library...\n");

myLibrary.addBook({
    title: "The Great Gatsby",
    author: "F. Scott Fitzgerald",
    isbn: "978-0743273565",
    publishedYear: 1925,
    genre: "Classic Fiction"
});

myLibrary.addBook({
    title: "1984",
    author: "George Orwell",
    isbn: "978-0451524935",
    publishedYear: 1949,
    genre: "Dystopian Fiction"
});

myLibrary.addBook({
    title: "Clean Code",
    author: "Robert C. Martin",
    isbn: "978-0132350884",
    publishedYear: 2008,
    genre: "Technical"
});

myLibrary.addBook({
    title: "The Hobbit",
    author: "J.R.R. Tolkien",
    isbn: "978-0547928227",
    publishedYear: 1937
    // No genre - optional property omitted
});

// Try to add duplicate (should show warning)
myLibrary.addBook({
    title: "Duplicate Book",
    author: "Some Author",
    isbn: "978-0743273565", // Same ISBN as first book
    publishedYear: 2024
});

console.log("\n" + "=".repeat(50) + "\n");

// Get details of specific books
console.log("🔍 Getting book details by ISBN:\n");

const book1 = myLibrary.getBookDetails("978-0743273565");
if (book1) {
    console.log("Found book:", JSON.stringify(book1, null, 2));
}

const book2 = myLibrary.getBookDetails("978-0451524935");
if (book2) {
    console.log("\nFound book:", JSON.stringify(book2, null, 2));
}

// Try non-existent ISBN
myLibrary.getBookDetails("999-9999999999");

console.log("\n" + "=".repeat(50) + "\n");

// List all book titles
console.log("📚 All Book Titles:");
const titles = myLibrary.listBooks();
titles.forEach((title, index) => {
    console.log(`  ${index + 1}. ${title}`);
});

console.log("\n" + "=".repeat(50) + "\n");

// Display full catalog
myLibrary.displayCatalog();

console.log("=".repeat(50) + "\n");

// Show library info
console.log(myLibrary.getLibraryInfo());

// Demonstrate readonly property
console.log(`\n🌐 Website: ${myLibrary.website}`);
// myLibrary.website = "https://newsite.com"; // ❌ Error: Cannot assign to 'website' because it is a read-only property

// Search by author
console.log("\n🔎 Search for 'Tolkien':");
const tolkienBooks = myLibrary.findBooksByAuthor("Tolkien");
console.log(tolkienBooks);