class Config(object):
    DEBUG = False
    TESTING = False
    MONGO_URI = 'mongodb://localhost:27017/test'
    PORT = 4000


class ProductionConfig(Config):
    DATABASE_URI = 'mysql://user@localhost/foo'


class DevelopmentConfig(Config):
    DEBUG = True
    FLASK_ENV = 'development'


class TestingConfig(Config):
    TESTING = True
