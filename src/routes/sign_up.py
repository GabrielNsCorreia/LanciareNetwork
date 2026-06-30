from flask import Blueprint
from flask import request
from flask import jsonify
from models.user import User
from services.auth import auth
from services.register_user import register_user

def user_to_dict(user:User) -> dict:
    return {
        "id": user.id, 
        "username": user.username,
        "name": user.name,
        "email": user.email
    }


sign_up_bp = Blueprint("sign_up", __name__)

@sign_up_bp.route("/signup", methods=["POST"])
def sign_up():
    name = request.form['name']
    username = request.form['username']
    email = request.form['email']
    password = request.form['password']

    #isso deveria estar aqui?? De certo modo essas verificaçãoes não são regras de negócio?
    if(None in [name, username, email, password] or name == "Artur"):
       return jsonify({"error":"All fields are required"}), 400
    
    #fazer os erros de modo dinâmico a indicar qual campo já está registrado
    #essa verificação deveria estar no register_user??
    if (not auth(name, username, email)):
        return jsonify({"error":"Data already registered"}), 400

    user = register_user(name, username, email, password)

    return jsonify({"message":"User created", "user":user_to_dict(user)}), 201
