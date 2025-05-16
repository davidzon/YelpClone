from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField
from wtforms.validators import DataRequired, URL

class ImageForm(FlaskForm):
    experience_id = IntegerField("Experience ID", validators=[DataRequired()])
    url = StringField("Image URL", validators=[DataRequired(), URL()])
    caption = StringField("Caption")
