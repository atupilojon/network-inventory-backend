from api.models import db


class Location(db.Model):
    __tablename__ = 'locations'
    row_position = db.Column(db.Integer, primary_key=True)
    rack_position = db.Column(db.Integer, primary_key=True)
    device_position = db.relationship('Device', backref='locations')

    def __repr__(self):
        return f'Row: {self.row_position} Rack: {self.rack_position}'
