from app import db
from enum import Enum
from sqlalchemy import Enum as SQLEnum
from sqlalchemy import Text

class CommentStatus(Enum):
    HIDDEN = "hidden"
    DELETED = "deleted"
    FIXED = "fixed"

class Comment(db.Model):
    __tablename__ = "comments"

    id = db.Column(db.Integer, primary_key=True)
    date_time = db.Column(db.DateTime, nullable=False)
    likes = db.Column(db.Integer, nullable=False, default=0)
    content = db.Column(Text, nullable=False)
    status = db.Column(SQLEnum(CommentStatus))

    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    post_id = db.Column(db.Integer, db.ForeignKey("posts.id"), nullable=False)