const express = require('express');
const app = express();

app.use(express.json());

const PORT = 5000;

let books = [
  { id: 1, title: "Atomic Habits", author: "James Clear", publishedYear: 2018 },
  { id: 2, title: "Rich Dad Poor Dad", author: "Robert Kiyosaki", publishedYear: 1997 }
];

// Server start
app.listen(PORT, () => {
  console.log(`Book API running on http://localhost:${PORT}`);
});

// GET all books
app.get('/api/books', (req, res) => {
  res.json(books);
});

// GET one book
app.get('/api/books/:bookId', (req, res) => {
  const id = parseInt(req.params.bookId);
  const book = books.find(b => b.id === id);

  if (!book) {
    return res.status(404).json({ message: "Book not found" });
  }

  res.status(200).json(book);
});

// CREATE book
app.post('/api/books', (req, res) => {
  const newBook = {
    id: books.length + 1,
    title: req.body.title,
    author: req.body.author,
    publishedYear: req.body.publishedYear
  };

  books.push(newBook);
  res.status(201).json(newBook);
});