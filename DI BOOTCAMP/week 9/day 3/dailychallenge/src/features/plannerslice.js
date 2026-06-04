import { createSlice } from "@reduxjs/toolkit";

const initialState = {
  selectedDay: new Date().toISOString().split("T")[0],

  tasks: {
    // Example:
    // "2026-06-04": [
    //   { id: 1, text: "Study React" }
    // ]
  },
};

const plannerSlice = createSlice({
  name: "planner",
  initialState,

  reducers: {
    setSelectedDay: (state, action) => {
      state.selectedDay = action.payload;
    },

    addTask: (state, action) => {
      const { day, task } = action.payload;

      if (!state.tasks[day]) {
        state.tasks[day] = [];
      }

      state.tasks[day].push({
        id: Date.now(),
        text: task,
      });
    },

    editTask: (state, action) => {
      const { day, id, text } = action.payload;

      const task = state.tasks[day]?.find(
        (task) => task.id === id
      );

      if (task) {
        task.text = text;
      }
    },

    deleteTask: (state, action) => {
      const { day, id } = action.payload;

      state.tasks[day] = state.tasks[day]?.filter(
        (task) => task.id !== id
      );
    },
  },
});

export const {
  setSelectedDay,
  addTask,
  editTask,
  deleteTask,
} = plannerSlice.actions;

export default plannerSlice.reducer;