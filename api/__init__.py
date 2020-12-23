from flask import Flask


def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('../config.py')
    with app.app_context():
        from .views.main_view import mainIndex
        from .views.device_view import device
        app.register_blueprint(mainIndex)
        app.register_blueprint(device)
        from .models import db, device
        db.init_app(app)
        db.create_all()
        return app
