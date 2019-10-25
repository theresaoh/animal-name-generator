from flask import Blueprint, jsonify, request
from sqlalchemy_db_instance import db
from models import User

users_api = Blueprint('users_api', __name__)

@users_api.route('/add-user', methods=["POST"])
def add_user():
    new_user = User()
    new_user.username = request.json["username"]
    new_user.password = request.json["password"]
    db.session.add(new_user)
    db.session.commit()
    return jsonify(success=True)

@users_api.route('/name', methods=["POST"])
def add_name():
    names.append({"name": request.json["item"], "id": 0, "gender": "GN"})
    print(names)
    return jsonify(success = True)