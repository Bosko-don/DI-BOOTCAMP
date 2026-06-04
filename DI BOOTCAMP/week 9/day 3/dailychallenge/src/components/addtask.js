import React, { useState } from "react";
import { useDispatch, useSelector } from "react-redux";

import { addTask } from "../features/plannerSlice";

function AddTask() {
  const [task, setTask] = useState("");

  const dispatch = useDispatch();

  const selectedDay = useSelector(
    (state) => state.planner.selectedDay
  );

  const handleSubmit = (e) => {
    e.preventDefault();

    if (!task.trim()) return;

    dispatch(
      addTask({
        day: selectedDay,
        task,
      })
    );

    setTask("");
  };

  return (
    <form onSubmit={handleSubmit}>
      <input
        type="text"
        placeholder="New Task"
        value={task}
        onChange={(e) => setTask(e.target.value)}
      />

      <button type="submit">
        Add Task
      </button>
    </form>
  );
}

export default AddTask;