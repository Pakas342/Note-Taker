from app import db
from app.models import Project

def get_all_projects():
    return db.session.execute(db.select(Project)).scalars().all()
