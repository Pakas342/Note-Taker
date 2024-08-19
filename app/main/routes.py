from app.main import bp
from app.main.forms import CreateCategoryForm, CreateTaskForm, CreateProjectForm
from flask import render_template, url_for, redirect
from app.services import get_all_categories, add_category, add_task, add_project

@bp.route("/", methods=['GET', 'POST'])
def index():
    category_form = CreateCategoryForm()
    project_form = CreateProjectForm()
    task_form = CreateTaskForm()
    
    if category_form.validate_on_submit():
        print("Category From Triggered")
        add_category(category_form)
        return redirect(url_for('main.index'))
    
    if project_form.validate_on_submit():
        print("Category From Triggered")
        add_project(project_form)
        return redirect(url_for('main.index'))
    
    if task_form.validate_on_submit():
        print("Category From Triggered")
        add_task(task_form)
        return redirect(url_for('main.index'))
    
    return render_template("home.html", all_categories=get_all_categories(), category_form=category_form, project_form=project_form, task_form=task_form)