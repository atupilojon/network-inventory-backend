from api.models import db
from api.models.ipaddr import IPAddress, int_ip, str_ipaddr


def add_ipaddr(request):
    ipaddr = request['ipaddress']
    new_ipaddr = IPAddress(
        ipaddr['number'],
        ipaddr['mask'],
        ipaddr['type']
    )
    db.session.add(new_ipaddr)
    db.session.commit()


def delete_all_ipaddr():
    IPAddress.query.delete()


def del_ipaddr(some_ip):
    ip = int_ip(some_ip)
    stored_ipaddr = IPAddress.query.filter_by(number_ip=ip).first()
    db.session.delete(stored_ipaddr)
    db.session.commit()


def get_ipaddr(some_ip):
    ip = int_ip(some_ip)
    got_ip = IPAddress.query.filter_by(number_ip=ip).first()
    message = {'ipaddress': {'number': str_ipaddr(got_ip.number_ip),
                             'mask': got_ip.mask_ip,
                             'type': got_ip.type_ip}}
    return message
