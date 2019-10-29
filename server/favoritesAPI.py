from flask import Blueprint, jsonify, request, session
from sqlalchemy_db_instance import db
from models import Favorite

favorites_api = Blueprint('favorites_api', __name__)

@favorites_api.route('/favorite-name', methods=["POST", "GET"])
def add_favorite():
    new_fav = Favorite()
    new_fav.user_username = request.json["username"]
    new_fav.name_id = request.json["name_id"]
    db.session.add(new_fav)
    db.session.commit()
    return jsonify(success = True)