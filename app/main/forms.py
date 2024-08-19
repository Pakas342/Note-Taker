from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, URL

class CreateCategory(FlaskForm):
    name = StringField("Category Title", validators=[DataRequired()])
    submit = SubmitField("Submit Post")