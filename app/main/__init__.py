from flask import Blueprint
from app.main import forms

bp = Blueprint("main", __name__)

from app.main import routes