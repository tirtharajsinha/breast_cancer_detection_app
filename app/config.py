class Config(object):
    DEBUG = True
    DEVELOPMENT = True
    SECRET_KEY = 'hlky288dnp10eskj'
    # FLASK_HTPASSWD_PATH = '/secret/.htpasswd'
    # SQLALCHEMY_DATABASE_URI = 'sqlite:///registration.db'
    FLASK_SECRET = SECRET_KEY


class ProductionConfig(Config):
    DEVELOPMENT = False
    DEBUG = False
