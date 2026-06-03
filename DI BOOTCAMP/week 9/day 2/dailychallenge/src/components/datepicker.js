import React from "react";
import { connect } from "react-redux";
import { selectDay } from "../redux/actions";

function DatePicker({
  selectedDay,
  selectDay,
}) {
  return (
    <input
      type="date"
      value={selectedDay}
      onChange={(e) =>
        selectDay(e.target.value)
      }
    />
  );
}

const mapStateToProps = (state) => ({
  selectedDay: state.selectedDay,
});

export default connect(
  mapStateToProps,
  { selectDay }
)(DatePicker);