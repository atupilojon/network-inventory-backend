from flask import Flask


def create_app():
    app = Flask(__name__)

    with app.app_context():
        from .views.main_view import mainIndex
        app.register_blueprint(mainIndex)
        return app
