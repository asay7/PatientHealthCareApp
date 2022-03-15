from flask import Blueprint, jsonify
from flask import current_app as app

homeBP = Blueprint(
    'homeBP', __name__
)

user_list = ["Avdol", "Jotaro", "Polnarif", "Joseph", "Dio"]


@homeBP.route('/users', methods=['GET'])
def home():
    app.logger.info("Homepage Accessed")

    return jsonify({'users': [user for user in user_list]})


@homeBP.route('/users/<int:id>', methods=['GET'])
def userByID(id):
    return jsonify({'username': user_list[id]})


@homeBP.route('/users/<string:name>', methods=['POST'])
def addUsers(name):
    user_list.append(name)
    return jsonify({'message': f'new user {name} added'})
