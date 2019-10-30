from flask import Blueprint, jsonify, request, session
from sqlalchemy_db_instance import db
from models import Favorite

favorites_api = Blueprint('favorites_api', __name__)

@favorites_api.route('/favorite-name', methods=["POST", "GET"])
def add_favorite():
    new_fav = Favorite()
    new_fav.user_username = session['user']
    new_fav.name_id = request.json["name_id"]
    new_fav.favorited_name = request.json["favorited_name"]
    new_fav.name_gender = request.json["name_gender"]
    db.session.add(new_fav)
    db.session.commit()
    return jsonify(success = True)

@favorites_api.route('/favorited-names', methods=['GET'])
def serve_favorited_names():
    username = session['user']
    favorite_instances = db.session.query(Favorite).filter(Favorite.user_username == username).all()
    favorite_results = [{"id": favorite.id, "user_username": favorite.user_username, "name_id": favorite.name_id, "favorited_name": favorite.favorited_name, "name_gender": favorite.name_gender} for favorite in favorite_instances]
    return jsonify({"favorites": favorite_results})