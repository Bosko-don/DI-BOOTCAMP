const { books } = require("../models/booksModel");

// GET all
exports.getBooks = (req, res) => {
  res.json(books);
};

// GET one
exports.getBook = (req, res) => {
  const book = books.find(b => b.id == req.params.bookId);
  if (!book) return res.status(404).send("Book not found");
  res.json(book);
};

// CREATE
exports.createBook = (req, res) => {
  const newBook = {
    id: books.length + 1,
    ...req.body,
  };
  books.push(newBook);
  res.status(201).json(newBook);
};