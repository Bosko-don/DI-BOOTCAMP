const express = require("express");
const app = express();

app.use(express.json());

const userRoutes = require("./server/routes/usersRoutes");
app.use("/", userRoutes);

// 404
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