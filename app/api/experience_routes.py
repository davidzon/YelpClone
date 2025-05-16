from flask import Blueprint, request, jsonify
from flask_login import login_required, current_user
from app.models import db, Experience
from app.forms.experience_form import ExperienceForm

experience_routes = Blueprint("experiences", __name__)

@experience_routes.route("/")
def all_experiences():
    name = request.args.get("name", "")
    category = request.args.get("category", "")
    min_price = request.args.get("minPrice", type=float, default=0)
    max_price = request.args.get("maxPrice", type=float, default=float('inf'))

    query = Experience.query
    if name:
        query = query.filter(Experience.title.ilike(f"%{name}%"))
    if category:
        query = query.filter(Experience.category.ilike(f"%{category}%"))
    query = query.filter(Experience.price >= min_price, Experience.price <= max_price)

    return {"experiences": [exp.to_dict() for exp in query.all()]}

@experience_routes.route("/<int:id>")
def single_experience(id):
    exp = Experience.query.get_or_404(id)
    return exp.to_dict()

@experience_routes.route("/", methods=["POST"])
@login_required
def create_experience():
    form = ExperienceForm()
    form["csrf_token"].data = request.cookies["csrf_token"]

    if form.validate_on_submit():
        exp = Experience(
            creator_id=current_user.id,
            title=form.title.data,
            description=form.description.data,
            location=form.location.data,
            category=form.category.data,
            price=form.price.data
        )
        db.session.add(exp)
        db.session.commit()
        return exp.to_dict()
    return {"errors": form.errors}, 400

@experience_routes.route("/<int:id>", methods=["PUT"])
@login_required
def update_experience(id):
    exp = Experience.query.get_or_404(id)
    if exp.creator_id != current_user.id:
        return {"error": "Unauthorized"}, 403

    form = ExperienceForm()
    form["csrf_token"].data = request.cookies["csrf_token"]

    if form.validate_on_submit():
        exp.title = form.title.data
        exp.description = form.description.data
        exp.location = form.location.data
        exp.category = form.category.data
        exp.price = form.price.data
        db.session.commit()
        return exp.to_dict()
    return {"errors": form.errors}, 400

@experience_routes.route("/<int:id>", methods=["DELETE"])
@login_required
def delete_experience(id):
    exp = Experience.query.get_or_404(id)
    if exp.creator_id != current_user.id:
        return {"error": "Unauthorized"}, 403
    db.session.delete(exp)
    db.session.commit()
    return {"message": "Experience deleted"}
