from flask import Blueprint, jsonify, request, abort
from flask import current_app as app
from werkzeug.exceptions import BadRequest

chatBP = Blueprint(
    'chatBP', __name__
)

messages_dB = []


@chatBP.route('/users/messages/', methods=['POST'])
def sendMessage():
    try:
        jsonfile = request.get_json(silent=False, force=False)
    except BadRequest:
        abort(400, "Bad jsonfile")
    messages_dB.append(jsonfile)
    return


@chatBP.route('/users/messages/', methods=['GET'])
def getMessage():
    return
