const express = require("express");
const app = express();

const indexRoutes = require("./routes/index");

app.use("/", indexRoutes);

const PORT = 3000;
app.listen(PORT, () => {
  console.log(`Server running on http://localhost:${PORT}`);
});