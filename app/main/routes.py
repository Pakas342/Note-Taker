from app.main import bp
from app.main.forms import CreateCategoryForm, CreateTaskForm, CreateProjectForm
from flask import render_template, url_for, redirect, request
from app.services import get_all_categories, add_category, add_task, add_project

@bp.route("/", methods=['GET', 'POST'])
def index():
    category_form = CreateCategoryForm()
    project_form = CreateProjectForm()
    task_form = CreateTaskForm()
    
    form_name = request.form.get("form_name")
    
    if form_name == "category_form" and category_form.validate_on_submit():
        add_category(category_form)
        return redirect(url_for('main.index'))
    
    if form_name == "project_form" and  project_form.validate_on_submit():
        add_project(project_form)
        return redirect(url_for('main.index'))
    
    if form_name == "task_form" and  task_form.validate_on_submit():
        add_task(task_form)
        return redirect(url_for('main.index'))
    
    return render_template("home.html", all_categories=get_all_categories(), category_form=category_form, project_form=project_form, task_form=task_form)