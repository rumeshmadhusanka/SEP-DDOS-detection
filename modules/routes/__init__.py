from flask import jsonify


def expose_routes(app, mongo):
    @app.route('/', methods=['GET'])
    def get_all():
        output = mongo.db.applogs.find().limit(5)
        result = []
        for i in output:
            result.append(i)
        return jsonify(result)

    @app.route('/ping/', methods=['GET'])
    def ping():
        return jsonify({"ping": "pong"})

    @app.route('/ping/pong/', methods=['GET'])
    def ping_pong():
        return jsonify({"ping": "ping pong"})
