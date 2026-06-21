from app import db
from datetime import datetime

class Follow(db.Model):
    __tablename__ = "follows"

    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    follower_id = db.Column(
        db.Integer,
        db.ForeignKey("users.id"),
        primary_key=True
    )

    following_id = db.Column(
        db.Integer,
        db.ForeignKey("users.id"),
        primary_key=True
    )
