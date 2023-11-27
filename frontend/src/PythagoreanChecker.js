import React, { useState } from "react";
import "./PythagoreanChecker.css";

function PythagoreanChecker() {
  const [inputArray, setInputArray] = useState([]);
  const [result, setResult] = useState("");

  const handleSubmit = async () => {
    try {
      const response = await fetch("http://127.0.0.1:5000/check-pythagorean", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({ inputArray }),
      });
      const data = await response.json();
      setResult(data.result);
    } catch (error) {
      console.error("Error:", error);
    }
  };

  return (
    <div className="PythagoreanChecker">
      <h1>Pythagorean Triple Checker</h1>
      <div className="input-section">
        <input
          type="text"
          value={inputArray}
          onChange={(e) => setInputArray(e.target.value.split(",").map(Number))}
          placeholder="Enter comma-separated numbers"
        />
        <br></br>
        <br></br>
        <button onClick={handleSubmit}>Check</button>
      </div>
      <div className="result-section">{result && <p>Result: {result}</p>}</div>
    </div>
  );
}

export default PythagoreanChecker;
