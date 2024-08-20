from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, HiddenField
from wtforms.validators import DataRequired

class CreateCategoryForm(FlaskForm):
    form_name = HiddenField('form_name', default='category_form')
    name = StringField("Category Title", validators=[DataRequired()])
    submit = SubmitField("Submit")
    
class CreateProjectForm(FlaskForm):
    form_name = HiddenField('form_name', default='project_form')
    name = StringField("Project Title", validators=[DataRequired()])
    category_id = HiddenField('Category ID', validators=[DataRequired()])
    due_date = StringField('Due Date', validators=[DataRequired()])
    submit = SubmitField("Submit")
    
class CreateTaskForm(FlaskForm):
    form_name = HiddenField('form_name', default='task_form')
    name = StringField("Task Name", validators=[DataRequired()])
    project_id = HiddenField('Project ID', validators=[DataRequired()])
    submit = SubmitField("Submit")