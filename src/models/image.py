from app import db
from enum import Enum
from sqlalchemy import Enum as SQLEnum

class ImageType(Enum):
    PNG = "png"
    JPEG = "jpeg"

class Image(db.Model):
    __tablename__ = "images"

    id = db.Column(db.Integer, primary_key=True)
    public_id = db.Column(db.String(255), nullable=False)
    type = db.Column(SQLEnum(ImageType), nullable=False)
    name = db.Column(db.String(255), nullable=False)
    size = db.Column(db.Float, nullable=False)
    width = db.Column(db.Integer, nullable=False)
    height = db.Column(db.Integer, nullable=False)

    post_id = db.Column(db.Integer, db.ForeignKey("posts.id"))