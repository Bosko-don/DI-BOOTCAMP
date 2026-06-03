import React from "react";
import { connect } from "react-redux";
import {
  editTask,
  deleteTask,
} from "../redux/actions";

import TaskItem from "./TaskItem";

function TaskList({
  tasks,
  selectedDay,
  editTask,
  deleteTask,
}) {
  return (
    <ul>
      {tasks.map((task) => (
        <TaskItem
          key={task.id}
          task={task}
          day={selectedDay}
          editTask={editTask}
          deleteTask={deleteTask}
        />
      ))}
    </ul>
  );
}

const mapStateToProps = (state) => ({
  selectedDay: state.selectedDay,
  tasks:
    state.tasksByDay[
      state.selectedDay
    ] || [],
});

export default connect(
  mapStateToProps,
  { editTask, deleteTask }
)(TaskList);