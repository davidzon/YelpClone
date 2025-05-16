from .db import db, environment, SCHEMA, add_prefix_for_prod
from datetime import datetime

class Image(db.Model):
    __tablename__ = "images"

    if environment == "production":
        __table_args__ = {'schema': SCHEMA}

    id = db.Column(db.Integer, primary_key=True)
    experience_id = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod("experiences.id")), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod("users.id")), nullable=False)
    url = db.Column(db.String(255), nullable=False)
    caption = db.Column(db.String(255), nullable=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    experience = db.relationship("Experience", back_populates="images")
    user = db.relationship("User", back_populates="images")

    def to_dict(self):
        return {
            "id": self.id,
            "experience_id": self.experience_id,
            "user_id": self.user_id,
            "url": self.url,
            "caption": self.caption,
            "created_at": self.created_at.isoformat()
        }
