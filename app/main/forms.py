from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, URL

class CreateCategoryForm(FlaskForm):
    name = StringField("Category Title", validators=[DataRequired()])
    submit = SubmitField("Submit")
    
class CreateProjectForm(FlaskForm):
    name = StringField("Project Title", validators=[DataRequired()])
    category = 
    submit = SubmitField("Submit")
    
class CreateTaskForm(FlaskForm):
    name = StringField("Task", validators=[DataRequired()])
    submit = SubmitField("Submit")