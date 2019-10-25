from flask import Blueprint, jsonify, request
from sqlalchemy import func, insert
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

@names_api.route('/name', methods=['POST'])
def add_name():
    # new_name = Name(AnimalName = request.json["AnimalName"], Sex = request.json["Sex"])
    i = insert(Name).values(AnimalName = request.json["AnimalName"], Sex = request.json["Sex"])
    db.engine.execute(i)
    # new_name = Name()
    # new_name.AnimalName = request.json["AnimalName"]
    # new_name.Sex = request.json["Sex"]
    # db.session.add(new_name)
    # db.session.commit()
    return jsonify(success=True)
