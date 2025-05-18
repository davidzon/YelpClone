import { useEffect, useState } from 'react';
import { useSelector } from 'react-redux';
import { useNavigate } from 'react-router-dom';
import ExperienceCard from '../ExperienceCard/ExperienceCard';
import './MyExperiencesPage.css';

export default function MyExperiencesPage() {
  const sessionUser = useSelector(state => state.session.user);
  const [experiences, setExperiences] = useState([]);
  const navigate = useNavigate();

  useEffect(() => {
    if (!sessionUser) return;

    fetch('/api/experiences/current')
      .then(res => res.json())
      .then(data => setExperiences(data.experiences || []));
  }, [sessionUser]);

  if (!sessionUser) return <p>Please log in to view your experiences.</p>;

  return (
    <div className="my-experiences-page">
      <h2>Your Created Experiences</h2>
      {experiences.length === 0 ? (
        <div className="empty-state">
          <p>It looks like you haven’t shared an experience yet.</p>
          <p>Your local favorites could become someone else’s best memory.</p>
          <p>Start something amazing — the world is waiting to TryThis!</p>
          <button
            className="get-started-button"
            onClick={() => navigate('/create')}
          >
            Get Started!
          </button>
        </div>
      ) : (
        <div className="experience-grid">
          {experiences.map(exp => (
            <ExperienceCard key={exp.id} experience={exp} />
          ))}
        </div>
      )}
    </div>
  );
}
