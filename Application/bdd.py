import json
import os

THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
file_poste = os.path.join(THIS_FOLDER, 'poste.json')


def read_bd():
    with open("poste.json", "r") as read_file:
        return json.load(read_file)


def obj_dict(obj):
    return obj.__dict__


def write_bd(data):
    with open("poste.json", "w") as write_file:
        json_string = json.dumps(data, default=obj_dict)
        write_file.write(json_string)
