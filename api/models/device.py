from api.models import db
from sqlalchemy.dialects.mysql import BIGINT


class Device(db.Model):
    __tablename__ = 'devices'
    name_device = db.Column(db.String(25), primary_key=True)

    def __repr__(self):
        return f'Device: {self.name_device}'


class Vendor(db.Model):
    __tablename__ = 'vendors'
    name_vendor = db.Column(db.String(25), primary_key=True)
    model_vendor = db.Column(db.String(25), db.ForeignKey('models.name_model'), nullable=False)


class Model(db.Model):
    __tablename__ = 'models'
    name_model = db.Column(db.String(25), primary_key=True)
    os_model = db.Column(db.String(25))
    vendor = db.relationship('Vendor', backref='models')
