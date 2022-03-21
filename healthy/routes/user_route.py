from flask import Blueprint, jsonify, abort
from flask import current_app as app

# Temporary list of users, will be replaced later with a database .
userlist = {
    'Tony': ['admin', 'doctor', 'nurse']
}

userBP = Blueprint(
    'userBP', __name__
)


@userBP.route('/users/<string:uID>', methods=['POST'])
def addUser(uID):
    """
    Add a user

    Specify the role of the user

    """
    u = {uID: ""}
    userlist.update(u)
    return f'<p> {uID} Added <p>'


@userBP.route('/users/<string:uID>', methods=['DELETE'])
def removeUser(uID):
    try:
        del userlist[uID]
        app.logger.info(f'{uID} added.')
    except KeyError:
        app.logger.error(f'User {uID} not found')
        abort(400)
    return 0


@userBP.route('/userlist', methods=['GET'])
def listUsers():
    """
    Returns a json file with all the users listed.
    """
    users = []
    for user in userlist.keys():
        users.append(user)

    return jsonify({"users": users}), 200


@userBP.route('/userinfo/<string:uID>', methods=['GET'])
def showUserRoles(uID):
    """
    Returns the roles of a user. For example admin, doctor, nurse
    """
    if uID not in userlist.keys():
        abort(400, f'Could not find user {uID} in system ')
    else:
        return jsonify({"roles": userlist[uID]}), 200

