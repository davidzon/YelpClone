// src/components/AllExperiencesPage/AllExperiencesPage.jsx

import { useEffect, useState } from 'react';
import { Link } from 'react-router-dom';
import './AllExperiencesPage.css';

export default function AllExperiencesPage() {
  const [experiences, setExperiences] = useState([]);

  useEffect(() => {
    fetch('/api/experiences')
      .then(res => res.json())
      .then(data => {
        if (data.experiences) setExperiences(data.experiences);
      });
  }, []);

  return (
    <div className="all-experiences-page">
      <h1>Explore All Experiences</h1>
      <div className="experience-grid">
        {experiences.map((exp) => (
          <Link to={`/experiences/${exp.id}`} key={exp.id} className="experience-card">
            {exp.images && exp.images.length > 0 && (
              <img src={exp.images[0].url} alt={exp.title} />
            )}
            <div className="details">
              <h2>{exp.title}</h2>
              <p><strong>Category:</strong> {exp.category}</p>
              <p><strong>Price:</strong> ${exp.price}</p>
              <p><strong>Location:</strong> {exp.location}</p>
            </div>
          </Link>
        ))}
      </div>
    </div>
  );
}
