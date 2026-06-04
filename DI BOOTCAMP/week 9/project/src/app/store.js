import { configureStore } from "@reduxjs/toolkit";

import taskReducer from "../features/tasks/taskSlice";
import categoryReducer from "../features/categories/categorySlice";

export const store = configureStore({
  reducer: {
    tasks: taskReducer,
    categories: categoryReducer,
  },
});

