import { useSelector } from "react-redux";
import { selectProgress } from "../selectors/selectors";

function ProgressSummary() {
  const { total, completed, percent } = useSelector(selectProgress);

  return (
    <div className="card">
      <h2>Progress</h2>
      <p>
        {completed} / {total} completed
      </p>
      <div
        style={{
          height: 12,
          background: "#eee",
          borderRadius: 999,
          overflow: "hidden",
          width: "100%",
        }}
      >
        <div
          style={{
            height: "100%",
            width: `${percent}%`,
            background: "#4f46e5",
          }}
        />
      </div>
    </div>
  );
}

export default ProgressSummary;

