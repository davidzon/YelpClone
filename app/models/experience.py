from .db import db, environment, SCHEMA, add_prefix_for_prod
from datetime import datetime

class Experience(db.Model):
    __tablename__ = 'experiences'

    if environment == "production":
        __table_args__ = {'schema': SCHEMA}

    id = db.Column(db.Integer, primary_key=True)
    creator_id = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod("users.id")), nullable=False)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    location = db.Column(db.String(255), nullable=False)
    category = db.Column(db.String(50), nullable=False)
    price = db.Column(db.Float, nullable=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    creator = db.relationship("User", back_populates="experiences")
    reviews = db.relationship("Review", back_populates="experience", cascade="all, delete-orphan")
    images = db.relationship("Image", back_populates="experience", cascade="all, delete-orphan")

    def to_dict(self):
        return {
            "id": self.id,
            "creator_id": self.creator_id,
            "title": self.title,
            "description": self.description,
            "location": self.location,
            "category": self.category,
            "price": self.price,
            "created_at": self.created_at.isoformat(),
            "images": [img.to_dict() for img in self.images],
            "reviews": [review.to_dict() for review in self.reviews]
        }
