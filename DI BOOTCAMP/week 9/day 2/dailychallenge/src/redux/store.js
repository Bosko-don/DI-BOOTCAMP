import { createStore } from "redux";
import plannerReducer from "./reducer";

const loadState = () => {
  try {
    const saved = localStorage.getItem("planner");
    return saved ? JSON.parse(saved) : undefined;
  } catch {
    return undefined;
  }
};

const store = createStore(
  plannerReducer,
  loadState()
);

store.subscribe(() => {
  localStorage.setItem(
    "planner",
    JSON.stringify(store.getState())
  );
});

export default store;