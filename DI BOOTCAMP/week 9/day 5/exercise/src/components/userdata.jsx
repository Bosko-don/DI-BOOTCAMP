import { useDispatch, useSelector } from "react-redux";
import { fetchUser } from "../features/users/userSlice";

function UserData() {
  const dispatch = useDispatch();

  const { data, loading, error } = useSelector(
    (state) => state.user
  );

  return (
    <div className="card">
      <h1>User Information</h1>

      <button
        onClick={() => dispatch(fetchUser())}
      >
        Fetch User
      </button>

      {loading && <p>Loading...</p>}

      {error && (
        <p className="error">
          Error: {error}
        </p>
      )}

      {data.id && (
        <div className="user-info">
          <h2>{data.name}</h2>
          <p>Email: {data.email}</p>
          <p>Phone: {data.phone}</p>
          <p>Website: {data.website}</p>
        </div>
      )}
    </div>
  );
}

export default UserData;