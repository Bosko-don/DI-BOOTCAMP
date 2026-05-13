import React from "react";
import CharacterCounter from "./CharacterCounter";
import "./index.css";

function App() {
  return (
    <div className="app">
      <div className="container">
        <h1 className="title">
          React Character Counter
        </h1>

        <CharacterCounter />
      </div>
    </div>
  );
}

export default App;