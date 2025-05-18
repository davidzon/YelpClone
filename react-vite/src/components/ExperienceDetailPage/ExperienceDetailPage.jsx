import { useEffect, useState } from 'react';
import { useParams, useNavigate } from 'react-router-dom';
import { useSelector } from 'react-redux';
import { toast } from 'react-toastify';
import ReviewForm from '../ReviewForm/ReviewForm';
import ConfirmModal from '../ConfirmModal/ConfirmModal';
import './ExperienceDetailPage.css';

export default function ExperienceDetailPage() {
  const { id } = useParams();
  const navigate = useNavigate();
  const sessionUser = useSelector(state => state.session.user);

  const [selectedImage, setSelectedImage] = useState(null); // holds image object now
  const [experience, setExperience] = useState(null);
  const [reviews, setReviews] = useState([]);
  const [editingReviewId, setEditingReviewId] = useState(null);
  const [showDeleteModal, setShowDeleteModal] = useState(false);
  const [imageURL, setImageURL] = useState('');
  const [caption, setCaption] = useState('');

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

  const getCSRFToken = () => {
    const csrf = document.cookie.split('; ').find(row => row.startsWith('csrf_token='));
    return csrf ? csrf.split('=')[1] : '';
  };

  const handleReviewSubmit = (newReview) => {
    setReviews(prev => [...prev, newReview]);
  };

  const handleReviewUpdate = async (reviewId, updatedReview) => {
    const res = await fetch(`/api/reviews/${reviewId}`, {
      method: 'PUT',
      credentials: 'include',
      headers: {
        'Content-Type': 'application/json',
        'X-CSRFToken': getCSRFToken()
      },
      body: JSON.stringify(updatedReview),
    });

    if (res.ok) {
      const updated = await res.json();
      setReviews(prev => prev.map((rev) => (rev.id === reviewId ? updated : rev)));
      setEditingReviewId(null);
    }
  };

  const handleReviewDelete = async (reviewId) => {
    const res = await fetch(`/api/reviews/${reviewId}`, {
      method: 'DELETE',
      credentials: 'include',
      headers: { 'X-CSRFToken': getCSRFToken() },
    });

    if (res.ok) {
      setReviews(prev => prev.filter((rev) => rev.id !== reviewId));
    }
  };

  const handleExperienceDelete = async () => {
    const res = await fetch(`/api/experiences/${experience.id}`, {
      method: 'DELETE',
      credentials: 'include',
      headers: {
        'Content-Type': 'application/json',
        'X-CSRFToken': getCSRFToken()
      }
    });

    if (res.ok) {
      toast.success("Experience deleted.");
      navigate('/');
    } else {
      toast.error("Failed to delete experience.");
    }
  };

  const handleImageUpload = async (e) => {
    e.preventDefault();
    const csrf = getCSRFToken();

    const res = await fetch("/api/images", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
        "X-CSRFToken": csrf
      },
      credentials: "include",
      body: JSON.stringify({
        url: imageURL,
        caption,
        experience_id: experience.id
      })
    });

    if (res.ok) {
      const newImg = await res.json();
      setExperience(prev => ({
        ...prev,
        images: [...prev.images, newImg]
      }));
      setImageURL('');
      setCaption('');
      toast.success("Image added!");
    }
  };

  const handleImageDelete = async (imageId) => {
    const res = await fetch(`/api/images/${imageId}`, {
      method: 'DELETE',
      credentials: 'include',
      headers: {
        'X-CSRFToken': getCSRFToken()
      }
    });

    if (res.ok) {
      setExperience(prev => ({
        ...prev,
        images: prev.images.filter(img => img.id !== imageId)
      }));
      toast.success("Image deleted.");
      setSelectedImage(null); // close modal after delete
    } else {
      toast.error("Failed to delete image.");
    }
  };

  if (!experience) return <p>Loading...</p>;

  const userHasReviewed = sessionUser && reviews.some(r => r.user_id === sessionUser.id);

  return (
    <div className="experience-detail">
      <h1>{experience.title}</h1>

      {experience.images?.length > 0 && (
        <div className="experience-images">
          {experience.images.map(img => (
            <img
              key={img.id}
              src={img.url}
              alt={img.caption || experience.title}
              className="experience-image"
              onClick={() => setSelectedImage(img)}
            />
          ))}
        </div>
      )}

      <h2>{experience.description}</h2>
      <div className="detail-container">
        <p><strong>Category:</strong> {experience.category}</p>
        <p><strong>Price:</strong> ${experience.price}</p>
        <p><strong>Location:</strong> {experience.location}</p>
      </div>

      {sessionUser?.id === experience.creator_id && (
        <div className="experience-actions">
          <button onClick={() => navigate(`/experiences/${experience.id}/edit`)}>Edit</button>
          <button onClick={() => setShowDeleteModal(true)}>Delete</button>
        </div>
      )}

      {sessionUser && (
        <form onSubmit={handleImageUpload} className="upload-image-form">
          <h3>Add an Image</h3>
          <input
            type="text"
            placeholder="Image URL"
            value={imageURL}
            onChange={(e) => setImageURL(e.target.value)}
            required
          />
          <input
            type="text"
            placeholder="Caption (optional)"
            value={caption}
            onChange={(e) => setCaption(e.target.value)}
          />
          <button type="submit">Upload</button>
        </form>
      )}

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
                  <p className="review-username"><strong>{review.user?.username}</strong></p>
                  <div className="star-display">
                    {"★".repeat(review.rating)}{"☆".repeat(5 - review.rating)}
                  </div>
                  <p>{review.review}</p>
                  {sessionUser?.id === review.user_id && (
                    <div className="review-actions">
                      <button onClick={() => setEditingReviewId(review.id)}>Edit</button>
                      <button onClick={() => handleReviewDelete(review.id)}>Delete</button>
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
            <img src={selectedImage.url} alt="Enlarged experience" />
            {(sessionUser?.id === selectedImage.user_id || sessionUser?.id === experience.creator_id) && (
              <button
                onClick={() => handleImageDelete(selectedImage.id)}
                className="delete-image-button"
              >
                Delete Image
              </button>
            )}
            <button onClick={() => setSelectedImage(null)}>Close ✖</button>
          </div>
        </div>
      )}

      {showDeleteModal && (
        <ConfirmModal
          message="Are you sure you want to delete this experience?"
          onConfirm={handleExperienceDelete}
          onCancel={() => setShowDeleteModal(false)}
        />
      )}
    </div>
  );
}
