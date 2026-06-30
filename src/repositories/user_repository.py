from models.user import User
from typing import Optional
from sqlalchemy import select
from sqlalchemy import exists
from app import db

def get_user_by_name(name) -> Optional[User]:
    stmt = select(User).where(User.name == name)
    user = db.session.scalar(stmt)
    return user

def get_user_by_username(username) -> Optional[User]:
    stmt = select(User).where(User.username == username)
    user = db.session.scalar(stmt)
    return user

def get_user_by_email(email) -> Optional[User]:
    stmt = select(User).where(User.email == email)
    user = db.session.scalar(stmt)
    return user

def create_user(user) -> None:
    db.session.add(user)
    db.session.commit()
