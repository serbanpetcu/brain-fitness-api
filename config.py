import os
import configparser


class Config(object):
    _SECTION_FLASK = "Flask"
    _SECTION_FLASK_SQLALCHEMY = "Flask-SQLAlchemy"
    _SECTION_FLASK_SESSION = "Flask-Session"
    _SECTION_FLASK_MAIL = "Flask-Mail"

    def __init__(self):
        BASE_DIR = os.path.abspath(os.path.dirname(__file__))
        CONFIG_FILE_PATH = os.path.join(BASE_DIR, "config.ini")
        config_parser = configparser.ConfigParser()
        config_parser.read(CONFIG_FILE_PATH)

        self.BASE_DIR = os.path.abspath(os.path.dirname(__file__))
        self.ENV = config_parser.get(self._SECTION_FLASK, "ENV")
        self.DEBUG = config_parser.getboolean(self._SECTION_FLASK, "DEBUG")
        self.SECRET_KEY = config_parser.get(self._SECTION_FLASK, "SECRET_KEY")
        self.SERVER_NAME = config_parser.get(self._SECTION_FLASK, "SERVER_NAME")
        self.TESTING = config_parser.getboolean(self._SECTION_FLASK, "TESTING")
        self.EXPIRATION = config_parser.getint(self._SECTION_FLASK, "EXPIRATION")

        # SQLALCHEMY SETTINGS
        self.SQLALCHEMY_DATABASE_URI = config_parser.get(
            self._SECTION_FLASK_SQLALCHEMY, "SQLALCHEMY_DATABASE_URI"
        )

        self.SQLALCHEMY_TRACK_MODIFICATIONS = config_parser.getboolean(
            self._SECTION_FLASK_SQLALCHEMY, "SQLALCHEMY_TRACK_MODIFICATIONS"
        )

        # SESSION
        self.SESSION_TYPE = config_parser.get(
            self._SECTION_FLASK_SESSION, "SESSION_TYPE"
        )
        self.SESSION_FILE_DIR = os.path.realpath(
            config_parser.get(self._SECTION_FLASK_SESSION, "SESSION_FILE_DIR")
        )
        self.SESSION_FILE_THRESHOLD = config_parser.getint(
            self._SECTION_FLASK_SESSION, "SESSION_FILE_THRESHOLD"
        )
        self.SESSION_COOKIE_NAME = config_parser.get(
            self._SECTION_FLASK_SESSION, "SESSION_COOKIE_NAME"
        )
        self.SESSION_PERMANENT = config_parser.getboolean(
            self._SECTION_FLASK_SESSION, "SESSION_PERMANENT"
        )
        self.PERMANENT_SESSION_LIFETIME = config_parser.getint(
            self._SECTION_FLASK_SESSION, "PERMANENT_SESSION_LIFETIME"
        )
        self.SESSION_REFRESH_EACH_REQUEST = config_parser.getboolean(
            self._SECTION_FLASK_SESSION, "SESSION_REFRESH_EACH_REQUEST"
        )
        # EMAIL SETTINGS
        self.EMAIL_SENDER = config_parser.get(self._SECTION_FLASK_MAIL, "EMAIL_SENDER")
        self.MAIL_SERVER = config_parser.get(self._SECTION_FLASK_MAIL, "MAIL_SERVER")
        self.MAIL_PORT = config_parser.get(self._SECTION_FLASK_MAIL, "MAIL_PORT")
        self.MAIL_USE_TLS = config_parser.get(self._SECTION_FLASK_MAIL, "MAIL_USE_TLS")
        self.MAIL_USERNAME = config_parser.get(
            self._SECTION_FLASK_MAIL, "MAIL_USERNAME"
        )
        self.MAIL_PASSWORD = config_parser.get(
            self._SECTION_FLASK_MAIL, "MAIL_PASSWORD"
        )
