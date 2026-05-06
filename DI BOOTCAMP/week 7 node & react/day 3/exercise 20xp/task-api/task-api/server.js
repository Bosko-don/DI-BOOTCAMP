const express = require("express");
const tasksRouter = require("./routes/tasks");

const app = express();

app.use(express.json());

// Routes
app.use("/tasks", tasksRouter);

// Global error handler
app.use((err, req, res, next) => {
  console.error(err.message);
  res.status(500).json({ error: "Server Error" });
});

const PORT = 5000;
app.listen(PORT, () => {
  console.log(`Server running on port ${PORT}`);
});