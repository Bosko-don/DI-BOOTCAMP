import { useState, useRef, useEffect } from 'react';
import { useTasks, EDIT_TASK, TOGGLE_TASK, DELETE_TASK } from '../context/TaskContext';

export default function TaskItem({ task }) {
    const { dispatch } = useTasks();
    const [isEditing, setIsEditing] = useState(false);
    const [editText, setEditText] = useState(task.text);
    const editInputRef = useRef(null);

    useEffect(() => {
        if (isEditing && editInputRef.current) {
            editInputRef.current.focus();
            editInputRef.current.select();
        }
    }, [isEditing]);

    const handleSave = () => {
        const trimmed = editText.trim();
        if (trimmed && trimmed !== task.text) {
            dispatch({ type: EDIT_TASK, payload: { id: task.id, text: trimmed } });
        }
        setIsEditing(false);
    };

    const handleKeyDown = (e) => {
        if (e.key === 'Enter') handleSave();
        if (e.key === 'Escape') {
            setEditText(task.text);
            setIsEditing(false);
        }
    };

    return (
        <li className={`task-item ${task.completed ? 'completed' : ''}`}>
            <div
                className={`checkbox ${task.completed ? 'checked' : ''}`}
                onClick={() => dispatch({ type: TOGGLE_TASK, payload: task.id })}
            />
            <div className="task-content">
                {isEditing ? (
                    <input
                        ref={editInputRef}
                        value={editText}
                        onChange={(e) => setEditText(e.target.value)}
                        onKeyDown={handleKeyDown}
                        onBlur={handleSave}
                        className="edit-input"
                    />
                ) : (
                    <span className="task-text" onClick={() => setIsEditing(true)}>
                        {task.text}
                    </span>
                )}
            </div>
            <div className="task-actions">
                {isEditing ? (
                    <>
                        <button className="icon-btn save-btn" onClick={handleSave}>✓</button>
                        <button className="icon-btn cancel-btn" onClick={() => {
                            setEditText(task.text);
                            setIsEditing(false);
                        }}>✕</button>
                    </>
                ) : (
                    <>
                        <button className="icon-btn edit-btn" onClick={() => setIsEditing(true)}>✎</button>
                        <button className="icon-btn delete-btn" onClick={() => dispatch({ type: DELETE_TASK, payload: task.id })}>🗑</button>
                    </>
                )}
            </div>
        </li>
    );
}