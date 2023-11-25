import React from "react";
import { BrowserRouter as Router, Routes, Route, Link } from "react-router-dom";
import PythagoreanChecker from "./PythagoreanChecker";
import LandingPage from "./LandingPage";
import "./App.css";
import NumberComparator from "./NumberComparator";

function App() {
  return (
    <Router>
      <div className="App">
        <nav>
          <ul>
            <li>
              <Link to="/">Home</Link>
            </li>
            <li>
              <Link to="/triple-check">Pythagorean Checker</Link>
            </li>
            <li>
              <Link to="/array-transform">Array Transform</Link>
            </li>
          </ul>
        </nav>

        <Routes>
          <Route path="/" element={<LandingPage />} />
          <Route path="/triple-check" element={<PythagoreanChecker />} />
          <Route path="/array-transform" element={<NumberComparator />} />
        </Routes>
      </div>
    </Router>
  );
}

export default App;
