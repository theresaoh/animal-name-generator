from flask import Blueprint, jsonify, request
from sqlalchemy import func
from sqlalchemy_db_instance import db
from models import Name
import pandas as pd

names = [{"id": 0, "name": "Nap Time All-Star", "gender": "GN" }]

names_api = Blueprint('names_api', __name__)

@names_api.route('/names', methods=['GET'])
def serve_all_names():
    name_instances = db.session.query(Name).all()
    name_results = [{"id": name.id, "name": name.AnimalName, "gender": name.Sex} for name in name_instances]
    return jsonify({"name": name_results})

@names_api.route('/male-names', methods=['GET'])
def serve_male_names():
    name_instances = db.session.query(Name).filter(Name.Sex == "M").order_by(func.random()).limit(10)
    name_results = [{"id": name.id, "name": name.AnimalName, "gender": name.Sex} for name in name_instances]
    return jsonify({"name": name_results})

@names_api.route('/female-names', methods=['GET'])
def serve_female_names():
    name_instances = db.session.query(Name).filter(Name.Sex == "F").order_by(func.random()).limit(10)
    name_results = [{"id": name.id, "name": name.AnimalName, "gender": name.Sex} for name in name_instances]
    return jsonify({"name": name_results})

@names_api.route('/gender-neutral-names', methods=['GET'])
def serve_gender_neutral_names():
    name_instances = db.session.query(Name).filter(Name.Sex == "GN").order_by(func.random()).limit(10)
    name_results = [{"id": name.id, "name": name.AnimalName, "gender": name.Sex} for name in name_instances]
    return jsonify({"name": name_results})

@names_api.route('/name', methods=["POST"])
def add_name():
    names.append({"name": request.json["item"], "id": 0, "gender": "GN"})
    print(names)
    return jsonify(success = True)