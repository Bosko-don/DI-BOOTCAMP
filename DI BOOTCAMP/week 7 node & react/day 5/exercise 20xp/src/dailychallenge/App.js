import { useState } from 'react';

function App() {
  const [languages, setLanguages] = useState([
    { name: "Php", votes: 0 },
    { name: "Python", votes: 0 },
    { name: "JavaSript", votes: 0 },
    { name: "Java", votes: 0 }
  ]);

  // Function to increase votes
  const handleVote = (index) => {
    const updated = [...languages];        // Copy array
    updated[index].votes += 1;             // Increase specific item
    setLanguages(updated);                 // Update state
  };

  return (
    <div style={{ padding: '20px' }}>
      <h1>Vote Your Language!</h1>
      {languages.map((lang, index) => (
        <div key={index} style={{ margin: '10px 0' }}>
          <button onClick={() => handleVote(index)}>
            {lang.name} {lang.votes}
          </button>
        </div>
      ))}
    </div>
  );
}

export default App;