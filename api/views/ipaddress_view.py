from ipaddress import AddressValueError
from flask import Blueprint, make_response, request, Response, jsonify
import json
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm.exc import UnmappedInstanceError
from ..dao.dao_ipaddress import add_ipaddr, del_ipaddr, get_ipaddr

ipaddr = Blueprint('ipaddr', __name__)


@ipaddr.route('/api/v1/ipaddr', methods=['POST', 'GET', 'DELETE'])
def load_ipaddr() -> Response:
    if request.method == 'POST':
        body_request = request.get_data()
        try:
            add_ipaddr(json.loads(body_request))
            return make_response({'message': 'IP address added'}, 201)
        except Exception as exc:
            return handle_exceptions(exc)

    if request.method == 'DELETE':
        body_request = request.args.get('ip')
        try:
            del_ipaddr(body_request)
            return make_response({'message': 'IP address deleted'}, 200)
        except Exception as exc:
            return handle_exceptions(exc)

    if request.method == 'GET':
        body_request = request.args.get('ip')
        try:
            found_ip = get_ipaddr(body_request)
            return make_response(found_ip, 200)
        except Exception as exc:
            return handle_exceptions(exc)


def handle_exceptions(exc: Exception) -> Response:
    try:
        raise exc
    except KeyError:
        return make_response({'message': 'Bad body'}, 400)
    except IntegrityError:
        return make_response({'message': 'IP already exists in database'}, 400)
    except UnmappedInstanceError:
        return make_response({'message': 'IP do not exists in database'}, 400)
    except AddressValueError:
        return make_response({'message': 'Bad IP format'}, 400)
    except AttributeError:
        return make_response({'message': 'IP do not exists in database'}, 400)

