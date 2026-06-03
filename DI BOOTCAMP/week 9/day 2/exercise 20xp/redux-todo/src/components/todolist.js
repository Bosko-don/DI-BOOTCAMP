import React from "react";
import { connect } from "react-redux";
import { toggleTodo, removeTodo } from "../redux/actions";
import TodoItem from "./TodoItem";

function TodoList({
  todos,
  toggleTodo,
  removeTodo,
}) {
  return (
    <ul>
      {todos.map((todo) => (
        <TodoItem
          key={todo.id}
          todo={todo}
          toggleTodo={toggleTodo}
          removeTodo={removeTodo}
        />
      ))}
    </ul>
  );
}

const mapStateToProps = (state) => ({
  todos: state.todos,
});

export default connect(
  mapStateToProps,
  { toggleTodo, removeTodo }
)(TodoList);