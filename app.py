import atexit
import time
from datetime import datetime

from apscheduler.schedulers.background import BackgroundScheduler
from flask import Flask
from flask import jsonify
from flask_pymongo import PyMongo

from modules.JSONEncoder import JSONEncoder
from modules.config import DevelopmentConfig
from modules.routes import expose_routes
app = Flask(__name__)
app.config.from_object(DevelopmentConfig)
mongo = PyMongo(app)

app.json_encoder = JSONEncoder

n = 0

expose_routes(app, mongo)


def get_data_in_interval(mongo_resource, start, end):
    cursor = mongo_resource.find({
        "time": {
            "$gte": start,
            "$lt": end
        }
    }).limit(500)
    # result = []
    # for i in cursor:
    #     result.append(i)
    # print(len(result))
    return cursor


def get_result_table(data):
    result = {}
    col_name = 'hostname'
    for i in data:
        if i[col_name] not in result:
            result[i[col_name]] = 1
        else:
            result[i[col_name]] += 1
    return result


def generate_time_intervals(start, interval_size, end):
    """
   :param  (int) interval_size: interval size to break to in milli seconds
   :param (int) start: start time in milliseconds
   :param (int) end: end time in milliseconds
   :return: list of time intervals
   """
    start = int(start)
    end = int(end)
    interval_list = []
    global n
    n = int((end - start) / interval_size)
    print("n: " + str(n))
    counter = start
    for i in range(n):
        interval_list.append([counter, counter + interval_size])
        counter += interval_size

    return interval_list


@app.route('/display/', methods=['GET'])
def get_ping():
    mongo_res = mongo.db.applogs
    interval_size = 20000
    start = int(datetime.strptime('28.08.1995 00:00:34,00',
                                  '%d.%m.%Y %H:%M:%S,%f').timestamp() * 10000)
    # full: 10:01:28
    # 500: 00:04:00
    end = int(datetime.strptime('28.08.1995 00:04:00,00',
                                '%d.%m.%Y %H:%M:%S,%f').timestamp() * 10000)
    interval_list = generate_time_intervals(start, interval_size, end)
    # print(interval_list)
    result = []
    for lst in interval_list:
        data = get_data_in_interval(mongo_res, lst[0], lst[1])
        result.append(get_result_table(data))
    return jsonify(result)


# def print_date_time():
#     print(time.strftime("%A, %d. %B %Y %I:%M:%S %p"))
#
#
# @app.before_first_request
# def init_scheduler():
#     scheduler = BackgroundScheduler()
#     scheduler.add_job(func=print_date_time, trigger="interval", seconds=3)
#     scheduler.start()
#     # Shut down the scheduler when exiting the app
#     atexit.register(lambda: scheduler.shutdown())


if __name__ == '__main__':
    app.run(port=app.config['PORT'], debug=True)
