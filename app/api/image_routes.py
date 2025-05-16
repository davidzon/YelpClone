from flask import Blueprint, request
from flask_login import login_required, current_user
from app.models import db, Image
from app.forms.image_form import ImageForm

image_routes = Blueprint("images", __name__)

@image_routes.route("/", methods=["POST"])
@login_required
def upload_image():
    form = ImageForm()
    form["csrf_token"].data = request.cookies["csrf_token"]

    if form.validate_on_submit():
        image = Image(
            experience_id=form.experience_id.data,
            user_id=current_user.id,
            url=form.url.data,
            caption=form.caption.data
        )
        db.session.add(image)
        db.session.commit()
        return image.to_dict()
    return {"errors": form.errors}, 400

@image_routes.route("/<int:id>", methods=["DELETE"])
@login_required
def delete_image(id):
    image = Image.query.get_or_404(id)
    if image.user_id != current_user.id:
        return {"error": "Unauthorized"}, 403
    db.session.delete(image)
    db.session.commit()
    return {"message": "Image deleted"}
