from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, HiddenField
from wtforms.validators import DataRequired

class CreateCategoryForm(FlaskForm):
    name = StringField("Category Title", validators=[DataRequired()])
    submit = SubmitField("Submit")
    
class CreateProjectForm(FlaskForm):
    name = StringField("Project Title", validators=[DataRequired()])
    category_id = HiddenField('Category ID', validators=[DataRequired()])
    submit = SubmitField("Submit")
    
class CreateTaskForm(FlaskForm):
    name = StringField("Task", validators=[DataRequired()])
    submit = SubmitField("Submit")