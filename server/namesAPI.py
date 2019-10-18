from flask import Blueprint, jsonify, request

names = [{"id": 0, "name": "Nap Time All-Star", "gender": "GN" }]

names_api = Blueprint('names_api', __name__)

@names_api.route('/names', methods=['GET'])
def serve_all_names():
    return jsonify({"results": names})

@names_api.route('/name', methods=["POST"])
def add_name():
    names.append({"name": request.json["item"], "id": 0, "gender": "GN"})
    print(names)
    return jsonify(success = True)