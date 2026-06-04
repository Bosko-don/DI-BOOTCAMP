import { useSelector } from "react-redux";
import { selectTasksByActiveCategory } from "../selectors/selectors";

function TaskList({ onToggleDone, onRemove }) {
  const tasks = useSelector(selectTasksByActiveCategory);

  return (
    <div className="card">
      <h2>Tasks</h2>

      {tasks.length === 0 ? (
        <p>No tasks yet.</p>
      ) : (
        <ul>
          {tasks.map((task) => (
            <li key={task.id}>
              <label style={{ cursor: "pointer" }}>
                <input
                  type="checkbox"
                  checked={!!task.done}
                  onChange={() => onToggleDone(task.id)}
                />
                <span style={{ marginLeft: 8, textDecoration: task.done ? "line-through" : "none" }}>
                  {task.title}
                </span>
              </label>

              <button
                style={{ marginLeft: 12 }}
                onClick={() => onRemove(task.id)}
              >
                Delete
              </button>
            </li>
          ))}
        </ul>
      )}
    </div>
  );
}

export default TaskList;

