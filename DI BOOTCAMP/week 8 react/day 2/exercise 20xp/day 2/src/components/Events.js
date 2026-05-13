import React, { useState } from 'react';

function Events() {

  // Part I
  const clickMe = () => {
    alert("I was clicked");
  };

  // Part II
  const handleKeyDown = (event) => {
    if (event.key === "Enter") {
      alert(`The Enter Key was pressed, your input is: ${event.target.value}`);
    }
  };

  // Part III
  const [isToggleOn, setIsToggleOn] = useState(true);

  const toggleButton = () => {
    setIsToggleOn(!isToggleOn);
  };

  return (
    <div>

      <button onClick={clickMe}>
        Click Me
      </button>

      <br /><br />

      <input
        type="text"
        placeholder="Press Enter"
        onKeyDown={handleKeyDown}
      />

      <br /><br />

      <button onClick={toggleButton}>
        {isToggleOn ? "ON" : "OFF"}
      </button>

    </div>
  );
}

export default Events;