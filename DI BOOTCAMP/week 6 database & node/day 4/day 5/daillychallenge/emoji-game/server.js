const express = require('express');
const fs = require('fs');
const path = require('path');
const emojis = require('./data');

const app = express();
const PORT = 3000;

app.use(express.json());
app.use(express.static('public'));

let score = 0;

// Helper: random emoji + options
function getQuestion() {
  const correct = emojis[Math.floor(Math.random() * emojis.length)];

  let options = [correct.name];

  while (options.length < 4) {
    const random = emojis[Math.floor(Math.random() * emojis.length)].name;
    if (!options.includes(random)) {
      options.push(random);
    }
  }

  // shuffle
  options.sort(() => Math.random() - 0.5);

  return { emoji: correct.emoji, correct: correct.name, options };
}

// Store current answer
let currentAnswer = "";

// GET question
app.get('/api/question', (req, res) => {
  const q = getQuestion();
  currentAnswer = q.correct;

  res.json({
    emoji: q.emoji,
    options: q.options
  });
});

// POST guess
app.post('/api/guess', (req, res) => {
  const userGuess = req.body.guess;

  let correct = false;

  if (userGuess === currentAnswer) {
    score++;
    correct = true;
  }

  res.json({
    correct,
    score
  });
});

// Leaderboard (simple file)
const leaderboardPath = path.join(__dirname, 'leaderboard.json');

// Save score
app.post('/api/leaderboard', (req, res) => {
  const { name, score } = req.body;

  let data = [];

  if (fs.existsSync(leaderboardPath)) {
    data = JSON.parse(fs.readFileSync(leaderboardPath));
  }

  data.push({ name, score });

  // sort top scores
  data.sort((a, b) => b.score - a.score);

  fs.writeFileSync(leaderboardPath, JSON.stringify(data, null, 2));

  res.json({ message: "Saved!" });
});

// Get leaderboard
app.get('/api/leaderboard', (req, res) => {
  if (!fs.existsSync(leaderboardPath)) {
    return res.json([]);
  }

  const data = JSON.parse(fs.readFileSync(leaderboardPath));
  res.json(data.slice(0, 5)); // top 5
});

app.listen(PORT, () => {
  console.log(`Game running on http://localhost:${PORT}`);
});