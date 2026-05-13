import React, { Component } from 'react';

class App extends Component {
  constructor(props) {
    super(props);
    this.state = {
      message: '',
      inputValue: '',
      responseMessage: ''
    };
  }

  // Part I: Fetch message on mount
  async componentDidMount() {
    try {
      const response = await fetch('/api/hello');
      const data = await response.text();
      this.setState({ message: data });
    } catch (error) {
      console.error('Error fetching:', error);
    }
  }

  // Handle input change
  handleChange = (event) => {
    this.setState({ inputValue: event.target.value });
  };

  // Part II: POST data to server
  handleSubmit = async (event) => {
    event.preventDefault();
    
    try {
      const response = await fetch('/api/world', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify({ value: this.state.inputValue })
      });
      
      const data = await response.text();
      this.setState({ responseMessage: data });
    } catch (error) {
      console.error('Error posting:', error);
    }
  };

  render() {
    return (
      <div style={{ padding: '20px' }}>
        {/* Part I: Display fetched message */}
        <h1>{this.state.message}</h1>

        <hr />

        {/* Part II: Form */}
        <form onSubmit={this.handleSubmit}>
          <input
            type="text"
            name="input"
            value={this.state.inputValue}
            onChange={this.handleChange}
            placeholder="Type something..."
          />
          <button type="submit">Submit</button>
        </form>

        {/* Display server response */}
        <p>{this.state.responseMessage}</p>
      </div>
    );
  }
}

export default App;