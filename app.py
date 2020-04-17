import os

from flask import Flask
from flask_pymongo import PyMongo

from modules.JSONEncoder import JSONEncoder
from modules.config import Config as Conf
from modules.routes import expose_routes

app = Flask(__name__)
app.config.from_object(Conf)
mongo = PyMongo(app)
thread = None
app.json_encoder = JSONEncoder
expose_routes(app, mongo)


@app.before_first_request
def schedule_threaded_task():
    pass
    # ddos_detection()


if __name__ == '__main__':
    app.run(port=app.config['PORT'], debug=True)
