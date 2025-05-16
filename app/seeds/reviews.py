from app.models import db, Review
from datetime import datetime
import random

def seed_reviews():
    reviews = [
        Review(user_id=2, experience_id=1, rating=5, review="Incredible views and not too crowded."),
        Review(user_id=3, experience_id=1, rating=4, review="Bring water! Great experience."),
        Review(user_id=1, experience_id=2, rating=5, review="Best food market I’ve ever visited."),
        Review(user_id=3, experience_id=3, rating=4, review="Relaxing and peaceful."),
        Review(user_id=2, experience_id=4, rating=4, review="Loved the street art. Cool neighborhood."),
        Review(user_id=1, experience_id=5, rating=3, review="Funny but small venue."),
        Review(user_id=3, experience_id=6, rating=5, review="Tacos were next-level. Worth it."),
        Review(user_id=2, experience_id=7, rating=5, review="The stars were unbelievable."),
        Review(user_id=1, experience_id=8, rating=4, review="Chilly morning but epic views."),
        Review(user_id=3, experience_id=9, rating=4, review="Lots of color, very inspiring."),
        Review(user_id=2, experience_id=10, rating=5, review="Perfect for photographers and travelers."),
    ]
    db.session.add_all(reviews)
    db.session.commit()

def undo_reviews():
    db.session.execute("DELETE FROM reviews")
    db.session.commit()
