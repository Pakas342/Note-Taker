from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, HiddenField
from wtforms.validators import DataRequired
from flask_ckeditor import CKEditorField

class CreateCategoryForm(FlaskForm):
    form_name = HiddenField('form_name', default='category_form')
    name = StringField("Category Title", validators=[DataRequired()])
    submit = SubmitField("Submit")
    
class CreateProjectForm(FlaskForm):
    form_name = HiddenField('form_name', default='project_form')
    name = StringField("Project Title", validators=[DataRequired()])
    category_id = HiddenField('Category ID', validators=[DataRequired()])
    due_date = StringField('Due Date')
    submit = SubmitField("Submit")
    
class CreateTaskForm(FlaskForm):
    form_name = HiddenField('form_name', default='task_form')
    name = StringField("Task Name", validators=[DataRequired()])
    content = CKEditorField("Task Content")
    project_id = HiddenField('Project ID', validators=[DataRequired()])
    due_date = StringField('Due Date')
    submit = SubmitField("Submit")