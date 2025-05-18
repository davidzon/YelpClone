// src/components/CreateExperiencePage/CreateExperiencePage.jsx

import { useState, useEffect } from 'react';
import { useNavigate } from 'react-router-dom';
import './CreateExperiencePage.css';
import { toast } from 'react-toastify'; // ✅ import toast
import 'react-toastify/dist/ReactToastify.css';

export default function CreateExperiencePage() {
  const [formData, setFormData] = useState({
    title: '', description: '', location: '', category: '', price: ''
  });

  const [allImages, setAllImages] = useState([]);
  const [currentIndex, setCurrentIndex] = useState(0);
  const navigate = useNavigate();

  const getCSRFToken = () => {
    const cookie = document.cookie
      .split('; ')
      .find(row => row.startsWith('csrf_token='));
    return cookie ? cookie.split('=')[1] : '';
  };

  useEffect(() => {
    fetch('/api/experiences')
      .then(res => res.json())
      .then(data => {
        const images = [];
        data.experiences.forEach(exp => {
          if (exp.images && Array.isArray(exp.images)) {
            images.push(...exp.images);
          }
        });
        setAllImages(images);
      });
  }, []);

  useEffect(() => {
    if (allImages.length === 0) return;
    const interval = setInterval(() => {
      setCurrentIndex(prev => (prev + 1) % allImages.length);
    }, 3000);
    return () => clearInterval(interval);
  }, [allImages]);

  const handleChange = e => {
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
    const csrfToken = getCSRFToken();

    const res = await fetch('/api/experiences', {
      method: 'POST',
      credentials: "include",
      headers: {
        'Content-Type': 'application/json',
        'X-CSRFToken': csrfToken
      },
      body: JSON.stringify(formData)
    });

    if (res.ok) {
      const newExp = await res.json();
      toast.success("Experience created successfully!");
      navigate(`/experiences/${newExp.id}`);
    } else {
      const errData = await res.json();
      toast.error("Failed to create: " + JSON.stringify(errData.errors || errData));
    }
  };

  return (
    <div className="create-page-container">
      <form className="create-form" onSubmit={handleSubmit}>
        <h2>Create A New Experience</h2>
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
        <button type="submit">Create</button>
      </form>

      {allImages.length > 0 && (
        <div className="image-slideshow">
          <img
            src={allImages[currentIndex]?.url}
            alt={allImages[currentIndex]?.caption || "Experience"}
            className="slideshow-image"
          />
          <p className="image-caption">{allImages[currentIndex]?.caption}</p>
        </div>
      )}
    </div>
  );
}
