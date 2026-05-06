const express = require("express");
const router = express.Router();
const ctrl = require("../controllers/usersController");

router.post("/register", ctrl.register);
router.post("/login", ctrl.login);

router.get("/users", ctrl.getUsers);
router.get("/users/:id", ctrl.getUser);
router.put("/users/:id", ctrl.updateUser);

module.exports = router;