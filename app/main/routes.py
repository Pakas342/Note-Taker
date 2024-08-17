from main import bp
from flask import render_template
from services import database_services

@bp.route("/")
def index():
    return render_template("home.html", all_projects=database_services.get_all_projects())