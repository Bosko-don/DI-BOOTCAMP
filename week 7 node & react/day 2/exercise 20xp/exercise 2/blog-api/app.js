const express = require("express");
const app = express();

app.use(express.json());

const bookRoutes = require("./server/routes/booksRoutes");
app.use("/api/books", bookRoutes);

app.listen(5000, () => {
  console.log("Server running on port 5000");
});