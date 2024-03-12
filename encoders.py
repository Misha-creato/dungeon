from json import JSONEncoder
from monster import Monster


class MonsterJSONEncoder(JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Monster):
            return vars(obj)
        return JSONEncoder.default(self, obj)
