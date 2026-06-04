import React, { useState } from "react";
import { useDispatch } from "react-redux";

import { editTask } from "../features/plannerSlice";

function EditTask({ task, day }) {
  const [editing, setEditing] = useState(false);
  const [text, setText] = useState(task.text);

  const dispatch = useDispatch();

  const saveTask = () => {
    dispatch(
      editTask({
        day,
        id: task.id,
        text,
      })
    );

    setEditing(false);
  };

  if (editing) {
    return (
      <>
        <input
          value={text}
          onChange={(e) =>
            setText(e.target.value)
          }
        />

        <button onClick={saveTask}>
          Save
        </button>
      </>
    );
  }

  return (
    <button
      onClick={() => setEditing(true)}
    >
      Edit
    </button>
  );
}

export default EditTask;