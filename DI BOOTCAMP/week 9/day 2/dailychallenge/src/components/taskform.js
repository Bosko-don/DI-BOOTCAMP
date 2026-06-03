import React, { useState } from "react";
import { connect } from "react-redux";
import { addTask } from "../redux/actions";

function TaskForm({
  selectedDay,
  addTask,
}) {
  const [text, setText] = useState("");

  const submit = (e) => {
    e.preventDefault();

    if (!text.trim()) return;

    addTask(selectedDay, {
      id: Date.now(),
      text,
    });

    setText("");
  };

  return (
    <form onSubmit={submit}>
      <input
        value={text}
        placeholder="New Task"
        onChange={(e) =>
          setText(e.target.value)
        }
      />

      <button>Add</button>
    </form>
  );
}

const mapStateToProps = (state) => ({
  selectedDay: state.selectedDay,
});

export default connect(
  mapStateToProps,
  { addTask }
)(TaskForm);