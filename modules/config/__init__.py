class Config(object):
    DEBUG = False
    TESTING = False
    MONGO_URI = 'mongodb://localhost:27017'
    MONGO_DATABASE = 'test'
    MONGO_LOG_COLLECTION = 'applogs'
    MONGO_IP_COLUMN_NAME = 'hostname'
    BETA = 3
    OMEGA = 0
    PORT = 4000
    SLIDING_WINDOW = 20  # 20 seconds
    SLIDING_WINDOW_PIECE = 5  # 5 seconds


class ProductionConfig(Config):
    MONGO_URI = 'mongodb+srv://rumesh:password-abc123@medical-cluster-efyfq.mongodb.net'


class DevelopmentConfig(Config):
    DEBUG = True
    FLASK_ENV = 'development'


class TestingConfig(Config):
    TESTING = True
