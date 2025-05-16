from flask_wtf import FlaskForm
from wtforms import StringField, FloatField
from wtforms.validators import DataRequired, Length

class ExperienceForm(FlaskForm):
    title = StringField("Title", validators=[DataRequired(), Length(max=100)])
    description = StringField("Description", validators=[DataRequired()])
    location = StringField("Location", validators=[DataRequired()])
    category = StringField("Category", validators=[DataRequired()])
    price = FloatField("Price")
