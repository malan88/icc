from flask import Blueprint

requests = Blueprint("requests", __name__, url_prefix="/request",
        template_folder="templates")

from app.requests import routes, forms