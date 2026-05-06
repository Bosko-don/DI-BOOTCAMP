const db = require("../config/db");

const getAllPosts = () => db("posts");

const getPostById = (id) =>
  db("posts").where({ id }).first();

const createPost = (data) =>
  db("posts").insert(data).returning("*");

const updatePost = (id, data) =>
  db("posts").where({ id }).update(data).returning("*");

const deletePost = (id) =>
  db("posts").where({ id }).del();

module.exports = {
  getAllPosts,
  getPostById,
  createPost,
  updatePost,
  deletePost,
};