const express = require("express");
const app = express();

app.use(express.json());

const postRoutes = require("./server/routes/postsRoutes");
app.use("/posts", postRoutes);

// 404 handler
app.use((req, res) => {
  res.status(404).send("Route not found");
});

// server error
app.use((err, req, res, next) => {
  res.status(500).send("Server error");
});

app.listen(3000, () => {
  console.log("Server running on port 3000");
});