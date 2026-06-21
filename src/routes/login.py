from flask import Blueprint

login_bp = Blueprint("login", __name__)

@login_bp.route("/login", methods=["POST", "GET"])
def login():
    return True