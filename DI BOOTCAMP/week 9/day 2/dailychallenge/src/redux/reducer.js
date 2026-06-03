import {
  SELECT_DAY,
  ADD_TASK,
  EDIT_TASK,
  DELETE_TASK,
} from "./actions";

const initialState = {
  selectedDay: new Date().toISOString().split("T")[0],
  tasksByDay: {},
};

function plannerReducer(state = initialState, action) {
  switch (action.type) {
    case SELECT_DAY:
      return {
        ...state,
        selectedDay: action.payload,
      };

    case ADD_TASK: {
      const { day, task } = action.payload;

      return {
        ...state,
        tasksByDay: {
          ...state.tasksByDay,
          [day]: [
            ...(state.tasksByDay[day] || []),
            task,
          ],
        },
      };
    }

    case EDIT_TASK: {
      const { day, id, text } = action.payload;

      return {
        ...state,
        tasksByDay: {
          ...state.tasksByDay,
          [day]: state.tasksByDay[day].map((task) =>
            task.id === id
              ? { ...task, text }
              : task
          ),
        },
      };
    }

    case DELETE_TASK: {
      const { day, id } = action.payload;

      return {
        ...state,
        tasksByDay: {
          ...state.tasksByDay,
          [day]: state.tasksByDay[day].filter(
            (task) => task.id !== id
          ),
        },
      };
    }

    default:
      return state;
  }
}

export default plannerReducer;