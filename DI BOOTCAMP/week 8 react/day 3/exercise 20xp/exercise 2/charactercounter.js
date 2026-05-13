import React, {
  useRef,
  useState,
} from "react";

function CharacterCounter() {
  const inputRef =
    useRef(null);

  const [count, setCount] =
    useState(0);

  const handleChange = () => {
    const length =
      inputRef.current
        .value.length;

    setCount(length);
  };

  return (
    <div
      style={{
        padding: "30px",
      }}
    >
      <h1>
        Character Counter
      </h1>

      <textarea
        ref={inputRef}
        onChange={handleChange}
        rows="5"
        cols="40"
        placeholder="Type here..."
      />

      <h2>
        Characters: {count}
      </h2>
    </div>
  );
}

export default CharacterCounter;