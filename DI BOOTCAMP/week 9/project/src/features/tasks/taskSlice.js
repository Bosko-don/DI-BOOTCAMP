import { createSlice } from "@reduxjs/toolkit";

const taskSlice = createSlice({
  name: "tasks",
  initialState: {
    items: [],
  },
  reducers: {
    addTask: (state, action) => {
      state.items.push(action.payload);
    },
    toggleTaskDone: (state, action) => {
      const id = action.payload;
      const task = state.items.find((t) => t.id === id);
      if (task) task.done = !task.done;
    },
    removeTask: (state, action) => {
      const id = action.payload;
      state.items = state.items.filter((t) => t.id !== id);
    },
    clearCompleted: (state) => {
      state.items = state.items.filter((t) => !t.done);
    },
  },
});

export const { addTask, toggleTaskDone, removeTask, clearCompleted } =
  taskSlice.actions;

export default taskSlice.reducer;

