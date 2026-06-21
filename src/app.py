from flask import Flask

from database.base import db
from config import DATABASE_URL

from routes.sign_up import sign_up_bp

def create_app():

    app = Flask(__name__)

    app.config["SQLALCHEMY_DATABASE_URI"] = DATABASE_URL
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.init_app(app)

    app.register_blueprint(sign_up_bp)

    return app