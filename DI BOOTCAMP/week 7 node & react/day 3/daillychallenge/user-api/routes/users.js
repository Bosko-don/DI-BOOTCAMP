const express = require("express");
const fs = require("fs");
const path = require("path");
const bcrypt = require("bcrypt");

const router = express.Router();

const filePath = path.join(__dirname, "../data/users.json");

// Helpers
const getUsers = () => JSON.parse(fs.readFileSync(filePath, "utf-8"));
const saveUsers = (users) =>
  fs.writeFileSync(filePath, JSON.stringify(users, null, 2));

// REGISTER
router.post("/register", async (req, res) => {
  try {
    const { name, lastName, email, username, password } = req.body;

    if (!name || !lastName || !email || !username || !password) {
      return res.status(400).json({ message: "error1" });
    }

    const users = getUsers();

    // check duplicate username or email
    const exists = users.find(
      (u) => u.username === username || u.email === email
    );

    if (exists) {
      return res.status(409).json({ message: "error1" });
    }

    const hashedPassword = await bcrypt.hash(password, 10);

    const newUser = {
      id: Date.now().toString(),
      name,
      lastName,
      email,
      username,
      password: hashedPassword
    };

    users.push(newUser);
    saveUsers(users);

    res.json({ message: "register" });
  } catch (err) {
    res.status(500).json({ message: "Server error" });
  }
});

// LOGIN
router.post("/login", async (req, res) => {
  try {
    const { username, password } = req.body;

    const users = getUsers();

    const user = users.find((u) => u.username === username);

    if (!user) {
      return res.status(404).json({ message: "error2" });
    }

    const isMatch = await bcrypt.compare(password, user.password);

    if (!isMatch) {
      return res.status(401).json({ message: "error2" });
    }

    res.json({ message: "login" });
  } catch (err) {
    res.status(500).json({ message: "Server error" });
  }
});

// GET ALL USERS
router.get("/users", (req, res) => {
  const users = getUsers();
  res.json(users);
});

// GET USER BY ID
router.get("/users/:id", (req, res) => {
  const users = getUsers();
  const user = users.find((u) => u.id === req.params.id);

  if (!user) {
    return res.status(404).json({ message: "User not found" });
  }

  res.json(user);
});

// UPDATE USER
router.put("/users/:id", (req, res) => {
  const users = getUsers();
  const index = users.findIndex((u) => u.id === req.params.id);

  if (index === -1) {
    return res.status(404).json({ message: "User not found" });
  }

  users[index] = {
    ...users[index],
    ...req.body
  };

  saveUsers(users);

  res.json(users[index]);
});

module.exports = router;