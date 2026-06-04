import { useDispatch } from "react-redux";

import TaskList from "./components/TaskList";
import CategorySelector from "./components/CategorySelector";
import ProgressSummary from "./components/ProgressSummary";

import {
  clearCompleted,
  toggleTaskDone,
  removeTask,
} from "./features/tasks/taskSlice";

function App() {
  const dispatch = useDispatch();

  return (
    <div className="container">
      <h1>Tasks by Category</h1>

      <div style={{ display: "grid", gridTemplateColumns: "1fr 1fr", gap: 16 }}>
        <CategorySelector />
        <ProgressSummary />
      </div>

      <div style={{ marginTop: 16 }}>
        <TaskList
          onToggleDone={(id) => dispatch(toggleTaskDone(id))}
          onRemove={(id) => dispatch(removeTask(id))}
        />

        <div style={{ marginTop: 12 }}>
          <button onClick={() => dispatch(clearCompleted())}>Clear completed</button>
        </div>
      </div>
    </div>
  );
}

export default App;

