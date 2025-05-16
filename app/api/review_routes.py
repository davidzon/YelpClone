from flask import Blueprint, request
from flask_login import login_required, current_user
from app.models import db, Review
from app.forms.review_form import ReviewForm

review_routes = Blueprint("reviews", __name__)

@review_routes.route("/", methods=["POST"])
@login_required
def create_review():
    form = ReviewForm()
    form["csrf_token"].data = request.cookies["csrf_token"]

    if form.validate_on_submit():
        review = Review(
            user_id=current_user.id,
            experience_id=form.experience_id.data,
            rating=form.rating.data,
            review=form.review.data
        )
        db.session.add(review)
        db.session.commit()
        return review.to_dict()
    return {"errors": form.errors}, 400

@review_routes.route("/<int:id>", methods=["PUT"])
@login_required
def update_review(id):
    review = Review.query.get_or_404(id)
    if review.user_id != current_user.id:
        return {"error": "Unauthorized"}, 403

    form = ReviewForm()
    form["csrf_token"].data = request.cookies["csrf_token"]
    if form.validate_on_submit():
        review.rating = form.rating.data
        review.review = form.review.data
        db.session.commit()
        return review.to_dict()
    return {"errors": form.errors}, 400

@review_routes.route("/<int:id>", methods=["DELETE"])
@login_required
def delete_review(id):
    review = Review.query.get_or_404(id)
    if review.user_id != current_user.id:
        return {"error": "Unauthorized"}, 403
    db.session.delete(review)
    db.session.commit()
    return {"message": "Review deleted"}
