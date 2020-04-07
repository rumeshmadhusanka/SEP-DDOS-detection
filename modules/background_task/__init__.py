from datetime import datetime

import pymongo


def get_data_in_interval(mongo_resource, start, end):
    cursor = mongo_resource.find({
        "time": {
            "$gte": start,
            "$lt": end
        }
    }).limit(500)
    return cursor


def generate_time_intervals(start1, interval_size, end1):
    """
   :param  (int) interval_size: interval size to break to in milli seconds
   :param (int) start: start time in milliseconds
   :param (int) end: end time in milliseconds
   :return: list of time intervals
   """
    start1 = int(start1)
    end1 = int(end1)
    interval_list1 = []
    n = int((end1 - start1) / interval_size)
    print("n: " + str(n))
    counter = start1
    for i in range(n):
        interval_list1.append([counter, counter + interval_size])
        counter += interval_size

    return interval_list1


def get_result_table(data):
    res = {}
    col_name = 'hostname'
    for i in data:
        if i[col_name] not in res:
            res[i[col_name]] = 1
        else:
            res[i[col_name]] += 1
    return res


def task():
    my_client = pymongo.MongoClient("mongodb://localhost:27017/")
    my_db = my_client["test"]
    my_col = my_db["applogs"]
    mongo_res = my_col
    interval_size = 20000

    start = int(datetime.strptime('28.08.1995 00:00:34,00',
                                  '%d.%m.%Y %H:%M:%S,%f').timestamp() * 10000)
    # full: 10:01:28
    # 500: 00:04:00
    end = int(datetime.strptime('28.08.1995 00:04:00,00',
                                '%d.%m.%Y %H:%M:%S,%f').timestamp() * 10000)

    interval_list = generate_time_intervals(start, interval_size, end)
    result = []
    for lst in interval_list:
        data = get_data_in_interval(mongo_res, lst[0], lst[1])
        result.append(get_result_table(data))
    return result


if __name__ == "__main__":
    print(task())
