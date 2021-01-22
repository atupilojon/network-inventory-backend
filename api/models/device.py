from sqlalchemy.dialects.mysql import BIGINT
from sqlalchemy import ForeignKeyConstraint

from api.models import db


class Device(db.Model):
    __tablename__ = 'devices'
    name_device = db.Column(db.String(25), primary_key=True)
    vendor_device = db.Column(db.String(25), db.ForeignKey('vendors.name_vendor'), nullable=False)
    ipaddr_device = db.Column(BIGINT(10, unsigned=True), db.ForeignKey('ipaddress.number_ip'))
    location_row_device = db.Column(db.Integer)
    location_rack_device = db.Column(db.Integer)
    __table_args__ = (
        ForeignKeyConstraint(
            ['location_row_device', 'location_rack_device'],
            ['locations.row_position', 'locations.rack_position']
        ),
    )

    def __repr__(self):
        return f'Device: {self.name_device}'


class Vendor(db.Model):
    __tablename__ = 'vendors'
    name_vendor = db.Column(db.String(25), primary_key=True)
    model_vendor = db.relationship('Model', backref='vendors')
    device_vendor = db.relationship('Device', backref='vendors')


class Model(db.Model):
    __tablename__ = 'models'
    name_model = db.Column(db.String(25), primary_key=True)
    os_model = db.Column(db.String(25))
    vendor_model = db.Column(db.String(25), db.ForeignKey('vendors.name_vendor'), nullable=False)
