from flask import Flask


def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('../config.py')
    with app.app_context():
        from .views.test_view import test
        from .views.device_view import device
        from .views.ipaddress_view import ipaddr
        app.register_blueprint(test)
        app.register_blueprint(device)
        app.register_blueprint(ipaddr)
        from .models import db, device, ipaddr, location
        db.init_app(app)
        db.create_all()
        return app
