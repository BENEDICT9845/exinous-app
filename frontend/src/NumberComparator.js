import React, { useState } from "react";
import "./NumberComparator.css";

function NumberComparator() {
  const [inputNumbers, setInputNumbers] = useState("");
  const [comparisons, setComparisons] = useState([]);

  const handleInputChange = (event) => {
    setInputNumbers(event.target.value);
  };

  const compareNumbers = async () => {
    try {
      const response = await fetch("http://127.0.0.1:5000/compare", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({ numbers: inputNumbers.split(",") }),
      });

      if (response.ok) {
        const data = await response.json();
        setComparisons(data.comparisons);
      } else {
        throw new Error("Failed to fetch data");
      }
    } catch (error) {
      console.error("Error:", error);
    }
  };

  return (
    <div className="number-comparator-container">
      <h1>Array Transform </h1>
      <input
        type="text"
        placeholder="Enter comma-separated numbers"
        value={inputNumbers}
        onChange={handleInputChange}
        className="number-input"
      />
      <br></br>
      <br></br>
      <button onClick={compareNumbers} className="compare-button">
        Transform
      </button>
      <div className="comparison-results">
        {comparisons.map((comparison, index) => (
          <p key={index}>{comparison}</p>
        ))}
      </div>
    </div>
  );
}

export default NumberComparator;
