from werkzeug.security import generate_password_hash

def generate_hash(text) -> str:
    return generate_password_hash(text)
