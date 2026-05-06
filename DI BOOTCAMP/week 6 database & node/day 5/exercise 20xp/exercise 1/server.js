const express = require('express');
const app = express();

app.use(express.json()); // Middleware

const PORT = 3000;

// Fake database
let posts = [
  { id: 1, title: "First Post", content: "This is my first blog post" },
  { id: 2, title: "Second Post", content: "Learning Express is fun!" }
];

// GET all posts
app.get('/posts', (req, res) => {
  res.json(posts);
});

// GET single post
app.get('/posts/:id', (req, res) => {
  const id = parseInt(req.params.id);
  const post = posts.find(p => p.id === id);

  if (!post) return res.status(404).json({ message: "Post not found" });

  res.json(post);
});

// CREATE post
app.post('/posts', (req, res) => {
  const newPost = {
    id: posts.length + 1,
    title: req.body.title,
    content: req.body.content
  };

  posts.push(newPost);
  res.status(201).json(newPost);
});

// UPDATE post
app.put('/posts/:id', (req, res) => {
  const id = parseInt(req.params.id);
  const post = posts.find(p => p.id === id);

  if (!post) return res.status(404).json({ message: "Post not found" });

  post.title = req.body.title || post.title;
  post.content = req.body.content || post.content;

  res.json(post);
});

// DELETE post
app.delete('/posts/:id', (req, res) => {
  const id = parseInt(req.params.id);
  const index = posts.findIndex(p => p.id === id);

  if (index === -1) return res.status(404).json({ message: "Post not found" });

  const deleted = posts.splice(index, 1);
  res.json(deleted);
});

// 404 handler
app.use((req, res) => {
  res.status(404).json({ message: "Route not found" });
});

// Server error handler
app.use((err, req, res, next) => {
  res.status(500).json({ message: "Server error", error: err.message });
});

app.listen(PORT, () => {
  console.log(`Server running on http://localhost:${PORT}`);
});