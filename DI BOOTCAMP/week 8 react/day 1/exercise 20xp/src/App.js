import React from 'react';
import ErrorBoundary from './ErrorBoundary';
import BuggyCounter from './BuggyCounter';

class App extends React.Component {
  render() {
    return (
      <div className="app-container">
        <h1>React Error Boundary Demo</h1>

        <section>
          <h2>Simulation 1: One ErrorBoundary for two counters</h2>
          <ErrorBoundary>
            <BuggyCounter />
            <BuggyCounter />
          </ErrorBoundary>
        </section>

        <section>
          <h2>Simulation 2: Two separate ErrorBoundaries</h2>
          <div className="simulation-row">
            <ErrorBoundary>
              <BuggyCounter />
            </ErrorBoundary>
            <ErrorBoundary>
              <BuggyCounter />
            </ErrorBoundary>
          </div>
        </section>

        <section>
          <h2>Simulation 3: No ErrorBoundary</h2>
          <BuggyCounter />
        </section>
      </div>
    );
  }
}

export default App;
