import React from "react";
import { useDispatch, useSelector } from "react-redux";
import { setSelectedDay } from "../features/plannerSlice";

function Calendar() {
  const dispatch = useDispatch();

  const selectedDay = useSelector(
    (state) => state.planner.selectedDay
  );

  return (
    <div>
      <h3>Select Day</h3>

      <input
        type="date"
        value={selectedDay}
        onChange={(e) =>
          dispatch(setSelectedDay(e.target.value))
        }
      />
    </div>
  );
}

export default Calendar;