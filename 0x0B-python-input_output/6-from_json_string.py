#!/usr/bin/python3
import json


def from_json_string(my_str):
    """ Return object representation json string """
    return json.loads(my_str)
