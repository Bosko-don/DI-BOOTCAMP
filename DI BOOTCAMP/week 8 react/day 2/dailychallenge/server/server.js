const express = require('express');
const cors = require('cors');

const app = express();

// Middleware
app.use(cors());
app.use(express.json());

// GET route
app.get('/api/hello', (req, res) => {
    res.send('Hello From Express');
});

// POST route
app.post('/api/world', (req, res) => {
    const value = req.body.value;
    console.log('Received from client:', value);
    res.send(`I received your POST request. This is what you sent me: ${value}`);
});

// Start server
app.listen(5000, () => {
    console.log('Server running on port 5000');
});