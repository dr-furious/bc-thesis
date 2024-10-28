import json


def load_json(json_path: str, mode='r') -> dict:
    with open(json_path, mode) as json_file:
        data = json.load(json_file)
    return data
