const express = require("express");
const fs = require("fs");
const path = require("path");

const router = express.Router();

const filePath = path.join(__dirname, "../data/tasks.json");

// Helper: read tasks
const getTasks = () => {
  try {
    const data = fs.readFileSync(filePath, "utf-8");
    return JSON.parse(data);
  } catch (err) {
    throw new Error("Failed to read tasks file");
  }
};

// Helper: save tasks
const saveTasks = (tasks) => {
  try {
    fs.writeFileSync(filePath, JSON.stringify(tasks, null, 2));
  } catch (err) {
    throw new Error("Failed to write tasks file");
  }
};

// GET all tasks
router.get("/", (req, res, next) => {
  try {
    const tasks = getTasks();
    res.json(tasks);
  } catch (err) {
    next(err);
  }
});

// GET task by ID
router.get("/:id", (req, res, next) => {
  try {
    const tasks = getTasks();
    const task = tasks.find(t => t.id === req.params.id);

    if (!task) {
      return res.status(404).json({ error: "Task not found" });
    }

    res.json(task);
  } catch (err) {
    next(err);
  }
});

// POST create task
router.post("/", (req, res, next) => {
  try {
    const { title, description } = req.body;

    // Validation
    if (!title || !description) {
      return res.status(400).json({ error: "Title and description are required" });
    }

    const tasks = getTasks();

    const newTask = {
      id: Date.now().toString(),
      title,
      description,
      completed: false
    };

    tasks.push(newTask);
    saveTasks(tasks);

    res.status(201).json(newTask);
  } catch (err) {
    next(err);
  }
});

// PUT update task
router.put("/:id", (req, res, next) => {
  try {
    const tasks = getTasks();
    const index = tasks.findIndex(t => t.id === req.params.id);

    if (index === -1) {
      return res.status(404).json({ error: "Task not found" });
    }

    const { title, description, completed } = req.body;

    // Update fields if provided
    tasks[index] = {
      ...tasks[index],
      title: title ?? tasks[index].title,
      description: description ?? tasks[index].description,
      completed: completed ?? tasks[index].completed
    };

    saveTasks(tasks);

    res.json(tasks[index]);
  } catch (err) {
    next(err);
  }
});

// DELETE task
router.delete("/:id", (req, res, next) => {
  try {
    let tasks = getTasks();

    const exists = tasks.some(t => t.id === req.params.id);
    if (!exists) {
      return res.status(404).json({ error: "Task not found" });
    }

    tasks = tasks.filter(t => t.id !== req.params.id);
    saveTasks(tasks);

    res.json({ message: "Task deleted successfully" });
  } catch (err) {
    next(err);
  }
});

module.exports = router;