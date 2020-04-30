from datetime import datetime

import numpy
import pymongo
import pytest

from modules.background_task import generate_time_intervals, get_data_in_interval
from modules.background_task import get_result_table
from modules.background_task.sliding_window_method import average
from modules.background_task.sliding_window_method import cal_entropy_per_window
from modules.background_task.sliding_window_method import cal_std_deviation
from modules.background_task.variance_method import cal_average_entropy_for_each_conn
from modules.background_task.variance_method import cal_entropy
from modules.background_task.variance_method import cal_variance
from modules.background_task.variance_method import find_possibles
from modules.background_task.variance_method import key_in_dict
from modules.config import Config
from modules.JSONEncoder import JSONEncoder
from test_data import data_list


def test_config():
    assert Config
    assert Config.MONGO_URI
    assert int(Config.PORT)
    assert Config.DEBUG
    assert Config.NODE_NAME
    assert Config.MONGO_DATABASE
    assert int(Config.BETA)
    assert not int(Config.OMEGA)
    assert int(Config.SLIDING_WINDOW)
    assert int(Config.SLIDING_WINDOW_PIECE)


@pytest.fixture(scope="module")
def test_get_data_in_interval():
    my_client = pymongo.MongoClient(Config.MONGO_URI)
    my_db = my_client[Config.MONGO_DATABASE]
    mongo_res = my_db[Config.MONGO_LOG_COLLECTION]
    start = int(datetime.now().timestamp() * 10000 - float(Config.SLIDING_WINDOW) * 1000)
    end = int(datetime.now().timestamp() * 10000)
    cursor = get_data_in_interval(mongo_res, start, end)
    print(type(cursor))
    assert type(cursor) == pymongo.cursor.Cursor
    return cursor


def test_generate_time_intervals():
    start = 500
    end = 5400
    win = 5
    expected = 980
    lst = generate_time_intervals(start, win, end)
    assert type(lst) == list
    assert len(lst) == expected
    assert type(lst[0]) == list


def test_get_result_table(test_get_data_in_interval):
    res = get_result_table(test_get_data_in_interval)
    assert type(res) == dict
    assert res.keys() is not None
    with pytest.raises(AssertionError):
        assert type(res) == list


@pytest.fixture(scope="module")
def test_cal_entropy_per_window():
    out = cal_entropy_per_window(data_list)
    assert type(out) == list
    assert len(out) != 0
    for i in range(len(out)):
        assert type(out[i]) == numpy.float64
    return out


@pytest.fixture(scope="module")
def test_average(test_cal_entropy_per_window):
    a = average([0, 0, 0, 0, 0])
    b = average(test_cal_entropy_per_window)
    c = average([])
    assert a == 0
    assert c == 0
    assert b == 3.777233940320172
    with pytest.raises(TypeError):
        average(45)
    with pytest.raises(TypeError):
        average("string")
    return b


def test_cal_std_deviation(test_cal_entropy_per_window, test_average):
    a = cal_std_deviation(test_cal_entropy_per_window, test_average)
    b = cal_std_deviation([0, 0, 0, 0], 0)
    c = cal_std_deviation([0, 0, 0, 0], 45)
    assert a == 0.6291135436856912
    assert b == 0
    assert c == 45
    with pytest.raises(TypeError):
        cal_std_deviation(343, 432)
    return a


def test_key_in_dict():
    a = key_in_dict(3, {"4": 4, "3": 3})
    b = key_in_dict(23, {23: 32})
    assert not a
    assert b
    assert type(b) == int


@pytest.fixture(scope="module")
def test_cal_entropy():
    a = cal_entropy(data_list)
    b = cal_entropy([{}, {}, {}])
    c = cal_entropy([])
    assert type(a) == dict
    assert b == {}
    assert c == {}
    return a


@pytest.fixture(scope="module")
def test_cal_average_entropy_for_each_conn(test_cal_entropy):
    a = cal_average_entropy_for_each_conn(test_cal_entropy)
    assert type(a) == dict
    for i in a.keys():
        assert type(i) == str
        assert type(a[i]) == numpy.float64
    return a


@pytest.fixture(scope="module")
def test_cal_variance(test_cal_entropy, test_cal_average_entropy_for_each_conn):
    a = cal_variance(test_cal_entropy, test_cal_average_entropy_for_each_conn)
    b = cal_variance({}, {})
    assert not b
    assert type(a) == dict

    return a


def test_find_possibles(test_cal_variance):
    a = find_possibles(test_cal_variance, data_list)
    for i in a.keys():
        assert type(i) == str
        assert type(a[i]) == dict
        assert a
    return a


if __name__ == "__main__":
    test_get_data_in_interval()
