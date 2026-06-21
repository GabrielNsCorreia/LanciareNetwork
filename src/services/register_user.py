from models.user import User
from services.generate_hash import generate_hash

def register_user(name, username, email, password) -> User:
    
    hash_password = generate_hash(password)

    new_user = User(name = name, username = username, email = email, password = hash_password)
    return 