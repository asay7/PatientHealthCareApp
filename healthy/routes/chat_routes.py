from flask import Blueprint, jsonify
from flask import current_app as app
import pymongo

chatBP = Blueprint(
    'chatBP', __name__
)


@chatBP.route('/users/messages/', methods=['POST'])
def sendMessage():

    return


@chatBP.route('/users/messages/', methods=['GET'])
def getMessage():
    return
