import { useState } from "react";
import { useSelector } from "react-redux";

import {
  selectBooks,
  selectHorrorBooks,
  selectFantasyBooks,
  selectScienceFictionBooks,
} from "../selectors/bookSelectors";

function BookList() {
  const [genre, setGenre] = useState("All");

  const allBooks = useSelector(selectBooks);
  const horrorBooks =
    useSelector(selectHorrorBooks);

  const fantasyBooks =
    useSelector(selectFantasyBooks);

  const scienceBooks = useSelector(
    selectScienceFictionBooks
  );

  let booksToDisplay = allBooks;

  if (genre === "Horror")
    booksToDisplay = horrorBooks;

  if (genre === "Fantasy")
    booksToDisplay = fantasyBooks;

  if (genre === "Science Fiction")
    booksToDisplay = scienceBooks;

  return (
    <div>
      <h1>Book Inventory</h1>

      <div>
        <button
          onClick={() => setGenre("All")}
        >
          All
        </button>

        <button
          onClick={() => setGenre("Horror")}
        >
          Horror
        </button>

        <button
          onClick={() => setGenre("Fantasy")}
        >
          Fantasy
        </button>

        <button
          onClick={() =>
            setGenre("Science Fiction")
          }
        >
          Science Fiction
        </button>
      </div>

      <h2>{genre} Books</h2>

      <ul>
        {booksToDisplay.map((book) => (
          <li key={book.id}>
            <strong>{book.title}</strong>
            <br />
            Author: {book.author}
            <br />
            Genre: {book.genre}
          </li>
        ))}
      </ul>
    </div>
  );
}

export default BookList;