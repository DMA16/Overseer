import json


def __read_sw__(path:str)->dict:
    with open(path, "r", encoding="utf8") as sw_file:
        return sw_file.readlines()


def __read_conf__(path:str)->dict:
    with open(path,"r") as conf_file:
        return json.loads(conf_file.read())


config = __read_conf__("data/env.json")
swearings = __read_sw__("data/swearings.txt")