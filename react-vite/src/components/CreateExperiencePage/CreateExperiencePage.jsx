import React, { useState } from 'react';
import './CreateExperiencePage.css';

export default function CreateExperiencePage() {
  const [formData, setFormData] = useState({
    title: '', description: '', location: '', category: '', price: ''
  });

  const handleChange = e => setFormData({ ...formData, [e.target.name]: e.target.value });

  const handleSubmit = e => {
    e.preventDefault();
    fetch('/api/experiences', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(formData)
    }).then(() => alert('Experience created!'));
  };

  return (
    <form className="create-form" onSubmit={handleSubmit}>
      <h2>Create New Experience</h2>
      {Object.keys(formData).map(field => (
        <input key={field} name={field} placeholder={field} value={formData[field]} onChange={handleChange} required />
      ))}
      <button type="submit">Create</button>
    </form>
  );
}
