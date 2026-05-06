const express = require("express");
const app = express();

app.use(express.json());

const todoRoutes = require("./routes/todos");
app.use("/todos", todoRoutes);

app.listen(3000, () => {
  console.log("Server running on port 3000");
});