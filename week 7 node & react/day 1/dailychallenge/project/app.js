const express = require("express");
const session = require("express-session");

const app = express();

app.use(express.json());

// Session to track score + progress
app.use(
  session({
    secret: "quiz-game-secret",
    resave: false,
    saveUninitialized: true,
  })
);

const quizRoutes = require("./routes/quiz");
app.use("/quiz", quizRoutes);

app.listen(3000, () => {
  console.log("Server running on http://localhost:3000");
});