from flask import Blueprint, make_response, Response, jsonify

mainIndex = Blueprint('mainIndex', __name__)


@mainIndex.route('/')
def index() -> Response:
    return make_response(jsonify({'connected': True}), 200)
