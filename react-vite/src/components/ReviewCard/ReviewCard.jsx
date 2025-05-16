import { Link } from "react-router-dom";
import "./ReviewCard.css";

export default function ReviewCard({ review }) {
  const { experience, user, rating, review: text } = review;

  return (
    <Link to={`/experiences/${experience.id}`} className="review-card-link">
      <div className="review-card">
        <div className="review-header">
          <img
            className="profile-pic"
            src={`https://i.pravatar.cc/40?u=${user.id}`}
            alt={`${user.username} profile`}
          />
          <div>
            <div className="reviewer-name">{user.username} wrote a review</div>
            <div className="review-time">Just now</div>
          </div>
        </div>

        <img
          className="experience-image"
          src={experience.previewImage}
          alt={experience.title}
        />

        <div className="review-content">
          <h3>{experience.title}</h3>
          <div className="stars">
            {"★".repeat(rating)}
            {"☆".repeat(5 - rating)}
          </div>
          <p>{text.slice(0, 100)}...</p>

        </div>

        {/* <div className="review-reactions">
          <span>💡</span>
          <span>😂</span>
          <span>❤️</span>
          <span>👍</span>
        </div> */}
      </div>
    </Link>
  );
}
