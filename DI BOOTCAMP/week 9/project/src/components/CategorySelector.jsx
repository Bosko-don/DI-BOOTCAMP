import { useDispatch, useSelector } from "react-redux";
import { selectCategories, selectActiveCategoryId } from "../selectors/selectors";
import { setActiveCategory } from "../features/categories/categorySlice";

function CategorySelector() {
  const dispatch = useDispatch();
  const categories = useSelector(selectCategories);
  const activeCategoryId = useSelector(selectActiveCategoryId);

  return (
    <div className="card">
      <h2>Category</h2>

      <select
        value={activeCategoryId ?? "all"}
        onChange={(e) => {
          const val = e.target.value;
          dispatch(setActiveCategory(val === "all" ? null : val));
        }}
      >
        <option value="all">All</option>
        {categories.map((cat) => (
          <option key={cat.id} value={cat.id}>
            {cat.name}
          </option>
        ))}
      </select>
    </div>
  );
}

export default CategorySelector;

