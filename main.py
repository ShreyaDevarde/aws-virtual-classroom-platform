"""
AWS Hosted Virtual Classroom Platform

Application Entry Point
"""

from flask import Flask
from config import Config

from routes.auth_routes import auth_bp
from routes.content_routes import content_bp


def create_app():

    app = Flask(__name__)

    app.config.from_object(Config)

    app.register_blueprint(auth_bp)
    app.register_blueprint(content_bp)

    return app


app = create_app()


if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=5000,
        debug=True
    )