const express = require("express");
const router = express.Router();

// 📌 Hard-coded questions (model)
const triviaQuestions = [
  {
    question: "What is the capital of France?",
    answer: "Paris",
  },
  {
    question: "Which planet is known as the Red Planet?",
    answer: "Mars",
  },
  {
    question: "What is the largest mammal in the world?",
    answer: "Blue whale",
  },
];

// 🟢 START QUIZ / GET QUESTION
router.get("/", (req, res) => {
  // initialize session if first time
  if (req.session.index === undefined) {
    req.session.index = 0;
    req.session.score = 0;
  }

  // if finished
  if (req.session.index >= triviaQuestions.length) {
    return res.json({
      message: "Quiz finished! Go to /quiz/score",
    });
  }

  const current = triviaQuestions[req.session.index];

  res.json({
    questionNumber: req.session.index + 1,
    question: current.question,
  });
});

// 🟡 SUBMIT ANSWER
router.post("/", (req, res) => {
  const userAnswer = req.body.answer;

  if (req.session.index === undefined) {
    return res.status(400).json({ message: "Start quiz first at GET /quiz" });
  }

  if (req.session.index >= triviaQuestions.length) {
    return res.json({ message: "Quiz already completed" });
  }

  const current = triviaQuestions[req.session.index];

  let correct = false;

  // check answer (case-insensitive)
  if (
    userAnswer &&
    userAnswer.toLowerCase() === current.answer.toLowerCase()
  ) {
    req.session.score++;
    correct = true;
  }

  req.session.index++;

  // next question or finish
  if (req.session.index >= triviaQuestions.length) {
    return res.json({
      correct,
      correctAnswer: current.answer,
      message: "Quiz completed!",
      goToScore: "/quiz/score",
    });
  }

  const nextQuestion = triviaQuestions[req.session.index];

  res.json({
    correct,
    correctAnswer: current.answer,
    nextQuestion: nextQuestion.question,
    scoreSoFar: req.session.score,
  });
});

// 🔵 GET FINAL SCORE
router.get("/score", (req, res) => {
  if (req.session.score === undefined) {
    return res.json({ message: "No quiz played yet" });
  }

  const result = {
    score: req.session.score,
    total: triviaQuestions.length,
  };

  // reset game
  req.session.index = 0;
  req.session.score = 0;

  res.json(result);
});

module.exports = router;