import { createSlice } from "@reduxjs/toolkit";

const categorySlice = createSlice({
  name: "categories",
  initialState: {
    items: [],
    activeCategoryId: null,
  },
  reducers: {
    addCategory: (state, action) => {
      state.items.push(action.payload);
    },
    setActiveCategory: (state, action) => {
      state.activeCategoryId = action.payload;
    },
  },
});

export const { addCategory, setActiveCategory } = categorySlice.actions;

export default categorySlice.reducer;

