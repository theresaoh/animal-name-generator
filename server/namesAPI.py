from flask import Blueprint, jsonify, request
from sqlalchemy import func, insert
from sqlalchemy_db_instance import db
from models import Name
import pandas as pd

names_api = Blueprint('names_api', __name__)

@names_api.route('/duplicate-name-test', methods=["POST"])
def test_duplicate_name():
    name = request.json["name"]
    gender = request.json["gender"]
    name_in_db = db.session.query(Name).filter(Name.name == name).filter(Name.gender == gender).all()
    # query any instances of names in the database that match the name and gender provided by user
    name_in_db_results = [{"id": name.id, "name": name.name, "gender": name.gender} for name in name_in_db]
    # if there are any names in the database, they will be returned 
    # otherwise, an empty array will be returned
    return jsonify({"does_the_name_exist": name_in_db_results})

@names_api.route('/male-names', methods=['GET'])
def serve_male_names():
    # serve 10 random male names to an API endpoint
    name_instances = db.session.query(Name).filter(Name.gender == "M").order_by(func.random()).limit(10)
    name_results = [{"id": name.id, "name": name.name, "gender": name.gender} for name in name_instances]
    return jsonify({"name": name_results})

@names_api.route('/female-names', methods=['GET'])
def serve_female_names():
    # serve 10 random female names to an API endpoint
    name_instances = db.session.query(Name).filter(Name.gender == "F").order_by(func.random()).limit(10)
    name_results = [{"id": name.id, "name": name.name, "gender": name.gender} for name in name_instances]
    return jsonify({"name": name_results})

@names_api.route('/gender-neutral-names', methods=['GET'])
def serve_gender_neutral_names():
    # serve 10 random gender-neutral names to an API endpoint
    name_instances = db.session.query(Name).filter(Name.gender == "GN").order_by(func.random()).limit(10)
    name_results = [{"id": name.id, "name": name.name, "gender": name.gender} for name in name_instances]
    return jsonify({"name": name_results})

@names_api.route('/name', methods=['POST'])
def add_name():
    # add a name to the DB
    new_name = Name()
    new_name.id = determine_next_id()
    new_name.name = request.json["name"]
    new_name.gender = request.json["gender"]
    db.session.add(new_name)
    db.session.commit()
    return jsonify(success=True)

def determine_next_id():
    # to account for an issue with added names not being assigned an auto-incrementing id
    # this function determines the max id currently in the Names table, adds one, and returns that number
    # this id is then referenced in the add_name function so that all added names have proper ids
    max_id = db.session.query(func.max(Name.id)).scalar()
    result = max_id + 1
    return result
