const bcrypt = require("bcrypt");
const model = require("../models/usersModel");

// 🟢 REGISTER
exports.register = async (req, res) => {
  try {
    const { email, username, first_name, last_name, password } = req.body;

    const hash = await bcrypt.hash(password, 10);

    const user = await model.createUser(
      { email, username, first_name, last_name },
      hash
    );

    res.status(201).json(user);
  } catch (err) {
    res.status(500).send("Registration failed");
  }
};

// 🟡 LOGIN
exports.login = async (req, res) => {
  try {
    const { username, password } = req.body;

    const user = await model.findUserByUsername(username);
    if (!user) return res.status(404).send("User not found");

    const hashRow = await model.getPassword(username);

    const valid = await bcrypt.compare(password, hashRow.password);

    if (!valid) return res.status(401).send("Invalid credentials");

    res.json({ message: "Login successful", user });
  } catch (err) {
    res.status(500).send("Login error");
  }
};

// 🔵 GET ALL USERS
exports.getUsers = async (req, res) => {
  const users = await model.getAllUsers();
  res.json(users);
};

// 🔍 GET ONE USER
exports.getUser = async (req, res) => {
  const user = await model.getUserById(req.params.id);
  if (!user) return res.status(404).send("User not found");
  res.json(user);
};

// ✏️ UPDATE USER
exports.updateUser = async (req, res) => {
  const [updated] = await model.updateUser(req.params.id, req.body);
  res.json(updated);
};