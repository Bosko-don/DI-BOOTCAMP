let currentScore = 0;

async function loadQuestion() {
  const res = await fetch('/api/question');
  const data = await res.json();

  document.getElementById('emoji').textContent = data.emoji;

  const optionsDiv = document.getElementById('options');
  optionsDiv.innerHTML = '';

  data.options.forEach(option => {
    const btn = document.createElement('button');
    btn.textContent = option;

    btn.onclick = () => submitGuess(option);

    optionsDiv.appendChild(btn);
  });
}

async function submitGuess(guess) {
  const res = await fetch('/api/guess', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ guess })
  });

  const data = await res.json();

  const feedback = document.getElementById('feedback');

  if (data.correct) {
    feedback.textContent = "✅ Correct!";
  } else {
    feedback.textContent = "❌ Wrong!";
  }

  currentScore = data.score;
  document.getElementById('score').textContent = currentScore;
}

async function loadLeaderboard() {
  const res = await fetch('/api/leaderboard');
  const data = await res.json();

  const list = document.getElementById('leaderboard');
  list.innerHTML = '';

  data.forEach(player => {
    const li = document.createElement('li');
    li.textContent = `${player.name}: ${player.score}`;
    list.appendChild(li);
  });
}

// initial load
loadQuestion();
loadLeaderboard();