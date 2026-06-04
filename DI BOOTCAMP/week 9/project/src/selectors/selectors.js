export const selectTasks = (state) => state.tasks.items;

export const selectCategories = (state) => state.categories.items;

export const selectActiveCategoryId = (state) =>
  state.categories.activeCategoryId;

export const selectTasksByActiveCategory = (state) => {
  const activeId = selectActiveCategoryId(state);
  const tasks = selectTasks(state);

  if (!activeId) return tasks;
  return tasks.filter((t) => t.categoryId === activeId);
};

export const selectProgress = (state) => {
  const tasks = selectTasksByActiveCategory(state);
  const total = tasks.length;
  const completed = tasks.filter((t) => t.done).length;

  return { total, completed, percent: total ? (completed / total) * 100 : 0 };
};

