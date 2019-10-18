from flask import Blueprint, jsonify, request

names = ['Nap Time All-Star', "Phil", "Theresa"]

names_api = Blueprint('names_api', __name__)

@names_api.route('/names', methods=['GET'])
def serve_all_names():
    return jsonify({"results": names})

@names_api.route('/name', methods=["POST"])
def add_name():
    names.append(request.json["item"])
    print(names)
    return jsonify(success = True)