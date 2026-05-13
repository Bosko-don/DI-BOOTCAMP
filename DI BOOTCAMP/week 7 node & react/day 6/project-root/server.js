const express = require('express');
const bodyParser = require('body-parser');
const cors = require('cors');
const Parser = require('rss-parser');

const app = express();
const parser = new Parser();

app.use(bodyParser.urlencoded({ extended: true }));
app.use(cors());
app.set('view engine', 'ejs');
app.use(express.static('public'));

const RSS_URL = 'https://thefactfile.org/feed/';

// Route 1: GET / - Display all posts
app.get('/', async (req, res) => {
    const feed = await parser.parseURL(RSS_URL);
    res.render('pages/index', { posts: feed.items, title: feed.title });
});

// Route 2: GET /search - Show search form (no posts yet)
app.get('/search', (req, res) => {
    res.render('pages/search', { posts: [] });
});

// Route 3: POST /search/title - Search by title
app.post('/search/title', async (req, res) => {
    const feed = await parser.parseURL(RSS_URL);
    const searchTitle = req.body.title.toLowerCase();
    const filtered = feed.items.filter(item => 
        item.title.toLowerCase().includes(searchTitle)
    );
    res.render('pages/search', { posts: filtered });
});

// Route 4: POST /search/category - Search by category
app.post('/search/category', async (req, res) => {
    const feed = await parser.parseURL(RSS_URL);
    const searchCategory = req.body.category;
    const filtered = feed.items.filter(item => 
        item.categories && item.categories.includes(searchCategory)
    );
    res.render('pages/search', { posts: filtered });
});

app.listen(3000, () => console.log('Server on port 3000'));