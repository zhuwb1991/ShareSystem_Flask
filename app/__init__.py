from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import config


db = SQLAlchemy()


def create_app(config_name):

    app = Flask(__name__)
    app.config.from_object(config[config_name])

    config[config_name].init_app(app)
    db.init_app(app)

    from .main import main as main_bp
    from .people import people as people_bp
    from .article import article as article_bp
    from .comment import comment as comment_bp

    app.register_blueprint(main_bp)
    app.register_blueprint(people_bp)
    app.register_blueprint(article_bp)
    app.register_blueprint(comment_bp)

    return app
