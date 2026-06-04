import { createSlice, createAsyncThunk } from "@reduxjs/toolkit";

// Age Up Async
export const ageUpAsync = createAsyncThunk(
  "age/ageUpAsync",
  async () => {
    await new Promise((resolve) =>
      setTimeout(resolve, 1000)
    );

    return 1;
  }
);

// Age Down Async
export const ageDownAsync = createAsyncThunk(
  "age/ageDownAsync",
  async () => {
    await new Promise((resolve) =>
      setTimeout(resolve, 1000)
    );

    return 1;
  }
);

const ageSlice = createSlice({
  name: "age",
  initialState: {
    age: 18,
    loading: false,
  },
  reducers: {},
  extraReducers: (builder) => {
    builder

      // AGE UP
      .addCase(ageUpAsync.pending, (state) => {
        state.loading = true;
      })
      .addCase(ageUpAsync.fulfilled, (state) => {
        state.age += 1;
        state.loading = false;
      })
      .addCase(ageUpAsync.rejected, (state) => {
        state.loading = false;
      })

      // AGE DOWN
      .addCase(ageDownAsync.pending, (state) => {
        state.loading = true;
      })
      .addCase(ageDownAsync.fulfilled, (state) => {
        state.age -= 1;
        state.loading = false;
      })
      .addCase(ageDownAsync.rejected, (state) => {
        state.loading = false;
      });
  },
});

export default ageSlice.reducer;