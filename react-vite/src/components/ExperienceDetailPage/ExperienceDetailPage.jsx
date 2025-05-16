import React, { useEffect, useState } from 'react';
import { useParams } from 'react-router-dom';
import { useSelector } from 'react-redux';
import ReviewForm from '../ReviewForm/ReviewForm';
import './ExperienceDetailPage.css';

export default function ExperienceDetailPage() {
  const { id } = useParams();
  const sessionUser = useSelector(state => state.session.user);
  const [selectedImage, setSelectedImage] = useState(null);
  const [experience, setExperience] = useState(null);
  const [reviews, setReviews] = useState([]);
  const [editingReviewId, setEditingReviewId] = useState(null);

  useEffect(() => {
    fetch(`/api/experiences/${id}`)
      .then(res => res.json())
      .then(setExperience);
  }, [id]);

  useEffect(() => {
    fetch(`/api/reviews/experience/${id}`)
      .then(res => res.json())
      .then(setReviews);
  }, [id]);

  const handleReviewSubmit = (newReview) => {
    setReviews(prev => [...prev, newReview]);
  };

  const handleReviewUpdate = async (reviewId, updatedReview) => {
    const res = await fetch(`/api/reviews/${reviewId}`, {
      method: 'PUT',
      headers: {
        'Content-Type': 'application/json',
        'X-CSRFToken': getCSRFToken()
      },
      body: JSON.stringify(updatedReview),
    });

    if (res.ok) {
      const updated = await res.json();
      setReviews(prev =>
        prev.map((rev) => (rev.id === reviewId ? updated : rev))
      );
      setEditingReviewId(null);
    }
  };

  const handleDelete = async (reviewId) => {
    const res = await fetch(`/api/reviews/${reviewId}`, {
      method: 'DELETE',
      headers: { 'X-CSRFToken': getCSRFToken() },
    });

    if (res.ok) {
      setReviews(prev => prev.filter((rev) => rev.id !== reviewId));
    }
  };

  const getCSRFToken = () => {
    const csrf = document.cookie.split('; ').find(row => row.startsWith('csrf_token='));
    return csrf ? csrf.split('=')[1] : '';
  };

  if (!experience) return <p>Loading...</p>;

  const userHasReviewed = sessionUser && reviews.some(r => r.user_id === sessionUser.id);

  return (
    <div className="experience-detail">
      <h1>{experience.title}</h1>

      {/* ✅ Show Experience Images if available */}
      {experience.images && experience.images.length > 0 && (
        <div className="experience-images">
          {experience.images.map(img => (
            <img
              key={img.id}
              src={img.url}
              alt={img.caption || experience.title}
              className="experience-image"
               onClick={() => setSelectedImage(img.url)}
            />
          ))}
        </div>
      )}

      <p>{experience.description}</p>
      <p><strong>Category:</strong> {experience.category}</p>
      <p><strong>Price:</strong> ${experience.price}</p>
      <p><strong>Location:</strong> {experience.location}</p>

      <h2>Reviews</h2>
      {reviews.length > 0 ? (
        <ul className="review-list">
          {reviews.map((review) => (
            <li key={review.id}>
              {editingReviewId === review.id ? (
                <ReviewForm
                  experienceId={experience.id}
                  initialReview={review}
                  onSubmit={(data) => handleReviewUpdate(review.id, data)}
                  isEditing
                />
              ) : (
                <>
                  <div className="star-display">
                    {"★".repeat(review.rating)}{"☆".repeat(5 - review.rating)}
                  </div>
                  <p>{review.review}</p>
                  {sessionUser?.id === review.user_id && (
                    <div className="review-actions">
                      <button onClick={() => setEditingReviewId(review.id)}>Edit</button>
                      <button onClick={() => handleDelete(review.id)}>Delete</button>
                    </div>
                  )}
                </>
              )}
            </li>
          ))}
        </ul>
      ) : (
        <p>No reviews yet — be the first!</p>
      )}

      {sessionUser && !userHasReviewed && (
        <>
          <h3>Leave a Review</h3>
          <ReviewForm experienceId={experience.id} onSubmit={handleReviewSubmit} />
        </>
      )}

        {selectedImage && (
        <div className="image-modal" onClick={() => setSelectedImage(null)}>
            <div className="image-modal-content" onClick={(e) => e.stopPropagation()}>
            <img src={selectedImage} alt="Enlarged experience" />
            <button onClick={() => setSelectedImage(null)}>Close ✖</button>
            </div>
        </div>
        )}

    </div>
  );
}
