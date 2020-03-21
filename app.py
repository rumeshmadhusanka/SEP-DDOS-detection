import time

from flask import Flask
from flask import jsonify
from flask_pymongo import PyMongo

from modules.JSONEncoder import JSONEncoder
from modules.config import DevelopmentConfig

app = Flask(__name__)
app.config.from_object(DevelopmentConfig)
mongo = PyMongo(app)

app.json_encoder = JSONEncoder


@app.route('/', methods=['GET'])
def get_all():
    output = mongo.db.applogs.find()
    result = []
    for i in output:
        result.append(i)
        print(type(i['time']))
    return jsonify(result)


@app.before_first_request
def before_first():
    a = int(round(time.time() * 1000))
    print(a)
    print(time.time())


# @app.route('/star/', methods=['GET'])
# def get_one_star(name):
#     star = mongo.db.stars
#     s = star.find_one({'name': name})
#     if s:
#         output = {'name': s['name'], 'distance': s['distance']}
#     else:
#         output = "No such name"
#     return jsonify({'result': output})
#
#
# @app.route('/star', methods=['POST'])
# def add_star():
#     star = mongo.db.stars
#     name = request.json['name']
#     distance = request.json['distance']
#     star_id = star.insert({'name': name, 'distance': distance})
#     new_star = star.find_one({'_id': star_id})
#     output = {'name': new_star['name'], 'distance': new_star['distance']}
#     return jsonify({'result': output})


if __name__ == '__main__':
    app.run(port=app.config['PORT'], debug=True)
