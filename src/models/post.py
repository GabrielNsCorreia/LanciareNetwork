from app import db
from datetime import datetime
from enum import Enum
from sqlalchemy import Enum as SQLEnum
from geoalchemy2 import Geometry

class PostStatus(Enum):
    POSTED = "posted"
    DELETED = "deleted"
    HIDDEN = "hidden"
    FIXED = "fixed"

class Post(db.Model):
    __tablename__ = "posts"

    id = db.Column(db.Integer, primary_key=True)
    likes = db.Column(db.Integer, nullable=False, default=0)
    comments_acount = db.Column(db.Integer, nullable=False, default=0)

    status = db.Column(
        SQLEnum(PostStatus),
        default=PostStatus.POSTED,
        nullable=False
    )

    date_time = db.Column(db.DateTime, nullable=False)

    location = db.Column(
        Geometry(geometry_type="POINT", srid=4326)
    )

    user_id = db.Column(
        db.Integer,
        db.ForeignKey("users.id"),
        nullable=False
    )
