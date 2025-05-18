// src/components/EditExperiencePage/EditExperiencePage.jsx

import { useState, useEffect } from "react";
import { useParams, useNavigate } from "react-router-dom";
import { toast } from "react-toastify"; // ✅ Add toast
import "react-toastify/dist/ReactToastify.css";
import "./EditExperiencePage.css";

export default function EditExperiencePage() {
  const { id } = useParams();
  const navigate = useNavigate();
  const [formData, setFormData] = useState({
    title: "", description: "", location: "", category: "", price: ""
  });

  useEffect(() => {
    fetch(`/api/experiences/${id}`)
      .then(res => res.json())
      .then(data => {
        setFormData({
          title: data.title,
          description: data.description,
          location: data.location,
          category: data.category,
          price: data.price
        });
      });
  }, [id]);

  const handleChange = (e) => {
    const { name, value } = e.target;

    let valid = true;
    if (name === 'location' || name === 'category') {
      valid = /^[a-zA-Z\s]*$/.test(value);
    }
    if (name === 'price') {
      valid = /^\d*$/.test(value);
    }
    if (!valid) return;

    setFormData({ ...formData, [name]: value });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    const csrfToken = document.cookie.split('; ').find(row => row.startsWith('csrf_token='))?.split('=')[1];

    const res = await fetch(`/api/experiences/${id}`, {
      method: "PUT",
      headers: {
        "Content-Type": "application/json",
        "X-CSRFToken": csrfToken
      },
      credentials: "include",
      body: JSON.stringify(formData)
    });

    if (res.ok) {
      const updated = await res.json();
      toast.success("Experience updated successfully!");
      navigate(`/experiences/${updated.id}`);
    } else {
      const err = await res.json();
      toast.error("Failed to update: " + JSON.stringify(err.errors || err));
    }
  };

  return (
    <form onSubmit={handleSubmit} className="edit-experience-form">
      <h2>Edit Experience</h2>
      {Object.keys(formData).map(field => (
        <input
          key={field}
          name={field}
          placeholder={field}
          value={formData[field]}
          onChange={handleChange}
          required
        />
      ))}
      <button type="submit">Save Changes</button>
    </form>
  );
}
