from app import db
from datetime import datetime
from enum import Enum
from sqlalchemy import Enum as SQLEnum

class MessageStatus(Enum):
    SENDED = "sended"
    RECEIVED = "received"
    DELETED = "deleted"

class Message(db.Model):
    __tablename__ = "messages"

    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(500), nullable=False)
    time_send = db.Column(db.DateTime, nullable=False)
    status = db.Column(
        SQLEnum(MessageStatus),
        default=MessageStatus.SENDED,
        nullable=False
    )

    sender_id = db.Column(
        db.Integer,
        db.ForeignKey("users.id"),
        nullable=False
    )

    recipient_id = db.Column(
        db.Integer,
        db.ForeignKey("users.id"),
        nullable=False
    )