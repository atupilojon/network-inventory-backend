from api.models import db


class Location(db.Model):
    __table_name__ = 'location'
    row_position = db.Column(db.Integer, primary_key=True)
    rack_position = db.Column(db.Integer, primary_key=True)

    def __repr__(self):
        return f'Row: {self.row_position} Rack: {self.rack_position}'
