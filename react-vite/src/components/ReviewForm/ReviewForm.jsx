import React, { useState, useEffect } from 'react';
import './ReviewForm.css';

export default function ReviewForm({ experienceId, onSubmit, initialReview = {}, isEditing = false }) {
  const [rating, setRating] = useState(initialReview.rating || 5);
  const [review, setReview] = useState(initialReview.review || '');
  const [errors, setErrors] = useState([]);

  useEffect(() => {
    if (isEditing) {
      setRating(initialReview.rating);
      setReview(initialReview.review);
    }
  }, [initialReview, isEditing]);

  const handleSubmit = async (e) => {
    e.preventDefault();

    const payload = {
      experience_id: experienceId,
      rating,
      review,
    };

    if (isEditing) {
      onSubmit(payload); // parent handles fetch
    } else {
      const res = await fetch('/api/reviews/', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
          'X-CSRFToken': getCSRFToken()
        },
        body: JSON.stringify(payload),
      });

      if (res.ok) {
        const data = await res.json();
        onSubmit?.(data);
        setReview('');
        setRating(5);
        setErrors([]);
      } else {
        const data = await res.json();
        setErrors(data.errors || ['An unexpected error occurred.']);
      }
    }
  };

  const getCSRFToken = () => {
    const csrf = document.cookie.split('; ').find(row => row.startsWith('csrf_token='));
    return csrf ? csrf.split('=')[1] : '';
  };

  return (
    <form onSubmit={handleSubmit} className="review-form">
      {errors.length > 0 && (
        <ul className="error-list">
          {errors.map((err, i) => <li key={i}>{err}</li>)}
        </ul>
      )}

      <div className="stars">
        {[1, 2, 3, 4, 5].map((star) => (
          <span
            key={star}
            onClick={() => setRating(star)}
            style={{
              cursor: "pointer",
              color: star <= rating ? "#ffc107" : "#e4e5e9"
            }}
          >
            ★
          </span>
        ))}
      </div>

      <textarea
        value={review}
        onChange={(e) => setReview(e.target.value)}
        placeholder="Write your review..."
        required
      />

      <button type="submit">{isEditing ? "Update" : "Submit"} Review</button>
    </form>
  );
}
