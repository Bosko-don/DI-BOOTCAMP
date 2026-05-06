import { TodoList } from './todo.js';

const todo = new TodoList();

todo.addTask("Learn Node.js");
todo.addTask("Build app");
todo.markComplete(0);

todo.listTasks();