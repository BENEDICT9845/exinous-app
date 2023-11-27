import React from "react";
import { Link } from "react-router-dom";
import "./LandingPage.css";

const LandingPage = () => {
  return (
    <div className="container">
      <h2 className="title">Exinous Technologies Private Limited</h2>
      <div className="options">
        <Link className="option-link" to="/triple-check">
          Pythagorean Checker
        </Link>
        <Link className="option-link" to="/array-transform">
          Array Transform
        </Link>
      </div>
    </div>
  );
};

export default LandingPage;
