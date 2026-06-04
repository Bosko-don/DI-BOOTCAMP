import { createSlice } from "@reduxjs/toolkit";

const initialState = [
  {
    id: 1,
    title: "It",
    author: "Stephen King",
    genre: "Horror",
  },
  {
    id: 2,
    title: "The Shining",
    author: "Stephen King",
    genre: "Horror",
  },
  {
    id: 3,
    title: "Harry Potter",
    author: "J.K. Rowling",
    genre: "Fantasy",
  },
  {
    id: 4,
    title: "The Hobbit",
    author: "J.R.R. Tolkien",
    genre: "Fantasy",
  },
  {
    id: 5,
    title: "Dune",
    author: "Frank Herbert",
    genre: "Science Fiction",
  },
  {
    id: 6,
    title: "Foundation",
    author: "Isaac Asimov",
    genre: "Science Fiction",
  },
];

const bookSlice = createSlice({
  name: "books",
  initialState,
  reducers: {},
});

export default bookSlice.reducer;