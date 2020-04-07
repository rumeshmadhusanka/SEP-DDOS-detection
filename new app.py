from threading import Thread

from flask import Flask
from flask_pymongo import PyMongo

from modules.JSONEncoder import JSONEncoder
from modules.background_task import task
from modules.config import DevelopmentConfig
from modules.routes import expose_routes

app = Flask(__name__)
app.config.from_object(DevelopmentConfig)
mongo = PyMongo(app)
thread = None
app.json_encoder = JSONEncoder
expose_routes(app, mongo)


@app.before_first_request
def schedule_threaded_task(duration=5):
    global thread
    thread = Thread(target=task, args=())
    thread.daemon = True
    thread.start()


if __name__ == '__main__':
    app.run(port=app.config['PORT'], debug=True)
