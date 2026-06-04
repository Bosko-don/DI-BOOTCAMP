import { createSelector } from "@reduxjs/toolkit";

const bookState = (state) => state.books;

// All Books
export const selectBooks = createSelector(
  [bookState],
  (books) => books
);

// Horror Books
export const selectHorrorBooks = createSelector(
  [bookState],
  (books) =>
    books.filter(
      (book) => book.genre === "Horror"
    )
);

// Fantasy Books
export const selectFantasyBooks = createSelector(
  [bookState],
  (books) =>
    books.filter(
      (book) => book.genre === "Fantasy"
    )
);

// Science Fiction Books
export const selectScienceFictionBooks =
  createSelector(
    [bookState],
    (books) =>
      books.filter(
        (book) =>
          book.genre === "Science Fiction"
      )
  );