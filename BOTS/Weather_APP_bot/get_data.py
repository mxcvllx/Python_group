from expt import exceptions
import json


def get_data():
    file = None
    try:
        with open("tashkent.json", encoding="utf8") as f:
            file = json.load(f)
    except FileNotFoundError as e:
        exceptions(e)
    return file
