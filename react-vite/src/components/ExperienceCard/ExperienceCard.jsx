import React from 'react';
import { Link } from 'react-router-dom';
import './ExperienceCard.css';

export default function ExperienceCard({ experience }) {
  return (
    <Link to={`/experiences/${experience.id}`} className="experience-card">
      {experience.previewImage && (
        <img
          src={experience.previewImage}
          alt={experience.title}
          className="experience-image"
        />
      )}
      <div className="experience-details">
        <h3>{experience.title}</h3>
        <p>{experience.location}</p>
        <p>${experience.price}</p>
      </div>
    </Link>
  );
}
