from .db import db, environment, SCHEMA, add_prefix_for_prod
from datetime import datetime

class Review(db.Model):
    __tablename__ = "reviews"

    if environment == "production":
        __table_args__ = {"schema": SCHEMA}

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod("users.id")), nullable=False)
    experience_id = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod("experiences.id")), nullable=False)
    rating = db.Column(db.Integer, nullable=False)
    review = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    user = db.relationship("User", back_populates="reviews")
    experience = db.relationship("Experience", back_populates="reviews")

    def to_dict(self):
     return {
        "id": self.id,
        "user_id": self.user_id,
        "experience_id": self.experience_id,
        "rating": self.rating,
        "review": self.review,
        "created_at": self.created_at.isoformat(),
        "user": {
            "id": self.user.id,
            "username": self.user.username
        }
    }
