from api.models import db
from sqlalchemy.dialects.mysql import BIGINT, INTEGER
from ipaddress import IPv4Address


def int_ip(ipaddr: str) -> int:
    return int(IPv4Address(ipaddr))


def str_ipaddr(ipaddr: int) -> str:
    return str(IPv4Address(ipaddr))


class IPAddress(db.Model):
    __tablename__ = 'ipaddress'
    number_ip = db.Column(BIGINT(10, unsigned=True), primary_key=True)
    mask_ip = db.Column(INTEGER(2), nullable=False)
    type_ip = db.Column(db.String(20))

    def __repr__(self):
        return f'IP: {str_ipaddr(self.number_ip)}/{self.mask_ip} - {self.type_ip}'

    def __init__(self, number, mask, type):
        self.number_ip = int_ip(number)
        self.mask_ip = mask
        self.type_ip = type

