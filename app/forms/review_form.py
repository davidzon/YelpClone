from flask_wtf import FlaskForm
from wtforms import IntegerField, StringField
from wtforms.validators import DataRequired

class ReviewForm(FlaskForm):
    experience_id = IntegerField("Experience ID", validators=[DataRequired()])
    rating = IntegerField("Rating", validators=[DataRequired()])
    review = StringField("Review", validators=[DataRequired()])
