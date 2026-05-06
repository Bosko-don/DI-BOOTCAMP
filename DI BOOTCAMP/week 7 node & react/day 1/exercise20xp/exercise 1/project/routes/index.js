const express = require("express");
const router = express.Router();

// Home route
router.get("/", (req, res) => {
  res.send("Welcome to Homepage");
});

// About route
router.get("/about", (req, res) => {
  res.send("About Us Page");
});

module.exports = router;