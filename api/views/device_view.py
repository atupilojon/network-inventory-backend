from flask import Blueprint, make_response, Response, jsonify

device = Blueprint('device', __name__)


@device.route('/device', methods=['GET'])
def get_devices() -> Response:
    return make_response(jsonify({'getting': True}), 200)


@device.route('/device/create', methods=['POST'])
def create_device() -> Response:
    return make_response(jsonify({'created': True}), 200)
