import React from 'react';
import FormComponent from './FormComponent';

class App extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      firstName: '',
      lastName: '',
      age: '',
      gender: '',
      destination: '',
      lactoseFree: false,
    };
    this.handleChange = this.handleChange.bind(this);
  }

  handleChange(event) {
    const target = event.target;
    const value = target.type === 'checkbox' ? (target.checked ? 'on' : '') : target.value;
    const name = target.name;

    this.setState({
      [name]: value,
    });
  }

  render() {
    return (
      <div className="app-container">
        <h1>Travel Form</h1>
        <FormComponent
          firstName={this.state.firstName}
          lastName={this.state.lastName}
          age={this.state.age}
          gender={this.state.gender}
          destination={this.state.destination}
          lactoseFree={this.state.lactoseFree}
          handleChange={this.handleChange}
        />
      </div>
    );
  }
}

export default App;
