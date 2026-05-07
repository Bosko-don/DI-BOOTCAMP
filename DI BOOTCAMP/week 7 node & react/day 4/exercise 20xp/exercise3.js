import React, { Component } from 'react';
import './Exercise.css';

class Exercise extends Component {

  render() {

    const style_header = {
      color: "white",
      backgroundColor: "DodgerBlue",
      padding: "10px",
      fontFamily: "Arial"
    };

    return (
      <div>

        <h1 style={style_header}>This is a Header</h1>

        <p className="para">
          This is a Paragraph
        </p>

        <a href="https://react.dev">
          React Official Website
        </a>

        <form>
          <input type="text" placeholder="Enter Name" />
          <button>Submit</button>
        </form>

        <img
          src="https://upload.wikimedia.org/wikipedia/commons/a/a7/React-icon.svg"
          alt="React Logo"
          width="200"
        />

        <ul>
          <li>Apple</li>
          <li>Mango</li>
          <li>Banana</li>
        </ul>

      </div>
    );
  }
}

export default Exercise;