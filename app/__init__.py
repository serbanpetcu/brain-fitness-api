from flask import Flask
from flask_migrate import Migrate

from .extensions import configuration, ma, mail
from .extensions import db
from .extensions import session

from app.http.api import api as api_blueprint

def create_app():
    main_app = Flask(__name__, static_folder="public")

    with main_app.app_context():

        # Load configuration variables
        main_app.config.from_object(configuration)

        # Models
        import app.models.user
        import app.models.lesson
        import app.models.card

        # Database
        db.init_app(main_app)

        # Migrate app+db
        Migrate(main_app, db)

        # Blueprints
        main_app.register_blueprint(api_blueprint)

        # Session
        session.init_app(main_app)

        # Marshmallow
        ma.init_app(main_app)

        # Mail
        mail.init_app(main_app)

        return main_app