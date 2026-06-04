import { useSelector } from "react-redux";

function AgeDisplay() {
  const { age, loading } = useSelector(
    (state) => state.age
  );

  return (
    <div className="display">
      <h1>Age Tracker</h1>

      {loading ? (
        <div className="spinner"></div>
      ) : (
        <h2>Age: {age}</h2>
      )}
    </div>
  );
}

export default AgeDisplay;