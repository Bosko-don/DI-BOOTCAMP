import React, { useState } from "react";

function TaskItem({
  task,
  editTask,
  deleteTask,
  day,
}) {
  const [editing, setEditing] =
    useState(false);

  const [text, setText] =
    useState(task.text);

  return (
    <li>
      {editing ? (
        <>
          <input
            value={text}
            onChange={(e) =>
              setText(e.target.value)
            }
          />

          <button
            onClick={() => {
              editTask(day, task.id, text);
              setEditing(false);
            }}
          >
            Save
          </button>
        </>
      ) : (
        <>
          {task.text}

          <button
            onClick={() =>
              setEditing(true)
            }
          >
            Edit
          </button>

          <button
            onClick={() =>
              deleteTask(day, task.id)
            }
          >
            Delete
          </button>
        </>
      )}
    </li>
  );
}

export default TaskItem;