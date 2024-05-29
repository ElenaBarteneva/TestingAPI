import json
import os.path


def get_current_path(file_name: str):
    current_path = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(current_path, file_name)


def get_json_data(json_data):
    config_file = get_current_path(json_data)
    with open(config_file) as file:
        config_data = json.load(file)
    return config_data
