import { createContext, useContext, useReducer } from 'react';

export const TaskContext = createContext();

export const ADD_TASK = 'ADD_TASK';
export const TOGGLE_TASK = 'TOGGLE_TASK';
export const DELETE_TASK = 'DELETE_TASK';
export const EDIT_TASK = 'EDIT_TASK';
export const SET_FILTER = 'SET_FILTER';
export const CLEAR_COMPLETED = 'CLEAR_COMPLETED';

const initialState = {
    tasks: [],
    filter: 'all'
};

function taskReducer(state, action) {
    switch (action.type) {
        case ADD_TASK:
            return {
                ...state,
                tasks: [...state.tasks, {
                    id: Date.now(),
                    text: action.payload,
                    completed: false,
                    createdAt: Date.now()
                }]
            };
        case TOGGLE_TASK:
            return {
                ...state,
                tasks: state.tasks.map(task =>
                    task.id === action.payload
                        ? { ...task, completed: !task.completed }
                        : task
                )
            };
        case DELETE_TASK:
            return {
                ...state,
                tasks: state.tasks.filter(task => task.id !== action.payload)
            };
        case EDIT_TASK:
            return {
                ...state,
                tasks: state.tasks.map(task =>
                    task.id === action.payload.id
                        ? { ...task, text: action.payload.text }
                        : task
                )
            };
        case SET_FILTER:
            return { ...state, filter: action.payload };
        case CLEAR_COMPLETED:
            return {
                ...state,
                tasks: state.tasks.filter(task => !task.completed)
            };
        default:
            return state;
    }
}

export function TaskProvider({ children }) {
    const [state, dispatch] = useReducer(taskReducer, initialState);
    return (
        <TaskContext.Provider value={{ state, dispatch }}>
            {children}
        </TaskContext.Provider>
    );
}

export function useTasks() {
    const context = useContext(TaskContext);
    if (!context) throw new Error('useTasks must be used within TaskProvider');
    return context;
}