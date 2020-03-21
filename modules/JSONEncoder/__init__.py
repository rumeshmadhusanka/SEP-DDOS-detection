import json
from datetime import datetime

from bson import ObjectId


class JSONEncoder(json.JSONEncoder):
    """ extend json-encoder class"""

    def default(self, o):
        if isinstance(o, ObjectId):
            return str(o)
        if isinstance(o, datetime):
            return str(o)
        return json.JSONEncoder.default(self, o)
