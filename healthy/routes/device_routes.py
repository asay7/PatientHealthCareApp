from flask import Blueprint, jsonify, request, abort
from flask import current_app as app
from werkzeug.exceptions import BadRequest

from ..models import device_model

deviceBP = Blueprint(
    'deviceBP', __name__
)

# change to dictionary to prevent any duplicate keys
deviceID_list = ['D000001', 'D000002', 'D000003']


@deviceBP.route('/devices/<string:devID>', methods=['POST'])
def addDevice(devID):
    """
    Register the device ID
    """
    if devID in deviceID_list:
        abort(400, f'{devID} Already registered')
    else:
        deviceID_list.append(devID)
        return jsonify({devID: "Registered"}), 200


@deviceBP.route('/devices/<string:devID>', methods=['DELETE'])
def removeDevice(devID):
    """
    Remove the specified device
    """
    if devID in deviceID_list:
        deviceID_list.remove(devID)
        return jsonify({devID: "Removed"}), 200
    else:
        abort(400, f'{devID} does not exist')
        return jsonify(), 200


@deviceBP.route('/devices', methods=['GET'])
def listDevices():
    """
    Lists all the devices currently registered
    """
    return jsonify({'devices': [devID for devID in deviceID_list]}), 200


@deviceBP.route('/devices/<devID>/data', methods=['POST'])
def uploadMeasurement(devID):
    # Check for proper cURL format
    # filetype = request.headers.get('Content-Type')
    # if filetype != 'application/json':
    #     abort(400, "Unsupported Content-Type specified")
    try:
        jsonfile = request.get_json(silent=False, force=False)
    except BadRequest:
        abort(400, "Bad jsonfile")

    device = device_model.DeviceModule()
    if not device.validFormat(jsonfile):
        abort(400, "JSON format is not supported")
    if not device.validMeasurement(jsonfile["MeasurementData"], jsonfile["DeviceType"]):
        abort(400, "Invalid measurement data")

    return jsonify(jsonfile), 200
