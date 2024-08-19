from app import db
from app.models import Project, Category, Task
from app.main.forms import CreateCategoryForm, CreateProjectForm, CreateTaskForm

def get_all_categories():
    return db.session.execute(db.select(Category).order_by(Category.name.asc())).scalars().all()

def add_category(new_category_form: CreateCategoryForm):
    new_category = Category(
        name=new_category_form.name.data
    )
    db.session.add(new_category)
    db.session.commit()
    
def add_project(new_project_form: CreateProjectForm):
    new_project = Project(
        name=new_project_form.name.data,
        category_id = new_project_form.category_id.data
    )
    db.session.add(new_project)
    db.session.commit()
    
def add_task(new_task_form: CreateTaskForm):
    new_task = Task(
        name=new_task_form.name.data,
        project_id = new_task_form.project_id.data
    )
    db.session.add(new_task)
    db.session.commit()