import os

import psutil
import requests
from flask import jsonify
from uptime import uptime

from modules.config import Config


def expose_routes(app, mongo):
    @app.route('/', methods=['GET'])
    def index():
        return jsonify({"Hello": "World"})

    @app.route('/ping/', methods=['GET'])
    def ping():
        try:
            r = requests.get(Config.API_GATEWAY_HEALTH_ENDPOINT)
            return jsonify(r.json())
        except ConnectionError as e:
            return "Error"

    @app.route('/health', methods=['GET'])
    def health():
        name = Config.NODE_NAME
        pid = os.getpid()
        py = psutil.Process(pid)
        cpu = py.cpu_percent()
        upt = uptime()
        avg_load = os.getloadavg()[0]
        free_mem = psutil.virtual_memory()
        memoryUse = py.memory_info()[0]  # todo change all the values to a standard format
        return jsonify({"name": name,
                        "cpu": cpu,
                        "uptime": upt,
                        "free_mem": free_mem[0],  # change free mem
                        "total_mem": memoryUse,
                        "load_avg": avg_load})
