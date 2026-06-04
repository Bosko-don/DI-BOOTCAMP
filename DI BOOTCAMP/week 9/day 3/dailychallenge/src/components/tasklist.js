import React from "react";
import { useSelector } from "react-redux";

import EditTask from "./EditTask";
import DeleteTask from "./DeleteTask";

function TaskList() {
  const selectedDay = useSelector(
    (state) => state.planner.selectedDay
  );

  const tasks = useSelector(
    (state) =>
      state.planner.tasks[selectedDay] || []
  );

  return (
    <div>
      <h2>
        Tasks for {selectedDay}
      </h2>

      {tasks.length === 0 ? (
        <p>No tasks for this day.</p>
      ) : (
        <ul>
          {tasks.map((task) => (
            <li key={task.id}>
              {task.text}

              <EditTask
                task={task}
                day={selectedDay}
              />

              <DeleteTask
                day={selectedDay}
                id={task.id}
              />
            </li>
          ))}
        </ul>
      )}
    </div>
  );
}

export default TaskList;