export class TodoList {
  constructor() {
    this.tasks = [];
  }

  addTask(task) {
    this.tasks.push({ task, completed: false });
  }

  markComplete(index) {
    if (this.tasks[index]) {
      this.tasks[index].completed = true;
    }
  }

  listTasks() {
    this.tasks.forEach((t, i) => {
      console.log(`${i + 1}. ${t.task} - ${t.completed ? "Done" : "Pending"}`);
    });
  }
}