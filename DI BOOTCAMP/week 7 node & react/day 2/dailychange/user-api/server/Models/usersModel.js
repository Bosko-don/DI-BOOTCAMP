const db = require("../config/db");

// 🔐 Register user using transaction
const createUser = async (user, hashedPassword) => {
  return db.transaction(async trx => {
    const [newUser] = await trx("users")
      .insert(user)
      .returning("*");

    await trx("hashpwd").insert({
      username: user.username,
      password: hashedPassword,
    });

    return newUser;
  });
};

// 🔍 Find user
const findUserByUsername = username =>
  db("users").where({ username }).first();

// 🔑 Get password hash
const getPassword = username =>
  db("hashpwd").where({ username }).first();

// 📄 Get all users
const getAllUsers = () => db("users");

// 📄 Get one user
const getUserById = id =>
  db("users").where({ id }).first();

// ✏️ Update user
const updateUser = (id, data) =>
  db("users").where({ id }).update(data).returning("*");

module.exports = {
  createUser,
  findUserByUsername,
  getPassword,
  getAllUsers,
  getUserById,
  updateUser,
};