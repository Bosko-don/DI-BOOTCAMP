const express = require("express");
const router = express.Router();
const ctrl = require("../controllers/booksController");

router.get("/", ctrl.getBooks);
router.get("/:bookId", ctrl.getBook);
router.post("/", ctrl.createBook);

module.exports = router;