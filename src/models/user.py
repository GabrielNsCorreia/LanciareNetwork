from app import db
from sqlalchemy import Text

class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)

    name = db.Column(db.String(30), nullable=False)
    username = db.Column(db.String(30), nullable=False, unique=True)

    email = db.Column(
        db.String(320),
        nullable=False,
        unique=True
    )

    password = db.Column(db.String(400), nullable=False)

    bio = db.Column(Text)

    posts_acount = db.Column(
        db.Integer,
        nullable=False,
        default=0
    )

    followers_acount = db.Column(
        db.Integer,
        nullable=False,
        default=0
    )

    following_acount = db.Column(
        db.Integer,
        nullable=False,
        default=0
    )

    image_id = db.Column(
        db.Integer,
        db.ForeignKey("images.id")
    )
