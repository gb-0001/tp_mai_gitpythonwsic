  
import os 
import json

THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
file_poste = os.path.join(THIS_FOLDER, 'poste.json')


def read_bd():
    with open("poste.json", "r") as read_file:
        return json.load(read_file)


def write_bd():
    with open("poste.json", "r") as read_file:
        pass
        #return  json.dump(data, read_file)