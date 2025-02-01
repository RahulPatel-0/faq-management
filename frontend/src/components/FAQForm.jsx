import React, { useState } from "react";
import { createFAQ } from "../api";

function FAQForm() {
  const [formData, setFormData] = useState({ question: "", answer: "" });

  const handleChange = (e) => {
    setFormData({ ...formData, [e.target.name]: e.target.value });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    await createFAQ(formData);
    alert("FAQ Added Successfully!");
  };

  return (
    <div className="container mt-4">
      <h2>Add New FAQ</h2>
      <form onSubmit={handleSubmit}>
        <div className="mb-3">
          <label className="form-label">Question</label>
          <input
            type="text"
            className="form-control"
            name="question"
            onChange={handleChange}
            required
          />
        </div>
        <div className="mb-3">
          <label className="form-label">Answer</label>
          <textarea
            className="form-control"
            name="answer"
            onChange={handleChange}
            required
          ></textarea>
        </div>
        <button type="submit" className="btn btn-primary">
          Submit
        </button>
      </form>
    </div>
  );
}

export default FAQForm;
