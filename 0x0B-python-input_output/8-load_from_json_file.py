#!/usr/bin/python3
import json


def load_from_json_file(filename):
    """create un object from json file """
    with open(filename) as file:
        return json.load(file)
