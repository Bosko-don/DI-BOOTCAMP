import './App.css';
import Car from './Components/Car';
import Events from './Components/Events';
import Phone from './Components/Phone';
import Color from './Components/Color';

function App() {

  const carinfo = {
    name: "Ford",
    model: "Mustang"
  };

  return (
    <div className="App">
      <h1>Exercise 1</h1>
      <Car model={carinfo.model} />

      <hr />

      <h1>Exercise 2</h1>
      <Events />

      <hr />

      <h1>Exercise 3</h1>
      <Phone />

      <hr />

      <h1>Exercise 4</h1>
      <Color />
    </div>
  );
}

export default App;