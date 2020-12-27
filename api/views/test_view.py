from flask import Blueprint, make_response, Response, jsonify

test = Blueprint('test_connectivity', __name__)


@test.route('/api/v1/test')
def index() -> Response:
    return make_response(jsonify({'connected': True}), 200)
