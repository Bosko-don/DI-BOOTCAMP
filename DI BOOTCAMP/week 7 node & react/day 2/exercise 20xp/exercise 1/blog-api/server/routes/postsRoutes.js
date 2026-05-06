const express = require("express");
const router = express.Router();
const ctrl = require("../controllers/postsController");

router.get("/", ctrl.getPosts);
router.get("/:id", ctrl.getPost);
router.post("/", ctrl.createPost);
router.put("/:id", ctrl.updatePost);
router.delete("/:id", ctrl.deletePost);

module.exports = router;