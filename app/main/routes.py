from app.main import bp
from flask import render_template
from app.services import get_all_projects

@bp.route("/")
def index():
    return render_template("home.html", all_projects=get_all_projects())