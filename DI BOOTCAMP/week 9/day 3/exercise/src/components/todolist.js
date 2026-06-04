import React from "react";
import { useSelector } from "react-redux";

import TodoItem from "./TodoItem";

function TodoList() {
  const todos = useSelector(
    (state) => state.todos.todos
  );

  return (
    <div>
      <h2>Todo List</h2>

      {todos.length === 0 ? (
        <p>No todos yet.</p>
      ) : (
        <ul>
          {todos.map((todo) => (
            <TodoItem
              key={todo.id}
              todo={todo}
            />
          ))}
        </ul>
      )}
    </div>
  );
}

export default TodoList;