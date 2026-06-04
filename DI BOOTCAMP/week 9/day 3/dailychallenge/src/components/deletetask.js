import React from "react";
import { useDispatch } from "react-redux";

import { deleteTask } from "../features/plannerSlice";

function DeleteTask({ day, id }) {
  const dispatch = useDispatch();

  return (
    <button
      onClick={() =>
        dispatch(
          deleteTask({
            day,
            id,
          })
        )
      }
    >
      Delete
    </button>
  );
}

export default DeleteTask;