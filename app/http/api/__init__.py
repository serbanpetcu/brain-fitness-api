from flask import Blueprint

# API (v1)
api = Blueprint("api", __name__, template_folder="templates", url_prefix="/api/v1")
