import os
from os import environ

from dotenv import load_dotenv

try:
    dotenv_path = os.path.join(os.path.dirname(__file__), '../../.env')
    load_dotenv(dotenv_path)
except Exception as e:
    print("Could not load .env file ", e)


class Config(object):
    DEBUG = environ.get("DEBUG")
    NODE_NAME = environ.get("NODE_NAME")
    MONGO_URI = environ.get("MONGO_URI")
    MONGO_DATABASE = environ.get("MONGO_DATABASE")
    MONGO_LOG_COLLECTION = environ.get("MONGO_LOG_COLLECTION")
    MONGO_IP_COLUMN_NAME = environ.get("MONGO_IP_COLUMN_NAME")
    BETA = environ.get("BETA")
    OMEGA = environ.get("OMEGA")
    PORT = environ.get("PORT")
    SLIDING_WINDOW = environ.get("SLIDING_WINDOW")  # 20 seconds
    SLIDING_WINDOW_PIECE = environ.get("SLIDING_WINDOW_PIECE")  # 5 seconds
    API_GATEWAY_HEALTH_ENDPOINT = environ.get("API_GATEWAY_HEALTH_ENDPOINT")
    API_GATEWAY_KEY = environ.get("API_GATEWAY_KEY")
    DDOS_DETECTION_ON = environ.get("DDOS_DETECTION_ON")


if __name__ == "__main__":
    p = Config()
    print(type(p.DDOS_DETECTION_ON))
