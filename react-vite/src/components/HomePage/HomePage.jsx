// import React, { useEffect, useState } from 'react';
// import ExperienceCard from '../ExperienceCard/ExperienceCard';
// import './HomePage.css';

// export default function HomePage() {
//   const [experiences, setExperiences] = useState([]);

//   useEffect(() => {
//     fetch('/api/experiences')
//       .then(res => res.json())
//       .then(data => {
//         // If data.experiences is an array, set it; otherwise, log and keep empty array
//         if (Array.isArray(data.experiences)) {
//           setExperiences(data.experiences);
//         } else {
//           console.error("Unexpected API response:", data);
//           setExperiences([]);
//         }
//       })
//       .catch(err => {
//         console.error("Failed to fetch experiences:", err);
//         setExperiences([]);
//       });
//   }, []);

//   return (
//     <div className="homepage">
//       <h1>Discover TryThis! Experiences</h1>
//       <div className="experience-grid">
//         {experiences.map(exp => (
//           <ExperienceCard key={exp.id} experience={exp} />
//         ))}
//       </div>
//     </div>
//   );
// }


import  { useEffect, useState } from 'react';
import ReviewCard from '../ReviewCard/ReviewCard';
import './HomePage.css';

export default function HomePage() {
  const [reviews, setReviews] = useState([]);

  useEffect(() => {
    fetch('/api/reviews/with-experience')
      .then(res => res.json())
      .then(data => {
        if (Array.isArray(data)) {
          const shuffled = [...data].sort(() => 0.5 - Math.random());
          setReviews(shuffled); // ✅ Use the shuffled array
        } else {
          console.error("Unexpected API response:", data);
          setReviews([]);
        }
      })
      .catch(err => {
        console.error("Failed to fetch reviews:", err);
        setReviews([]);
      });
  }, []);

  return (
    <div className="homepage">
      <h1>Try this Businesses!</h1>
      <div className="review-card-container">
        {reviews.map((review) => (
          <ReviewCard key={review.id} review={review} />
        ))}
      </div>
    </div>
  );
}
