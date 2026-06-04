import { configureStore } from "@reduxjs/toolkit";
import plannerReducer from "../features/plannerSlice";

export const store = configureStore({
  reducer: {
    planner: plannerReducer,
  },
});